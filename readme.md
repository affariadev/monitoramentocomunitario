Documentação de Instalação do Projeto de Monitoramento de Sensores
Descrição do Projeto
Este projeto utiliza um sistema de monitoramento com um sensor de cor conectado a um Arduino, que envia dados para um servidor Python. O servidor exibe esses dados em uma interface web simples, permitindo o monitoramento em tempo real.

Estrutura do Projeto
Código Arduino: src/Arduino_Sensor_Code.ino - Código para o Arduino que lê dados do sensor e os envia para o servidor.
Código Python: src/server.py - Código Python que recebe dados do Arduino e os exibe em uma interface web.
Página Web: src/templates/index.html - Página HTML para visualizar os dados do sensor.
Requisitos
Hardware:

Arduino (ex: Arduino Uno)
Sensor de cor (ex: TCS34725)
Cabos de conexão
Computador com porta USB para conectar o Arduino
Software:

Arduino IDE
Python 3.x
Pacotes Python: Flask, PySerial
