#include <Keyboard.h>

const int joyXPin = A0;
const int joyYPin = A1;
const int joyButtonPin = 2;
const int threshold = 100;

// Debounce delay for the button (in milliseconds)
const int debounceDelay = 200;
unsigned long lastButtonPress = 0;

// Delay for repeated key presses (in milliseconds)
const int repeatDelay = 100;
unsigned long lastRepeatX = 0;
unsigned long lastRepeatY = 0;

void setup() {
  pinMode(joyButtonPin, INPUT_PULLUP);
  Keyboard.begin();
}

void loop() {
  int xValue = analogRead(joyXPin);
  int yValue = analogRead(joyYPin);
  int buttonState = digitalRead(joyButtonPin);
  unsigned long currentTime = millis();

  // Handle Left/Right (10 seconds seek)
  if (xValue < (512 - threshold) && (currentTime - lastRepeatX > repeatDelay)) {
    Keyboard.press(KEY_LEFT_ARROW);
    Keyboard.releaseAll();
    lastRepeatX = currentTime;
  } else if (xValue > (512 + threshold) && (currentTime - lastRepeatX > repeatDelay)) {
    Keyboard.press(KEY_RIGHT_ARROW);
    Keyboard.releaseAll();
    lastRepeatX = currentTime;
  }

  // Handle Up/Down (Volume control - using Page Up/Page Down as examples)
  if (yValue < (512 - threshold) && (currentTime - lastRepeatY > repeatDelay)) {
    Keyboard.press(KEY_UP); // Adjust if your OS has different volume up key
    Keyboard.releaseAll();
    lastRepeatY = currentTime;
  } else if (yValue > (512 + threshold) && (currentTime - lastRepeatY > repeatDelay)) {
    Keyboard.press(KEY_DOWN); // Adjust if your OS has different volume down key
    Keyboard.releaseAll();
    lastRepeatY = currentTime;
  }

  // Handle Center Press (Play/Pause - using Spacebar)
  if (buttonState == LOW && (currentTime - lastButtonPress > debounceDelay)) {
    Keyboard.press(' ');
    Keyboard.release(' ');
    lastButtonPress = currentTime;
  }

  delay(50);
}
