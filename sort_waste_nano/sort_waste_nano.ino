//#include "SoftwareSerial.h";
#include <Servo.h>

#include <FastLED_NeoPixel.h>

// Which pin on the Arduino is connected to the LEDs?
#define DATA_PIN 6

// How many LEDs are attached to the Arduino?
#define NUM_LEDS 60

// LED brightness, 0 (min) to 255 (max)
#define BRIGHTNESS 50

// Amount of time for each half-blink, in milliseconds
#define BLINK_TIME 1500

#define DUMP_DELAY 3000
#define ROTATE_HOME 100
#define DUMP_HOME 100

// CRGB leds[NUM_LEDS];
// Adafruit_NeoPixel strip(NUM_LEDS, DATA_PIN, NEO_GRB);  // <- Adafruit NeoPixel version
FastLED_NeoPixel<NUM_LEDS, DATA_PIN, NEO_GRB> strip;      // <- FastLED NeoPixel version

//int rxPin = 10;
//int txPin = 11;
//
//SoftwareSerial EspSerial(rxPin, txPin);

Servo rotateServo;
Servo dumpServo;

int dumpServoPin = 4;
int rotateServoPin = 3;

String wasteClassification;
String userInput;

void setup() {
  // put your setup code here, to run once:
  strip.begin();  // initialize strip (required!)
  strip.setBrightness(BRIGHTNESS);
  Serial.begin(9600);
  rotateServo.attach(rotateServoPin);
  dumpServo.attach(dumpServoPin);
  rotateServo.write(ROTATE_HOME);
  dumpServo.write(DUMP_HOME);
  strip.setPixelColor(0, strip.Color(254, 254, 254));  // set pixel 0 to blue
  strip.show();
}

void loop() {

   if(Serial.available()){
     userInput = Serial.readString();
     userInput.toLowerCase();
     userInput.trim();
     if(userInput == "plastic"){
       sortPlastic();
     } else if (userInput == "metal"){
       sortMetal();
     } else if (userInput == "paper" || userInput == "glass"){
     sortOther();
   } else {
    return;
   }
   }


}

void colorWipe(uint32_t color, unsigned long wait) {
  // Serial.println(strip.numPixels());
  for (unsigned int i = 0; i < strip.numPixels(); i++) {
    strip.setPixelColor(i, color);
    strip.show();
    delay(wait);
  }
}

void activateLeds(){
    colorWipe(strip.Color(255, 255, 255), 25);  // white
    delay(BLINK_TIME);
}

void deactivateLeds(){
    // strip.setPixelColor(0, strip.Color(0, 0, 0));  // set pixel 0 to blue
    // strip.setPixelColor(1, strip.Color(0, 0, 0));  // set pixel 0 to blue
    strip.clear();
    strip.show();
    delay(BLINK_TIME);
}

void sortPlastic(){
  activateLeds();
  dumpServo.write(145);
  delay(DUMP_DELAY);
  rotateServo.write(ROTATE_HOME);
  dumpServo.write(DUMP_HOME);
  deactivateLeds();
   return;
}

void sortMetal(){
  activateLeds();
  dumpServo.write(45);
  delay(DUMP_DELAY);
  rotateServo.write(ROTATE_HOME);
  dumpServo.write(DUMP_HOME);
  deactivateLeds();
   return;
}

void sortOther(){
//  activateLeds();
  rotateServo.write(10);
  delay(1000);
  dumpServo.write(45);
  delay(DUMP_DELAY);
  dumpServo.write(DUMP_HOME);
  delay(1000);
  rotateServo.write(ROTATE_HOME);
  deactivateLeds();
   return;
}
