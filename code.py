import board
import digitalio
import displayio
import neopixel_write
import sys
import terminalio

from adafruit_display_text import label, wrap_text_to_pixels

SCALE = 4 # Scale factor for text size
display = board.DISPLAY

# Black background
bg = displayio.Bitmap(display.width, display.height, 1)
palette = displayio.Palette(1)
palette[0] = 0x000000

text_label = label.Label(
    terminalio.FONT, text="",
    color=0xFFFFFF, scale=SCALE, x=2, y=20,
)

root = displayio.Group()
root.append(displayio.TileGrid(bg, pixel_shader=palette))
root.append(text_label)
display.root_group = root

np_pwr = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
np_pwr.switch_to_output(True)
np_pin = digitalio.DigitalInOut(board.NEOPIXEL)
np_pin.switch_to_output()

def set_led(on):
    neopixel_write.neopixel_write(
        np_pin, bytearray([60, 60, 60] if on else [0, 0, 0])
    )

def screen_print(text):
    lines = wrap_text_to_pixels(text, display.width // SCALE, terminalio.FONT)
    text_label.text = "\n".join(lines)

set_led(False)

screen_print("code.py started...")

while True:
    line = sys.stdin.readline().strip()
    if line == "led on":
        set_led(True)
    elif line == "led off":
        set_led(False)
    else:
        screen_print(line)
