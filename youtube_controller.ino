const int joyXPin = A0;
const int joyYPin = A1;
const int joyButtonPin = 2;
const int threshold = 100;
const int debounceDelay = 200;
unsigned long lastButtonPress = 0;

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
    delay(500);
  } else if (xValue > (512 + threshold)) {
    Serial.println("RIGHT");
    delay(500);
  } else if (yValue < (512 - threshold)) {
    Serial.println("UP");
    delay(500);
  } else if (yValue > (512 + threshold)) {
    Serial.println("DOWN");
    delay(500);
  }

  if (buttonState == LOW && (millis() - lastButtonPress > debounceDelay)) {
    Serial.println("PRESS");
    lastButtonPress = millis();
    delay(200);
  }

  delay(50);
}