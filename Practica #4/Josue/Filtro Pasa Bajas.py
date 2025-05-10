import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Cargar los archivos CSV
temperatura = pd.read_csv('temperatura.csv', sep=",", decimal=".")
humedad = pd.read_csv('humedad.csv', sep=",", decimal=".")
viento = pd.read_csv('viento.csv', sep=",", decimal=".")

def tiempo(df):
    return df.index * 5  

temperatura["Promediado_movil"] = temperatura["Temperatura_C"].rolling(3, center=True).mean()
humedad["Promediado_movil"] = humedad["Humedad_Relativa_%"].rolling(3, center=True).mean()
viento["PM_Velocidad"] = viento["Velocidad_Viento_mps"].rolling(3, center=True).mean()
viento["PM_Direccion"] = viento["Direccion_Viento_deg"].rolling(3, center=True).mean()

plt.figure(figsize=(10, 12))

plt.subplot(4,1,1)
plt.plot(tiempo(temperatura), temperatura["Temperatura_C"], color="orange", label="Original")
plt.plot(tiempo(temperatura), temperatura["Promediado_movil"], color="blue", linestyle="--", label="Prom. Móvil (V=3)")
plt.title("Temperatura - Promediado Móvil")
plt.ylabel("Temperatura (°C)")
plt.grid()
plt.legend()

plt.subplot(4,1,2)
plt.plot(tiempo(humedad), humedad["Humedad_Relativa_%"], color="green", label="Original")
plt.plot(tiempo(humedad), humedad["Promediado_movil"], color="red", linestyle="--", label="Prom. Móvil (V=3)")
plt.title("Humedad - Promediado Móvil")
plt.ylabel("Humedad (%)")
plt.grid()
plt.legend()

plt.subplot(4,1,3)
plt.plot(tiempo(viento), viento["Velocidad_Viento_mps"], label="Original")
plt.plot(tiempo(viento), viento["PM_Velocidad"], color="orange", linestyle="--", label="Prom. Móvil (V=3)")
plt.title("Velocidad Viento - Promediado Móvil")
plt.ylabel("Velocidad (m/s)")
plt.grid()
plt.legend()

plt.subplot(4,1,4)
plt.plot(tiempo(viento), viento["Direccion_Viento_deg"], color="grey", label="Original")
plt.plot(tiempo(viento), viento["PM_Direccion"], color="purple", linestyle="--", label="Prom. Móvil (V=3)")
plt.title("Dirección Viento - Promediado Móvil")
plt.ylabel("Dirección (°)")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

def aplicar_filtro(senal, fc=0.1, orden=4):
    b, a = butter(orden, fc, btype='low')
    return filtfilt(b, a, senal)

temperatura["Filtro_PB"] = aplicar_filtro(temperatura["Temperatura_C"])
humedad["Filtro_PB"] = aplicar_filtro(humedad["Humedad_Relativa_%"])
viento["Filt_Velocidad"] = aplicar_filtro(viento["Velocidad_Viento_mps"])
viento["Filt_Direccion"] = aplicar_filtro(viento["Direccion_Viento_deg"])

plt.figure(figsize=(12, 16))

estilo = {
    'original': {'color': 'navy', 'alpha': 0.6, 'linewidth': 1},
    'movil': {'color': 'darkorange', 'linestyle': '--', 'linewidth': 1.5},
    'filtro': {'color': 'crimson', 'linewidth': 2}
}

plt.subplot(4,1,1)
plt.plot(tiempo(temperatura), temperatura["Temperatura_C"], label="Original", **estilo['original'])
plt.plot(tiempo(temperatura), temperatura["Promediado_movil"], label="Prom. Móvil (V=3)", **estilo['movil'])
plt.plot(tiempo(temperatura), temperatura["Filtro_PB"], label="Filtro PB (fc=0.1)", **estilo['filtro'])
plt.title("Comparación: Temperatura")
plt.ylabel("Temperatura (°C)")
plt.grid(alpha=0.3)
plt.legend()

plt.subplot(4,1,2)
plt.plot(tiempo(humedad), humedad["Humedad_Relativa_%"], label="Original", **estilo['original'])
plt.plot(tiempo(humedad), humedad["Promediado_movil"], label="Prom. Móvil (V=3)", **estilo['movil'])
plt.plot(tiempo(humedad), humedad["Filtro_PB"], label="Filtro PB (fc=0.1)", **estilo['filtro'])
plt.title("Comparación: Humedad")
plt.ylabel("Humedad (%)")
plt.grid(alpha=0.3)
plt.legend()

plt.subplot(4,1,3)
plt.plot(tiempo(viento), viento["Velocidad_Viento_mps"], label="Original", **estilo['original'])
plt.plot(tiempo(viento), viento["PM_Velocidad"], label="Prom. Móvil (V=3)", **estilo['movil'])
plt.plot(tiempo(viento), viento["Filt_Velocidad"], label="Filtro PB (fc=0.1)", **estilo['filtro'])
plt.title("Comparación: Velocidad Viento")
plt.ylabel("Velocidad (m/s)")
plt.grid(alpha=0.3)
plt.legend()

plt.subplot(4,1,4)
plt.plot(tiempo(viento), viento["Direccion_Viento_deg"], label="Original", **estilo['original'])
plt.plot(tiempo(viento), viento["PM_Direccion"], label="Prom. Móvil (V=3)", **estilo['movil'])
plt.plot(tiempo(viento), viento["Filt_Direccion"], label="Filtro PB (fc=0.1)", **estilo['filtro'])
plt.title("Comparación: Dirección Viento")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Dirección (°)")
plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
