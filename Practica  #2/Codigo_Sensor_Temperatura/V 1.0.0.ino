import Adafruit_DHT
import time

# Definir el tipo de sensor y el pin GPIO al que está conectado el sensor
DHT_SENSOR = Adafruit_DHT.DHT11  # Tipo de sensor (DHT11 o DHT22)
DHT_PIN = 7  # Número del pin GPIO (puedes cambiarlo a tu configuración)

while True:
    # Leer la humedad y la temperatura
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    # Comprobar si las lecturas son válidas
    if humidity is not None and temperature is not None:
        # Mostrar los resultados
        print(f'Temperatura: {temperature:.1f}°C, Humedad: {humidity:.1f}%')
    else:
        # Si la lectura falla, mostrar un mensaje de error
        print('Error al leer del sensor')

    # Esperar 2 segundos antes de la siguiente lectura
    time.sleep(2)
