# Código Python para receber dados do Arduino e exibi-los em uma interface web

from flask import Flask, render_template, jsonify
import serial
import time

app = Flask(__name__)

# Configuração da comunicação serial (substitua '/dev/ttyUSB0' e 9600 pelo seu porta e baud rate)
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)  # Espera a conexão estabilizar

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    line = ser.readline().decode('utf-8').strip()
    if line:
        values = line.split()
        if len(values) == 8:
            r = values[1]
            g = values[3]
            b = values[5]
            c = values[7]
            return jsonify({'r': r, 'g': g, 'b': b, 'c': c})
    return jsonify({'error': 'No data'})

if __name__ == '__main__':
    app.run(debug=True)
