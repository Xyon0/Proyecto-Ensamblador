# -*- coding: utf-8 -*-
#Version 1.0.0
import serial 
arduinoSerialData = serial.Serial("COM3", 9600) 
while True:
    if (arduinoSerialData.inWaiting ()> 0): 
        myData = arduinoSerialData.readline() 
        datos = float(myData) 
        print(datos)