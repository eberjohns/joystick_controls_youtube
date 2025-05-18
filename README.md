# joystick_controls_youtube

This repository contains the code and instructions to create a custom controller for YouTube using an Arduino and a 5-way joystick.

It includes separate folders for Arduino Uno (which requires a host-side Python script due to its lack of native USB HID) and Arduino Leonardo/Micro (which can directly act as a USB keyboard).

## Folders:

* **uno/**: Contains the Arduino sketch (.ino), the host-side Python script (.py), and setup instructions for using an Arduino Uno as the controller.
* **leonardo_micro/**: Contains the Arduino sketch (.ino) and setup instructions for using an Arduino Leonardo or Micro as the controller.

For detailed setup and usage, please refer to the `instructions.md` file within each respective folder.
