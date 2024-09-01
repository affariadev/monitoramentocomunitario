// Código Arduino para leitura de sensores e envio de dados para o servidor Python

#include <Wire.h> // Biblioteca para comunicação I2C
#include <Adafruit_Sensor.h> // Biblioteca para sensores
#include <Adafruit_TCS34725.h> // Biblioteca para sensor de cor (exemplo)

// Configuração do sensor (substitua pelo seu sensor)
Adafruit_TCS34725 tcs = Adafruit_TCS34725();

// Configuração da comunicação serial
const int baudRate = 9600;

void setup() {
  Serial.begin(baudRate); // Inicia a comunicação serial
  if (tcs.begin()) {
    Serial.println("Sensor de cor iniciado com sucesso.");
  } else {
    Serial.println("Não foi possível iniciar o sensor de cor.");
  }
}

void loop() {
  // Leitura dos dados do sensor (exemplo)
  uint16_t r, g, b, c;
  tcs.getRawData(&r, &g, &b, &c);

  // Envio dos dados para o servidor Python
  Serial.print("R: "); Serial.print(r); Serial.print(" ");
  Serial.print("G: "); Serial.print(g); Serial.print(" ");
  Serial.print("B: "); Serial.print(b); Serial.print(" ");
  Serial.print("C: "); Serial.println(c);

  delay(1000); // Espera 1 segundo antes da próxima leitura
}
