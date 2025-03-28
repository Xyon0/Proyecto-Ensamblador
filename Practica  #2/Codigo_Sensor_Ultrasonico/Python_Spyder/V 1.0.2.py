# -*- coding: utf-8 -*-
#Version 1.0.2
import serial

arduinoSerialData = serial.Serial("COM3", 9600)

while True:
    if arduinoSerialData.inWaiting() > 0:
        myData = arduinoSerialData.readline().decode('latin1').strip()  # Decodifica y elimina espacios en blanco
        try:
            distance = float(myData.split(':')[1])  # Divide la cadena y toma la parte después de ':'
            print(distance)
        except (ValueError, IndexError) as e:
            print(f"Error al convertir a float: {e}")