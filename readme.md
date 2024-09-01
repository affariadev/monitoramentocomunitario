Diagrama da Arquitetura da Aplicação

      +----------------+         +-----------------+
      |                |         |                 |
      |     Sensor     |         |    Arduino      |
      |     (TCS34725) |         |   (Código)      |
      |                |         |                 |
      +--------+-------+         +--------+--------+
               |                         |
               | (1) Dados do Sensor      | (2) Envia Dados via Serial
               |                         |
               V                         V
      +----------------+         +-----------------+
      |                |         |                 |
      |  Porta Serial  |         |   Servidor      |
      |                |         |     Python       |
      |                |         |  (Código Python) |
      +--------+-------+         +--------+--------+
               |                         |
               | (3) Recebe Dados via Serial
               |                         |
               V                         V
      +----------------+         +-----------------+
      |                |         |                 |
      |  Comunicação   |         |    Flask        |
      |   Serial       |         |    Web Server   |
      |                |         |                 |
      +--------+-------+         +--------+--------+
               |                         |
               | (4) Exibe Dados via API  |
               |                         |
               V                         V
      +----------------+         +-----------------+
      |                |         |                 |
      |    Interface   |         |     Navegador    |
      |      Web        |         |     (Frontend)   |
      |                |         |                 |
      +----------------+         +-----------------+

