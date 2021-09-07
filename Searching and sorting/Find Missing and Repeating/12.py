String state;
void setup()
{
  pinMode(12, OUTPUT);
  Serial.begin(9600);
}
void loop()
{
  state=Serial.readString();
  if(state=="ON"){
    digitalWrite(12,HIGH);
    Serial.println("ON");
  delay(5000);
}
else if(state=="OFF"){
  digitalWrite(12, LOW);
    Serial.println("OFF");
  delay(5000);
}
  else{
    Serial.println("blink");
     digitalWrite(12, HIGH);
    delay(1000);
    digitalWrite(12, LOW);
     delay(1000);
  }
}
