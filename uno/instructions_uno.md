# Instructions for Arduino Uno YouTube Controller

This guide will help you set up your Arduino Uno and Python script to control YouTube using a 5-way joystick.

## Materials:

* Arduino Uno board
* 5-way Joystick module (with center press)
* Jumper wires
* USB cable (Type A to B)
* Python 3 installed on your computer
* `pyserial` and `pyautogui` Python libraries installed (`pip install pyserial pyautogui`)

## Connections:

Connect the joystick to your Arduino Uno as follows:

| Joystick Pin | Arduino Uno Pin (Example) |
| :---------- | :------------------------ |
| VCC         | 5V                      |
| GND         | GND                     |
| VRx         | A0                      |
| VRy         | A1                      |
| SW          | 2                       |

## Setup:

1.  **Upload the Arduino Sketch:**
    * Open the `youtube_joystick_uno.ino` file in the Arduino IDE.
    * Ensure your Arduino Uno board is selected (`Tools > Board > Arduino Uno`).
    * Select the correct serial port for your Arduino (`Tools > Port`).
    * Upload the sketch to your Arduino Uno.

2.  **Install Python Libraries:**
    * If you haven't already, open your command prompt or terminal and install the necessary Python libraries:
        ```bash
        pip install pyserial pyautogui
        ```

3.  **Run the Python Script:**
    * Save the `youtube_controller.py` file to a location on your computer.
    * Open the file in a text editor.

4.  **Configure the Python Script:**
    * **`SERIAL_PORT`:** Change the value of the `SERIAL_PORT` variable (e.g., `'COM3'` on Windows, `/dev/ttyACM0` on Linux, `/dev/cu.usbmodemXXXX` on macOS) to the serial port your Arduino Uno is connected to. You can usually find this in the Arduino IDE under `Tools > Port`.
    * **`BAUD_RATE`:** Ensure the `BAUD_RATE` is set to `9600` to match the Arduino sketch.
    * **`KEY_LEFT`, `KEY_RIGHT`, `KEY_UP`, `KEY_DOWN`, `KEY_PLAY_PAUSE`:** These variables define the keyboard shortcuts that will be sent to control YouTube.
        * `KEY_LEFT`: Default is the left arrow key (seek backward 10 seconds).
        * `KEY_RIGHT`: Default is the right arrow key (seek forward 10 seconds).
        * `KEY_UP`: Default is `pageup` (you might need to change this to your operating system's volume up shortcut, e.g., `'f12'` on some Windows systems when used with the Fn key).
        * `KEY_DOWN`: Default is `pagedown` (you might need to change this to your operating system's volume down shortcut, e.g., `'f11'` on some Windows systems when used with the Fn key).
        * `KEY_PLAY_PAUSE`: Default is the spacebar.
        **To use a different keyboard shortcut, simply change the string value assigned to these variables to the desired key (e.g., `'k'`, `'l'`, `'alt+p'`, etc., as recognized by `pyautogui`).** Refer to the `pyautogui` documentation for available key names.
    * **`REPEAT_DELAY`:** This variable (set to `0.1` seconds by default) controls the minimum time between repeated key presses when you hold the joystick left, right, up, or down. You can adjust this value (in seconds) to make the seeking or volume changes faster or slower when holding the joystick.

5.  **Run the Script:**
    * Open your command prompt or terminal.
    * Navigate to the directory where you saved `youtube_controller.py`.
    * Run the script using: `python youtube_controller.py`
    * Keep this script running in the background while you use YouTube.

6.  **Control YouTube:**
    * Open a YouTube video in your web browser.
    * Use the joystick to control playback, seeking, and volume.

## Stopping the Script:

* Press `Ctrl + C` in the terminal or command prompt window where the script is running.
