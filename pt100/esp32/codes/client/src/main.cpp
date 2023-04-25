#include <Arduino.h>
#include <ArduinoJson.h>
#include <WiFi.h>
#include <HTTPClient.h>

/**
 * This is a header file which contains WiFi network credentials and URLs
 * Its contents are:
 *
 * const char *ssid = "YOUR-SSID-HERE";
 * const char *password = "YOUR-PASSWORD-HERE";
 * const char *statusURL = "URL-TO-PUT-ESP32-READY-STATUS"
 * const char *decisionURL = "URL-TO-READ-NEXT-MOVE"
*/
#include "credentials.h"

#define A -8.6837e-6
#define B 3.245e-3
#define C 1.553
#define TEMP_PIN 34

WiFiClient client;
HTTPClient temp;

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
}

float getTemp() {
  float analogValue = analogRead(TEMP_PIN);
  float V = 3.3*analogValue/4095;
  Serial.println(V);
  return (B - sqrtl(B*B+4*A*(C-V)))/(2*A);
}

void loop() {
  temp.addHeader("Content-Type", "application/json");
  StaticJsonDocument<200> doc;
  doc["temp"] = getTemp();
  String requestBody;
  serializeJson(doc, requestBody);
  int httpResponseCode = temp.PUT(requestBody);
  delay(2000);
  // doc["status"] = 1;
  // serializeJson(doc, requestBody);
  // httpResponseCode = status.PUT(requestBody);
  // // Process the order
  // if (order == 0) front();
  // else if (order == 1) {left(); front();}
  // else if (order == 2) back();
  // else if (order == 3) {right(); front();}
  // else if (order == 4) left();
  // doc["status"] = 0;
  // serializeJson(doc, requestBody);
  // httpResponseCode = status.POST(requestBody);
}
