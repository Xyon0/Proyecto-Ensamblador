# -*- coding: latin1 -*-
#Version 1.0.2
import serial  # Importa la biblioteca para la comunicación serial

# Configura el puerto serial para comunicarse con el Arduino
# "COM3" es el puerto donde está conectado el Arduino y 9600 es la velocidad de baudios
arduinoSerialData = serial.Serial("COM3", 9600) 

while True:    # Bucle infinito para leer datos continuamente
    if arduinoSerialData.inWaiting() > 0:    # Verifica si hay datos disponibles para leer en el puerto serial
        myData = arduinoSerialData.readline().decode('latin1').strip()  # Decodifica y elimina espacios en blanco
        try:
            distance = float(myData.split(':')[1])  # Divide la cadena y toma la parte después de ':'
            print(distance)    # Imprime el valor de distancia
        except (ValueError, IndexError) as e:    # Captura errores de conversión o de índice
            print(f"Error al convertir a float: {e}")    # Imprime el error si ocurre un problema
