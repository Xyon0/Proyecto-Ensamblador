#parte 4 del código
from scipy.signal import butter, filtfilt

def aplicar_filtro_pasabandas(senal, fs, f_low, f_high, orden=4):
    nyquist = 0.5 * fs
    low = f_low / nyquist
    high = f_high / nyquist
    b, a = butter(orden, [low, high], btype='band')
    return filtfilt(b, a, senal)

# Asumiendo que las muestras se toman cada 5 segundos => fs = 1/5 Hz
fs = 1 / 5  

# Filtro pasa bandas entre 0.01 y 0.08 Hz
temperatura["Filtro_PBAND"] = aplicar_filtro_pasabandas(temperatura["Temperatura_C"], fs, 0.01, 0.08)
humedad["Filtro_PBAND"] = aplicar_filtro_pasabandas(humedad["Humedad_Relativa_%"], fs, 0.01, 0.08)
viento["Filt_Vel_PBAND"] = aplicar_filtro_pasabandas(viento["Velocidad_Viento_mps"], fs, 0.01, 0.08)
viento["Filt_Dir_PBAND"] = aplicar_filtro_pasabandas(viento["Direccion_Viento_deg"], fs, 0.01, 0.08)
plt.figure(figsize=(12, 16))

plt.subplot(4,1,1)
plt.plot(tiempo(temperatura), temperatura["Temperatura_C"], label="Original", **estilo['original'])
plt.plot(tiempo(temperatura), temperatura["Filtro_PBAND"], label="Filtro Pasa Bandas", **estilo['filtro'])
plt.title("Temperatura - Filtro Pasa Bandas")
plt.ylabel("°C")
plt.grid()
plt.legend()

plt.subplot(4,1,2)
plt.plot(tiempo(humedad), humedad["Humedad_Relativa_%"], label="Original", **estilo['original'])
plt.plot(tiempo(humedad), humedad["Filtro_PBAND"], label="Filtro Pasa Bandas", **estilo['filtro'])
plt.title("Humedad - Filtro Pasa Bandas")
plt.ylabel("%")
plt.grid()
plt.legend()

plt.subplot(4,1,3)
plt.plot(tiempo(viento), viento["Velocidad_Viento_mps"], label="Original", **estilo['original'])
plt.plot(tiempo(viento), viento["Filt_Vel_PBAND"], label="Filtro Pasa Bandas", **estilo['filtro'])
plt.title("Velocidad Viento - Filtro Pasa Bandas")
plt.ylabel("m/s")
plt.grid()
plt.legend()

plt.subplot(4,1,4)
plt.plot(tiempo(viento), viento["Direccion_Viento_deg"], label="Original", **estilo['original'])
plt.plot(tiempo(viento), viento["Filt_Dir_PBAND"], label="Filtro Pasa Bandas", **estilo['filtro'])
plt.title("Dirección Viento - Filtro Pasa Bandas")
plt.xlabel("Tiempo (s)")
plt.ylabel("°")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

