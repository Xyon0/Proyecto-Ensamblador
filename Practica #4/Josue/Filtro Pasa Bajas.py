# Importación de bibliotecas necesarias.
import pandas as pd  # Para manejo de datos y DataFrames.
import matplotlib.pyplot as plt  # Para visualización gráfica.
from scipy.signal import butter, filtfilt

# --------------------- CARGA DE DATOS ---------------------
# Cargar los archivos CSV usando pandas.
# Se especifica separador decimal como punto y delimitador de columnas como coma.
temperatura = pd.read_csv('temperatura.csv', sep= ",", decimal= ".")
humedad = pd.read_csv('humedad.csv', sep= ",", decimal= ".")
viento = pd.read_csv('viento.csv', sep= ",", decimal= ".")

def tiempo (df):    # Calcula el tiempo transcurrido basado en el índice del DataFrame.
    return df.index * 5    # Multiplica cada valor del índice por 5 para obtener el tiempo.

# Calcula el promedio móvil de 3 puntos para la temperatura
# rolling(3): Usa una ventana de 3 periodos (valores consecutivos)
# mean(): Calcula el promedio dentro de la ventana
temperatura["Promediado movil"] = temperatura["Temperatura_C"].rolling(3).mean()

# Aplica el mismo promedio móvil a la humedad relativa
humedad["Promediado movil"] = humedad["Humedad_Relativa_%"].rolling(3).mean()

# Calcula promedio móvil para velocidad del viento (nueva columna PM_Velocidad)
viento["PM_Velocidad"] = viento["Velocidad_Viento_mps"].rolling(3).mean()

# Calcula promedio móvil para dirección del viento (nueva columna PM_Direccion)
viento["PM_Direccion"] = viento["Direccion_Viento_deg"].rolling(3).mean()

def aplicar_filtro(senal, fc=0.1, orden=4):
    b, a = butter(orden, fc, btype='low')
    return filtfilt(b, a, senal)

temperatura["Filtro_PB"] = aplicar_filtro(temperatura["Temperatura_C"])
humedad["Filtro_PB"] = aplicar_filtro(humedad["Humedad_Relativa_%"])
viento["Filt_Velocidad"] = aplicar_filtro(viento["Velocidad_Viento_mps"])
viento["Filt_Direccion"] = aplicar_filtro(viento["Direccion_Viento_deg"])

# --------------------- CONFIGURACIÓN DE GRÁFICOS ---------------------
# Crear una figura con 4 subgráficos en disposición vertical (4 filas, 1 columna)
plt.figure(figsize=(12, 16))    # Tamaño opcional para mejor visualización.

estilo = {
    'original': {'color': 'navy', 'alpha': 0.6, 'linewidth': 1},
    'movil': {'color': 'darkorange', 'linestyle': '--', 'linewidth': 1.5},
    'filtro': {'color': 'crimson', 'linewidth': 2}
}

# Primer subgráfico: Temperatura
plt.subplot(4,1,1)    # (filas, columnas, posición)
plt.plot(tiempo(temperatura), temperatura["Temperatura_C"], label="Original", **estilo['original'])
plt.plot(tiempo(temperatura), temperatura["Promediado_movil"], label="Prom. Móvil (V=3)", **estilo['movil'])
plt.plot(tiempo(temperatura), temperatura["Filtro_PB"], label="Filtro PB (fc=0.1)", **estilo['filtro'])
plt.title("Comparación: Temperatura")    # Titulo de la grafica
plt.ylabel("Temperatura (°C)")     #  Nombre de la grafica Y
plt.grid(alpha=0.3)    #  Rejilla en la grafica para no mostrar un fondo blanco.
plt.legend()    #    Mostrar la leyenda de cada grafica.

# Primer subgráfico: Humedad
plt.subplot(4,1,2)    # (filas, columnas, posición)
plt.plot(tiempo(humedad), humedad["Humedad_Relativa_%"], label="Original", **estilo['original'])
plt.plot(tiempo(humedad), humedad["Promediado_movil"], label="Prom. Móvil (V=3)", **estilo['movil'])
plt.plot(tiempo(humedad), humedad["Filtro_PB"], label="Filtro PB (fc=0.1)", **estilo['filtro'])
plt.title("Comparación: Humedad")    # Titulo de la grafica
plt.ylabel("Humedad (%)")     #  Nombre de la grafica Y
plt.grid(alpha=0.3)    #  Rejilla en la grafica para no mostrar un fondo blanco.
plt.legend()    #    Mostrar la leyenda de cada grafica.

# Primer subgráfico: Viento (Velocidad)
plt.subplot(4,1,3)    # (filas, columnas, posición)
plt.plot(tiempo(viento), viento["Velocidad_Viento_mps"], label="Original", **estilo['original'])
plt.plot(tiempo(viento), viento["PM_Velocidad"], label="Prom. Móvil (V=3)", **estilo['movil'])
plt.plot(tiempo(viento), viento["Filt_Velocidad"], label="Filtro PB (fc=0.1)", **estilo['filtro'])
plt.title("Comparación: Velocidad Viento")    # Titulo de la grafica
plt.ylabel("Velocidad (m/s)")     #  Nombre de la grafica Y
plt.grid(alpha=0.3)    #  Rejilla en la grafica para no mostrar un fondo blanco.
plt.legend()    #    Mostrar la leyenda de cada grafica.

# Primer subgráfico: Viento (Dirección)
plt.subplot(4,1,4)    # (filas, columnas, posición)
plt.plot(tiempo(viento), viento["Direccion_Viento_deg"], label="Original", **estilo['original'])
plt.plot(tiempo(viento), viento["PM_Direccion"], label="Prom. Móvil (V=3)", **estilo['movil'])
plt.plot(tiempo(viento), viento["Filt_Direccion"], label="Filtro PB (fc=0.1)", **estilo['filtro'])
plt.title("Comparación: Dirección Viento")    # Titulo de la grafica
plt.xlabel("Tiempo (segundos)")    #  Nombre de la grafica en x
plt.ylabel("Dirección (°)")     #  Nombre de la grafica Y
plt.grid(alpha=0.3)    #  Rejilla en la grafica para no mostrar un fondo blanco.
plt.legend()    #    Mostrar la leyenda de cada grafica.

# Ajustar espaciado entre subgráficos para evitar superposiciones
plt.tight_layout()

# Mostrar la figura con todos los subgráficos
plt.show()
