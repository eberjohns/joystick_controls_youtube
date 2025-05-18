const int joyXPin = A0;
const int joyYPin = A1;
const int joyButtonPin = 2;
const int threshold = 100;

void setup() {
  Serial.begin(9600);
  pinMode(joyButtonPin, INPUT_PULLUP);
}

void loop() {
  int xValue = analogRead(joyXPin);
  int yValue = analogRead(joyYPin);
  int buttonState = digitalRead(joyButtonPin);

  if (xValue < (512 - threshold)) {
    Serial.println("LEFT");
    delay(100);
  } else if (xValue > (512 + threshold)) {
    Serial.println("RIGHT");
    delay(100);
  } else if (yValue < (512 - threshold)) {
    Serial.println("UP");
    delay(100);
  } else if (yValue > (512 + threshold)) {
    Serial.println("DOWN");
    delay(100);
  }

  if (buttonState == LOW) {
    Serial.println("PRESS");
    while (digitalRead(joyButtonPin) == LOW) {
      delay(10);
    }
    delay(200);
  }

  delay(50);
}
