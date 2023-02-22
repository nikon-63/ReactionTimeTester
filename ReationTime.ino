//Button pin 4
//Led pin 12 with 220 Ohm resistor

int x = 1;
int times = 0;


//Set up a loop
void setup() {
  Serial.begin(9600); //Turn on the serial
  pinMode(12, OUTPUT); //Set up the light 
  pinMode(4, INPUT_PULLUP); // Set up the button
}


//Starting loop
void loop() {
  easy(); //Runs the easy mode          
}


//Function to turn light off 
void off() {
  digitalWrite(12, LOW); 
}


//Function to turn light on 
void on() {
  digitalWrite(12, HIGH);
}


//Function to flash light
void flash() {
  for (times=0; times < 5; times++) { //Runs in a loop 5 times
      off();
      delay(100);
      on();
      delay(100);
    }
   off();
}


//Easy mode
void easy() {
  x = 1; //Sets x to on for the loop
  flash();
  delay(1000);
  off();
  delay(random(500, 2000)); //Picks random time delay
  on();
  long int t1 = millis(); //Starts the timer 
  while (x == 1) { //Runs till x = 0
    byte buttonState = digitalRead(4); //Reads if the button has been clicked or not
    if (buttonState == LOW) { //When the button is clicked
      long int t2 = millis(); //Stops the timer
      Serial.println(t2-t1); //Prints out the time
      x = 0; //Sets x to 0 to stop the loop
      delay(50);
      off();
      delay(1000);
      }
  }
}
