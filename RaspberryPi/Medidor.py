import RPi.GPIO as GPIO
import time
import Adafruit_DHT
from RPLCD.gpio import CharLCD
from flask import Flask, jsonify

# Configura el pin GPIO
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 2  # GPIO 2
GPIO.setmode(GPIO.BCM)

# Configura la pantalla LCD
lcd = CharLCD(
    pin_rs=24,  # Pin para RS
    pin_e=23,   # Pin para Enable
    pins_data=[17, 18, 27, 22, 5, 6, 13, 19],  # Pines D0-D7
    numbering_mode=GPIO.BCM  # Usar el modo BCM
)

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    humedad, temperatura = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
    if humedad is not None and temperatura is not None:
        return jsonify({'temperature': temperatura, 'humidity': humedad})
    else:
        return jsonify({'error': 'Error al leer del sensor.'}), 500

def update_lcd(temperatura, humedad):
    lcd.clear()
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f'Temp: {temperatura:.1f}')
    lcd.cursor_pos = (0, 0)
    lcd.write_string(f'Humi: {humedad:.1f}%')

try:
    while True:
        # Lee la temperatura y la humedad
        humedad, temperatura = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humedad is not None and temperatura is not None:
            # Muestra los resultados en la consola
            print(f'Temperatura: {temperatura:.1f}°C, Humedad: {humedad:.1f}%')
            # Muestra los resultados en la LCD
            lcd.clear()
            lcd.cursor_pos=(1,0)
            lcd.write_string(f'Temp: {temperatura:.1f}')
            lcd.cursor_pos=(0,0)
            lcd.write_string(f'Humi: {humedad:.1f}%')
        else:
            print('Error al leer del sensor.')

        time.sleep(2)

except KeyboardInterrupt:
    print("Programa detenido por el usuario.")
finally:
    GPIO.cleanup()  # Limpia la configuración de GPIO
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000) 
