char a;


void setup() {
  Serial.begin(57600);              //Starting serial communication
  pinMode(LED_BUILTIN, OUTPUT);
  delay(10000);
  
  Serial.write(0x0a);
  //delay(10);
  Serial.write(0x0a);
  //delay(10);
  Serial.write(0x0a);
  //delay(10);
  Serial.write(0x0a);
  //delay(10);
  Serial.write(0x2e);
  //delay(100);
  Serial.write(0x30);
  //delay(10);
  Serial.write(0x31);
  //delay(10);
  Serial.write(0x32);
  //delay(10);
  Serial.write(0x33);
  //delay(10);
  Serial.write(0x34);
  //delay(10);
  Serial.write(0x35);
  //delay(10);
  Serial.write(0x36);
  //delay(10);
  Serial.write(0x37);
  //delay(10);
  Serial.write(0x38);
  //delay(10);
  Serial.write(0x39);
  //delay(10);
  Serial.write(0x0d);
  //delay(10);
  
}
  
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on
  Serial.write(0x34);
  delay(100);
}
