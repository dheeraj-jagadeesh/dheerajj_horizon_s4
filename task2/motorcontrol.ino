#include <Servo.h>

Servo servos[6];
int servoPins[6] = {3, 5, 6, 9, 10, 11}; 
int targetAngles[6];
int currentAngles[6] = {90, 90, 90, 90, 90, 90}; 

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 6; i++) {
    servos[i].attach(servoPins[i]);
    servos[i].write(currentAngles[i]);
  }
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    sscanf(data.c_str(), "%d,%d,%d,%d,%d,%d", &targetAngles[0], &targetAngles[1], &targetAngles[2], &targetAngles[3], &targetAngles[4], &targetAngles[5]);
    moveServosSmoothly();
  }
}

void moveServosSmoothly() {
  bool allReached = false;
  while (!allReached) {
    allReached = true;
    for (int i = 0; i < 6; i++) {
      if (currentAngles[i] < targetAngles[i]) {
        currentAngles[i]++;
        allReached = false;
      } else if (currentAngles[i] > targetAngles[i]) {
        currentAngles[i]--;
        allReached = false;
      }
      servos[i].write(currentAngles[i]);
    }
    delay(20); 
  }
}
