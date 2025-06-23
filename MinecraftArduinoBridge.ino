void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char value = Serial.read();
    if (value == 'r') {  // 'r' = click destro
      digitalWrite(13, HIGH);
      delay(500);
      digitalWrite(13, LOW);
    }
  }
}
