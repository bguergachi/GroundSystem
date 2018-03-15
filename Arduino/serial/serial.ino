char a;


void setup() {
  Serial.begin(57600);              //Starting serial communication
  pinMode(LED_BUILTIN, OUTPUT);
}
  
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on
  Serial.write("\nGood\r");
  Serial.write("\n5890231\r");
  Serial.write("\n453623\r");
  Serial.write("\nHello\r");
  Serial.write("\n95734573467\r");
  Serial.write("\n3489560123.4112334\r");
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED on
  delay(500);
}
