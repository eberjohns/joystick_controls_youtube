# Instructions for Arduino Leonardo/Micro YouTube Controller

This guide will help you set up your Arduino Leonardo or Micro to directly control YouTube using a 5-way joystick. These boards have native USB HID capabilities and can act as a keyboard.

## Materials:

* Arduino Leonardo or Arduino Micro board
* 5-way Joystick module (with center press)
* Jumper wires
* USB cable (compatible with your Arduino board)

## Connections:

Connect the joystick to your Arduino Leonardo or Micro as follows:

| Joystick Pin | Arduino Pin (Example) |
| :---------- | :------------------------ |
| VCC         | 5V                      |
| GND         | GND                     |
| VRx         | A0                      |
| VRy         | A1                      |
| SW          | 2                       |

## Setup:

1.  **Open the Arduino Sketch:**
    * Open the `youtube_joystick_leonardo_micro.ino` file in the Arduino IDE.

2.  **Configure the Arduino Sketch (Optional):**
    * **Key Mappings:** The sketch uses `KEY_LEFT_ARROW`, `KEY_RIGHT_ARROW`, `KEY_UP`, `KEY_DOWN`, and `' '` (spacebar) as the default key presses.
        * `KEY_LEFT_ARROW`: Seeks backward 10 seconds.
        * `KEY_RIGHT_ARROW`: Seeks forward 10 seconds.
        * `KEY_UP`: Default is the "Volume Up" key (you might need to change this if your operating system uses a different key – common alternatives are `KEY_PAGE_UP` or function keys like `KEY_F12`).
        * `KEY_DOWN`: Default is the "Volume Down" key (you might need to change this, e.g., `KEY_PAGE_DOWN` or `KEY_F11`).
        * `' '` (spacebar): Play/Pause.
        **To use different keyboard shortcuts, you can change the `Keyboard.press()` arguments to other keys defined in the `Keyboard.h` library.** Refer to the Arduino documentation for the `Keyboard` library to see a list of available keys (e.g., `KEY_MEDIA_NEXT`, `KEY_MEDIA_PREVIOUS`, etc.).

    * **`repeatDelay`:** This variable (set to `100` milliseconds by default) controls the delay between repeated key presses when you hold the joystick left, right, up, or down. Adjust this value (in milliseconds) to make the seeking or volume changes faster or slower when holding the joystick.

3.  **Upload the Arduino Sketch:**
    * Ensure your Arduino Leonardo or Micro board is selected (`Tools > Board > Arduino Leonardo` or `Tools > Board > Arduino Micro`).
    * Select the correct serial port for your Arduino (`Tools > Port`).
    * Upload the sketch to your Arduino board.

4.  **Control YouTube:**
    * Open a YouTube video in your web browser.
    * Your Arduino should now be recognized as a USB keyboard. Use the joystick to control playback, seeking, and volume.

## Stopping:

* Simply disconnect the USB cable from your Arduino board.
