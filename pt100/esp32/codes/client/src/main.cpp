#include <Arduino.h>
#include <ArduinoJson.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <LiquidCrystal.h>

/**
 * This is a header file which contains WiFi network credentials and URLs
 * Its contents are:
 *
 * const char *ssid = "YOUR-SSID-HERE";
 * const char *password = "YOUR-PASSWORD-HERE";
 * const char *tempURL = "URL-TO-PUT-TEMPERATURE";
*/
#include "credentials.h"

#define A -3.975e-6
#define B 2.894e-3
#define C 1.568
#define PIN_TEMP 34
#define RS 19
#define EN 23
#define D4 18
#define D5 17
#define D6 16
#define D7 15
#define NCOLS 16
#define NROWS 2

WiFiClient client;
HTTPClient temp;
LiquidCrystal lcd(RS, EN, D4, D5, D6, D7);

void setup() {
  Serial.begin(9600);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
  Serial.println();
  Serial.println(WiFi.localIP());
  temp.begin(client, tempURL);
  lcd.begin(NCOLS, NROWS);
  lcd.clear(); lcd.setCursor(0,0);
  lcd.print("Temperature ("); lcd.print((char)223); lcd.print("C)");
}

float getTemp() {
  float analogValue = analogRead(PIN_TEMP);
  float V = 3.3*analogValue/4095;
  Serial.println(V);
  return (B - sqrtl(B*B+4*A*(C-V)))/(2*A);
}

void dispTemp(float t) { 
  lcd.setCursor(0,1);
  lcd.print(t);
}

void loop() {
  temp.addHeader("Content-Type", "application/json");
  StaticJsonDocument<200> doc;
  doc["temp"] = getTemp();
  String requestBody;
  serializeJson(doc, requestBody);
  int httpResponseCode = temp.PUT(requestBody);
  dispTemp(doc["temp"]);
  delay(2500);
}
