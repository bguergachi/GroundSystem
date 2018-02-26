char a;


void setup() {
  Serial.begin(9600);              //Starting serial communication
  pinMode(LED_BUILTIN, OUTPUT);
}
  
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on
  Serial.write("\n50238\r");
  Serial.write("\n5890231\r");
  Serial.write("\n453623\r");
  Serial.write("\n4536722\r");
  Serial.write("\n45734573467\r");
  Serial.write("\n3489560123.4112334\r");
  delay(5000);
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED on
  delay(5000);
}
