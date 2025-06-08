# Raspberry Pi Pico W Joystick Controller (YouTube/Game HID)

This project transforms a 5-way analog joystick module into a USB Human Interface Device (HID) that acts as a keyboard. It's configured for continuous key presses for directional movements (like YouTube seeking or game acceleration) and a single press for the joystick button (like YouTube play/pause or game jump).

## Materials Needed

* **Raspberry Pi Pico W** (your board without pre-soldered headers)
* **5-way Analog Joystick Module**
* **USB Micro-B Cable:** For connecting the Pico W to your computer/phone.

## Pin Connections (Joystick to Raspberry Pi Pico W)

| Joystick Pin | Raspberry Pi Pico W Connection (GPIO Name) | Physical Pin Number |
| :----------- | :---------------------------------------- | :------------------ |
| VCC          | 3V3 OUT                                   | 36                  |
| GND          | GND                                       | 38                  |
| VRx          | GP26 (ADC0)                               | 31                  |
| VRy          | GP27 (ADC1)                               | 32                  |
| SW           | GP17                                      | 22                  |

---

## Initial Setup (CircuitPython)

This project uses CircuitPython, which is excellent for USB HID projects on the Pico W.

### Step 1: Install CircuitPython Firmware on your Pico W

1.  **Download Firmware:** Go to the official CircuitPython website: [https://circuitpython.org/downloads](https://circuitpython.org/downloads)
    * Search for "Raspberry Pi Pico W" and download the **latest stable `.uf2` file**.
2.  **Enter Bootloader Mode:**
    * **Unplug** your Pico W from your computer.
    * **Press and hold the BOOTSEL button** on the Pico W.
    * While holding BOOTSEL, **plug the Pico W into your computer** using the USB Micro-B cable.
    * Release the BOOTSEL button.
3.  Your computer should now recognize the Pico W as a new USB drive named `RPI-RP2`.
4.  **Drag and Drop Firmware:** Drag the downloaded `.uf2` CircuitPython firmware file directly onto the `RPI-RP2` drive.
5.  The Pico W will automatically reboot. The `RPI-RP2` drive will disappear and be replaced by a new drive called `CIRCUITPY`. This confirms CircuitPython is now installed!

### Step 2: Install `adafruit_hid` Library

1.  **Download Library Bundle:** Go to [https://circuitpython.org/libraries](https://circuitpython.org/libraries)
    * Download the "Adafruit CircuitPython Library Bundle" (it's a `.zip` file). Make sure the bundle version matches your CircuitPython version (e.g., if you downloaded CircuitPython 9.x, get the 9.x bundle).
2.  **Extract Bundle:** Unzip the downloaded bundle on your computer. You'll find a folder named `lib` inside the extracted bundle.
3.  **Copy `adafruit_hid`:** Inside the extracted bundle's `lib` folder, find the `adafruit_hid` folder.
4.  **Copy to Pico W:** Drag and drop the *entire* `adafruit_hid` folder into the `lib` folder on your `CIRCUITPY` drive (your Pico W).
    * If you don't see a `lib` folder on your `CIRCUITPY` drive, create one, then copy `adafruit_hid` into it.

### Step 3: Install Thonny IDE (Recommended for Code Upload & Debugging)

1.  **Download Thonny:** Go to [https://thonny.org/](https://thonny.org/) and download the installer for your operating system.
2.  **Install Thonny:** Run the installer and follow the instructions.
3.  **Configure Thonny for CircuitPython:**
    * Open Thonny.
    * Go to `Tools > Options`.
    * Select the "Interpreter" tab.
    * From the "Interpreter" dropdown, choose "CircuitPython (generic)".
    * Thonny should automatically detect your Pico W's port. If not, select it from the "Port" dropdown.
    * Click "OK".
    * You should now see a CircuitPython prompt (e.g., `>>>`) in the "Shell" window at the bottom of Thonny. This indicates you are connected to your Pico W.

## Uploading the Code

Now, you'll place the Python file (`code.py`) onto your Pico W.

  **Copy `code.py`:**
  * In Thonny, click `File > New`  and paste the content of `code.py` (from above) into the new editor window.
  * Click `File > Save as...`.
  * Select "MicroPython device" (or "CircuitPython device").
  * Save the file in the root of your `CIRCUITPY` drive as `code.py`.
  * **Important:** CircuitPython automatically runs the `code.py` (or `main.py`) file when the board powers up or resets.

## How to Use

1.  Ensure your joystick module is correctly wired to your Pico W as per the "Pin Connections" table.
2.  Plug your Raspberry Pi Pico W into your computer or smartphone (via USB OTG adapter).
3.  Your device should recognize the Pico W as a standard USB keyboard.
4.  **For YouTube:**
    * Navigate to a YouTube video.
    * Move the joystick **Left/Right** to seek backward/forward (press-and-hold behavior).
    * Move the joystick **Up/Down** to control volume or scroll (you might need to adjust Keycodes in `code.py` if `UP_ARROW`/`DOWN_ARROW` don't work as expected for volume).
    * Press the **joystick button** to Play/Pause the video.
5.  **For Games (e.g., Hill Climb Racing):**
    * Launch the game on your phone.
    * You may need to experiment or check the game's settings for keyboard control mappings.
    * Typically, `LEFT_ARROW` and `RIGHT_ARROW` are used for movement/acceleration.
    * `SPACE` is common for jumping or action.
    * You might need to change `Keycode.UP_ARROW`/`Keycode.DOWN_ARROW` to specific game keys like `Keycode.W`/`Keycode.S` in your `code.py` if the game uses WASD controls.

## Tuning and Debugging

### **1. Adjusting Joystick Sensitivity (`THRESHOLD_ANALOG`)**

If your joystick constantly triggers actions even when it's at rest, or if it's not sensitive enough:

1.  **Temporarily modify `code.py` for debugging:**
    * Open `code.py` in Thonny.
    * Inside the `while True:` loop, near the beginning, add the following line:
        ```python
        print(f"Raw X: {x_val}, Raw Y: {y_val}")
        ```
    * Save `code.py`.
2.  **Observe values:** In Thonny's "Shell" window, watch the `Raw X` and `Raw Y` values when your joystick is perfectly at rest.
3.  **Adjust `THRESHOLD_ANALOG`:**
    * Note the typical range of `X` and `Y` values when the joystick is still (e.g., if X fluctuates between 31000 and 34000).
    * Calculate the maximum deviation from `CENTER_ANALOG` (32767).
    * In `code.py`, set `THRESHOLD_ANALOG` to a value slightly *larger* than this observed maximum deviation. This creates a "dead zone" around the center.
    * Save `code.py`.
4.  **Remove debug line:** Once satisfied, remove the `print` line from `code.py` and save it again.

### **2. Adjusting Button Debounce (`BUTTON_DEBOUNCE_MS`)**

If your joystick button causes multiple rapid presses (e.g., YouTube pausing and immediately playing again):

1.  In `code.py`, increase the `BUTTON_DEBOUNCE_MS` value.
2.  Start by trying `250` milliseconds. If the issue persists, try `300`.
3.  Save `code.py`.

### **3. `ImportError: no module named 'adafruit_hid....'`**

If you encounter this error (or similar `ImportError` for other `adafruit_hid` submodules):

* **Check `adafruit_hid` folder:** Ensure you copied the *entire* `adafruit_hid` folder (not just its contents) into the `lib` folder on your `CIRCUITPY` drive.
* **Correct version:** Make sure the Adafruit CircuitPython Library Bundle you downloaded matches the version of CircuitPython firmware installed on your Pico W.

---

This setup should give you a robust and configurable joystick controller for your projects!
