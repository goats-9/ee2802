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
 * const char *tempURL = "URL-TO-PUT-TEMPERATURE"
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
  return (-B + sqrtl(B*B+4*A*(C-V)))/(2*A);
}

void loop() {
  temp.addHeader("Content-Type", "application/json");
  StaticJsonDocument<200> doc;
  doc["temp"] = getTemp();
  String requestBody;
  serializeJson(doc, requestBody);
  int httpResponseCode = temp.PUT(requestBody);
  delay(2000);
}
