char dataString[50] = {0};
int a =0; 
int sensorPin = A1;    // select the input pin for the potentiometer
  // select the pin for the LED
int sensorValue = 0;

void setup() {
Serial.begin(9600);              //Starting serial communication
}
  
void loop() {
  sensorValue = analogRead(sensorPin);
   // a value increase every loop
  sprintf(dataString,"%02X",sensorValue); // convert a value to hexa 
  delay(1000);                  // give the loop some break
  Serial.println(dataString);   // send the data
}
