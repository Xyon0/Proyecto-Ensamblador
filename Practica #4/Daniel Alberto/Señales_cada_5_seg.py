#Version 2.0.1
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

# --------------------- CONFIGURACIÓN DE GRÁFICOS ---------------------
# Crear una figura con 4 subgráficos en disposición vertical (4 filas, 1 columna)
plt.figure(figsize=(10, 8))    # Tamaño opcional para mejor visualización.

# Primer subgráfico: Temperatura
plt.subplot(4, 1, 1)  # (filas, columnas, posición)
plt.plot(temperatura["Tiempo"],temperatura["Temperatura_C"] )  #  (x, y)
plt.title("Señal original - Temperatura")  # Titulo de la grafica
plt.ylabel("Temperatura - Centigrados")  #  Nombre de la grafica Y
plt.grid()  #  Rejilla en la grafica para no mostrar un fondo blanco.

# Segundo subgráfico: Humedad
plt.subplot(4,1,2)
plt.plot(humedad["Tiempo"], humedad ["Humedad_Relativa_%"])  #  (x, y)
plt.title("Señal original - Humedad")  # Titulo de la grafica
plt.ylabel("Humedad - Relativa")  #  Nombre de la grafica Y
plt.grid()  #  Rejilla en la grafica para no mostrar un fondo blanco.

# Tercer subgráfico: Velocidad del viento
plt.subplot(4,1,3)  # (filas, columnas, posición)
plt.plot(viento["Tiempo"], viento["Velocidad_Viento_mps"])  #  (x, y)
plt.title("Señal original - Viento")  # Titulo de la grafica
plt.ylabel("Velacidad - Mps")  #  Nombre de la grafica Y
plt.grid()  #  Rejilla en la grafica para no mostrar un fondo blanco.

# Cuarto subgráfico: Dirección del viento
plt.subplot(4,1,4)
plt.plot(viento["Direccion_Viento_deg"])  #  (x, y)
plt.title("Señal original - Viento")  # Titulo de la grafica
plt.ylabel("Dirección - DEG")  #  Nombre de la grafica Y
plt.grid()  #  Rejilla en la grafica para no mostrar un fondo blanco.

# Ajustar espaciado entre subgráficos para evitar superposiciones
plt.tight_layout()

# Mostrar la figura con todos los subgráficos
plt.show()
