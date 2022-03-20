/*
Simple example to try DMX capability
Press a button to cycle through values
Current value will be shown as user LED brightness and will be sent to DMX
*/

#include "src/SparkFunDMX.h"
#define LED 22

SparkFunDMX dmx;
volatile byte value_index = 0;
byte values[] = {0, 1, 16, 32, 127, 255};

void setup() {
  
  pinMode(LED, OUTPUT);
  
  pinMode(26, OUTPUT); //rs485 rt lightbrain
  digitalWrite(26, LOW); //rs485 rt lightbrain
  
  pinMode(32, INPUT_PULLUP); //button
  pinMode(33, INPUT_PULLUP); //button

  attachInterrupt(digitalPinToInterrupt(32), button32, FALLING);
  attachInterrupt(digitalPinToInterrupt(33), button33, FALLING);

  ledcSetup(0, 5000, 13);
  ledcAttachPin(LED, 0);

  dmx.initWrite(5);
  delay(20);
}

void ledcAnalogWrite(uint8_t channel, uint32_t value, uint32_t valueMax = 255) {
  // calculate duty, 8191 from 2 ^ 13 - 1
  uint32_t duty = (8191 / valueMax) * min(value, valueMax);
  // write duty to LEDC
  ledcWrite(channel, duty);
}

void loop() {
  byte value = values[value_index];
  ledcAnalogWrite(0, value);

  // ***dmx send ***
  dmx.write(1, value);
  dmx.write(2, value);
  dmx.write(3, value);
  dmx.update();
}

void button32(){
  changeLightValues(1);
}

void button33(){
  changeLightValues(-1);
}

void changeLightValues(int dir) {
  int count = sizeof(values);
  if (dir>0) {
    value_index = (count + value_index + 1) % count;
  } else if (dir<0) {
    value_index = (count + value_index - 1) % count;
  }
}
