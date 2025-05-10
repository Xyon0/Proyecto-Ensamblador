#Version 1.1.0
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los archivos CSV
temperatura = pd.read_csv('temperatura.csv', sep= ",", decimal= ".")
humedad = pd.read_csv('humedad.csv', sep= ",", decimal= ".")
viento = pd.read_csv('viento.csv', sep= ",", decimal= ".")

plt.subplot(4,1,1)
plt.plot(temperatura["Tiempo"],temperatura["Temperatura_C"] )
plt.title("Señal original - Temperatura")
plt.ylabel("Temperatura - Centigrados")
plt.grid()

plt.subplot(4,1,2)
plt.plot(humedad["Tiempo"], humedad ["Humedad_Relativa_%"])
plt.title("Señal original - Humedad")
plt.ylabel("Humedad - Relativa")
plt.grid()

plt.subplot(4,1,3)
plt.plot(viento["Tiempo"], viento["Velocidad_Viento_mps"])
plt.title("Señal original - Viento")
plt.ylabel("Velacidad - Mps")
plt.grid()

plt.subplot(4,1,4)
plt.plot(viento["Direccion_Viento_deg"])
plt.title("Señal original - Viento")
plt.ylabel("Dirección - DEG")
plt.grid()

plt.tight_layout()
plt.show()

