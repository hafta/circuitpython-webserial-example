A CircuitPython and Web Serial Example Project
----------------------------------------------

This example project includes a CircuitPython code.py file to be run on an
ESP32 or similar device and a standalone webserial.html file for sending text to
the device to be displayed on the embedded display.

The CircuitPython code.py file depends on adafruit_display_text which is not
part of CircuitPython and can be downloaded from Adafruit here.
https://learn.adafruit.com/circuitpython-display-text-library/setup

Install the code.py and adafruit_display_text on the device by dragging and
dropping into the mounted USB device.

The project was tested with an Adafruit ESP32-S2 TFT Feather.
https://learn.adafruit.com/adafruit-esp32-s2-tft-feather/overview

Open webserial.html in the browser and click connect and then choose
your connected device. Requires a browser that supports Web Serial such as
Firefox 151+ or Chromium-based browsers.

Send text "led on" and "led off" to toggle the LED light. All other text is
written to the device display.