import ctypes
import random
import time

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

hdc = user32.GetDC(0)

sw = user32.GetSystemMetrics(0)
sh = user32.GetSystemMetrics(1)

start = time.time()
duration = 600  # 10 minutes

while time.time() - start < duration:

    cycle_start = time.time()

    # -------- STAGE 1: TUNNEL ZOOM --------
    for i in range(120):
        offset = i * 2
        gdi32.StretchBlt(
            hdc,
            offset, offset,
            sw - offset * 2,
            sh - offset * 2,
            hdc,
            0, 0,
            sw, sh,
            0x00CC0020
        )
        time.sleep(0.01)

    # -------- STAGE 2: STRETCH UPWARD --------
    for i in range(200):
        stretch = i * 2
        gdi32.StretchBlt(
            hdc,
            0, -stretch,
            sw, sh + stretch,
            hdc,
            0, 0,
            sw, sh,
            0x00CC0020
        )
        time.sleep(0.01)

    # -------- STAGE 3: SCRIBBLE --------
    for _ in range(400):
        x1 = random.randint(0, sw)
        y1 = random.randint(0, sh)
        x2 = random.randint(0, sw)
        y2 = random.randint(0, sh)

        color = random.randint(0, 0xFFFFFF)
        pen = gdi32.CreatePen(0, 3, color)
        old_pen = gdi32.SelectObject(hdc, pen)

        gdi32.MoveToEx(hdc, x1, y1, None)
        gdi32.LineTo(hdc, x2, y2)

        gdi32.SelectObject(hdc, old_pen)
        gdi32.DeleteObject(pen)

        time.sleep(0.003)

    # -------- STAGE 4: FULL-SCREEN INVERT --------
    for _ in range(80):
        gdi32.BitBlt(
            hdc,
            0, 0,
            sw, sh,
            hdc,
            0, 0,
            0x00990066  # NOTSRCCOPY
        )
        time.sleep(0.05)

    # -------- EXTRA CHAOS AFTER 3 MINUTES --------
    if time.time() - start >= 180:
        # Flood screen with random shapes
        for _ in range(300):
            shape_type = random.choice(["rect", "ellipse"])
            x1 = random.randint(0, sw)
            y1 = random.randint(0, sh)
            w = random.randint(20, 300)
            h = random.randint(20, 300)
            x2 = min(sw, x1 + w)
            y2 = min(sh, y1 + h)

            color = random.randint(0, 0xFFFFFF)
            brush = gdi32.CreateSolidBrush(color)

            rect = ctypes.wintypes.RECT(x1, y1, x2, y2)

            if shape_type == "rect":
                gdi32.FillRect(hdc, ctypes.byref(rect), brush)
            else:
                # Ellipse uses current brush
                old_brush = gdi32.SelectObject(hdc, brush)
                gdi32.Ellipse(hdc, x1, y1, x2, y2)
                gdi32.SelectObject(hdc, old_brush)

            gdi32.DeleteObject(brush)
            time.sleep(0.005)

# -------- FINAL MELTDOWN: CRT COLLAPSE + STATIC --------

for i in range(sh // 2):
    gdi32.StretchBlt(
        hdc,
        0, sh // 2 - i,
        sw, i * 2,
        hdc,
        0, 0,
        sw, sh,
        0x00CC0020
    )
    time.sleep(0.005)

for _ in range(5000):
    x = random.randint(0, sw - 1)
    y = random.randint(0, sh - 1)
    color = random.randint(0, 0xFFFFFF)
    gdi32.SetPixel(hdc, x, y, color)




