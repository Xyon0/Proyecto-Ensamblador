#Version 2.1.1
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los archivos CSV
temperatura = pd.read_csv('temperatura.csv', sep= ",", decimal= ".")
humedad = pd.read_csv('humedad.csv', sep= ",", decimal= ".")
viento = pd.read_csv('viento.csv', sep= ",", decimal= ".")

def tiempo (df):
    return df.index * 5

temperatura["Promediado movil"] = temperatura["Temperatura_C"].rolling(3).mean()
humedad["Promediado movil"] = humedad["Humedad_Relativa_%"].rolling(3).mean()
viento["PM_Velocidad"] = viento["Velocidad_Viento_mps"].rolling(3).mean()
viento["PM_Direccion"] = viento["Direccion_Viento_deg"].rolling(3).mean()

plt.figure(figsize=(10, 12))

plt.subplot(4,1,1)
plt.plot(tiempo(temperatura),temperatura["Temperatura_C"] , color = "orange", label = "Original")
plt.plot(tiempo(temperatura), temperatura["Promediado movil"], color = "blue", linestyle = "--", label = "Promediado")
plt.title("Señal original - Temperatura")
plt.ylabel("Temperatura - °C")
plt.grid()
plt.legend()

plt.subplot(4,1,2)
plt.plot(tiempo(humedad), humedad ["Humedad_Relativa_%"], color = "green", label = "Original")
plt.plot(tiempo(temperatura), humedad["Promediado movil"], color = "red", linestyle = "--", label = "Promediado")
plt.title("Señal original - Humedad")
plt.ylabel("Humedad - %")
plt.grid()
plt.legend()

plt.subplot(4,1,3)
plt.plot(tiempo(viento), viento["Velocidad_Viento_mps"], label = "Original")
plt.plot(tiempo(viento), viento["PM_Velocidad"], color = "orange", linestyle = "--", label = "Promediado")
plt.title("Señal original - Viento")
plt.ylabel("Velacidad - m/s")
plt.grid()
plt.legend()

plt.subplot(4,1,4)
plt.plot(tiempo(viento), viento["Direccion_Viento_deg"], color = "grey", label = "Original")
plt.plot(tiempo(viento), viento["PM_Direccion"], color = "purple", linestyle = "--", label = "Promediado")
plt.title("Señal original - Viento")
plt.ylabel("Dirección - DEG")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
