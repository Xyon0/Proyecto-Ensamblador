#Version 2.1.2
# Importación de bibliotecas necesarias.
import pandas as pd  # Para manejo de datos y DataFrames.
import matplotlib.pyplot as plt  # Para visualización gráfica.

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

# --------------------- CONFIGURACIÓN DE GRÁFICOS ---------------------
# Crear una figura con 4 subgráficos en disposición vertical (4 filas, 1 columna)
plt.figure(figsize=(10, 12)) # Tamaño opcional para mejor visualización.

# Primer subgráfico: Temperatura
plt.subplot(4,1,1)    # (filas, columnas, posición)
plt.plot(tiempo(temperatura),temperatura["Temperatura_C"] , color = "orange", label = "Original")    #  (x, y), ademas de el color y la leyenda de la grafica.
plt.plot(tiempo(temperatura), temperatura["Promediado movil"], color = "blue", linestyle = "--", label = "Promediado")    #  (x, y), ademas de el color, la leyenda de la grafica y un estilo para diferenciar los datos.
plt.title("Señal - Temperatura")    # Titulo de la grafica
plt.ylabel("Temperatura - °C")    #  Nombre de la grafica Y
plt.grid()    #  Rejilla en la grafica para no mostrar un fondo blanco.
plt.legend()    #    Mostrar la leyenda de cada grafica.

plt.subplot(4,1,2)    # (filas, columnas, posición)
plt.plot(tiempo(humedad), humedad ["Humedad_Relativa_%"], color = "green", label = "Original")    #  (x, y), ademas de el color y la leyenda de la grafica.
plt.plot(tiempo(temperatura), humedad["Promediado movil"], color = "red", linestyle = "--", label = "Promediado")    #  (x, y), ademas de el color, la leyenda de la grafica y un estilo para diferenciar los datos.

plt.title("Señal - Humedad")    # Titulo de la grafica
plt.ylabel("Humedad - %")    #  Nombre de la grafica Y
plt.grid()    #  Rejilla en la grafica para no mostrar un fondo blanco.
plt.legend()    #    Mostrar la leyenda de cada grafica.

plt.subplot(4,1,3)    # (filas, columnas, posición)
plt.plot(tiempo(viento), viento["Velocidad_Viento_mps"], label = "Original")        #  (x, y), ademas de la leyenda de la grafica.
plt.plot(tiempo(viento), viento["PM_Velocidad"], color = "orange", linestyle = "--", label = "Promediado")    #  (x, y), ademas de el color, la leyenda de la grafica y un estilo para diferenciar los datos.

plt.title("Señal - Viento")    # Titulo de la grafica
plt.ylabel("Velacidad - m/s")    #  Nombre de la grafica Y
plt.grid()    #  Rejilla en la grafica para no mostrar un fondo blanco.
plt.legend()    #    Mostrar la leyenda de cada grafica.

plt.subplot(4,1,4)    # (filas, columnas, posición)
plt.plot(tiempo(viento), viento["Direccion_Viento_deg"], color = "grey", label = "Original")    #  (x, y), ademas de el color y la leyenda de la grafica.
plt.plot(tiempo(viento), viento["PM_Direccion"], color = "purple", linestyle = "--", label = "Promediado")    #  (x, y), ademas de el color, la leyenda de la grafica y un estilo para diferenciar los datos.

plt.title("Señal - Viento/Dirección")    # Titulo de la grafica
plt.ylabel("Dirección - DEG")    #  Nombre de la grafica Y
plt.grid()    #  Rejilla en la grafica para no mostrar un fondo blanco.
plt.legend()    #    Mostrar la leyenda de cada grafica.

# Ajustar espaciado entre subgráficos para evitar superposiciones
plt.tight_layout()

# Mostrar la figura con todos los subgráficos
plt.show()
