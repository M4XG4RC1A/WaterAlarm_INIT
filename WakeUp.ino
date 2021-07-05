
int pinWater = 2;
int pinBuzz = 3;

void setup() {
  pinMode(pinWater,OUTPUT);
  pinMode(pinBuzz,OUTPUT);
  digitalWrite(pinWater,HIGH);
  digitalWrite(pinBuzz,HIGH);
}

void loop() {
  if (Serial.available()) {
    int val = Serial.read();
    if(val == 'u'){
      digitalWrite(pinWater,HIGH);
      digitalWrite(pinBuzz,HIGH);
    }
  }
}
