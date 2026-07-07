import ctypes
import random
import time

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

SW = user32.GetSystemMetrics(0)
SH = user32.GetSystemMetrics(1)

# Works on ALL Windows versions
hdc = user32.GetDC(0)

def chaos():
    x = random.randint(0, SW)
    y = random.randint(0, SH)
    w = random.randint(100, SW)
    h = random.randint(100, SH)
    dx = random.randint(-200, 200)
    dy = random.randint(-200, 200)

    # Universal raster op (always works)
    gdi32.BitBlt(hdc, x, y, w, h, hdc, dx, dy, 0x00CC0020)

while True:
    chaos()
    time.sleep(0.02)

import ctypes
import random
import time
import sys

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# --- check if Python is 32-bit or 64-bit ---
is_64 = ctypes.sizeof(ctypes.c_void_p) == 8
if is_64:
    print("This is 64-bit Python. Desktop GDI chaos will NOT work.")
    print("You need a 32-bit Python (win32) build for this to affect the screen.")
    while True:
        time.sleep(1)  # just sit here so you can read the message
    sys.exit(0)

# --- minimize console ---
console = user32.GetConsoleWindow()
user32.ShowWindow(console, 6)  # SW_MINIMIZE

SW = user32.GetSystemMetrics(0)
SH = user32.GetSystemMetrics(1)

hdc = user32.GetDC(0)

def chaos():
    x = random.randint(0, SW)
    y = random.randint(0, SH)
    w = random.randint(100, SW)
    h = random.randint(100, SH)
    dx = random.randint(-200, 200)
    dy = random.randint(-200, 200)

    gdi32.BitBlt(hdc, x, y, w, h, hdc, dx, dy, 0x00CC0020)

while True:
    chaos()
    time.sleep(0.02)


