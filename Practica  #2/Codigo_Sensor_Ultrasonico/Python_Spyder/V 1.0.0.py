# -*- coding: utf-8 -*-
#Version 1.0.0
import serial # Importa la biblioteca para la comunicación serial.

# Configura el puerto serial para comunicarse con el Arduino.
# "COM3" es el puerto donde está conectado el Arduino y 9600 es la velocidad de baudios.
arduinoSerialData = serial.Serial("COM3", 9600) 

while True: # Bucle infinito para leer datos continuamente
    if (arduinoSerialData.inWaiting ()> 0):     # Verifica si hay datos disponibles para leer en el puerto serial.
        myData = arduinoSerialData.readline()    #Lee los datos que obtiene del arudino.
        datos = float(myData)    # Convierte los datos del arduino
        print(datos)    # Imprime el valor de datos.
