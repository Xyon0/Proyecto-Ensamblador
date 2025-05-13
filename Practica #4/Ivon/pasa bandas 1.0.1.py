#código del filtro pasa bandas parte final
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Configuración de estilo para las gráficas
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 8)

def aplicar_filtro_pasa_bandas(datos, fs, lowcut_hz=0.1, highcut_hz=0.3):
    """Aplica un filtro pasa bandas con frecuencias en Hz"""
    nyquist = 0.5 * fs
    low = lowcut_hz / nyquist
    high = highcut_hz / nyquist
    b, a = signal.butter(4, [low, high], btype='band')
    return signal.filtfilt(b, a, datos)

def cargar_y_procesar_csv(archivo_csv, fs):
    """Carga un archivo CSV y devuelve los datos originales y filtrados"""
    df = pd.read_csv(archivo_csv)
    tiempo = df.iloc[:, 0].values
    datos_originales = df.iloc[:, 1].values
    
    # Aplicar filtro pasa bandas
    datos_filtrados = aplicar_filtro_pasa_bandas(datos_originales, fs=fs)
    
    return tiempo, datos_originales, datos_filtrados

# Archivos CSV a leer (cambiar por tus rutas reales)
archivos_csv = ['humedad.csv', 'temperatura.csv', 'viento.csv']

# Frecuencia de muestreo 
fs = 10  # Ejemplo: 10 Hz (muestras por segundo)

# Crear una sola figura
plt.figure()

# Colores diferenciados para cada archivo
colores = ['b', 'g', 'r', 'c', 'm', 'y']

# Procesar cada archivo CSV y agregar a la gráfica
for i, archivo in enumerate(archivos_csv):
    try:
        tiempo, original, filtrado = cargar_y_procesar_csv(archivo, fs)
        
        # Graficar datos originales (línea continua)
        plt.plot(tiempo, original, 
                color=colores[i%len(colores)], 
                linestyle='-', 
                alpha=0.5, 
                label=f'{archivo} - Original')
        
        # Graficar datos filtrados (línea discontinua)
        plt.plot(tiempo, filtrado, 
                color=colores[i%len(colores)], 
                linestyle='--', 
                linewidth=1.5, 
                label=f'{archivo} - Filtrado (0.1-0.3 Hz)')
        
    except Exception as e:
        print(f'Error procesando {archivo}: {str(e)}')

# Configuración de la gráfica
plt.title(f'Comparación de datos originales y filtrados (fs={fs} Hz)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  # Leyenda fuera del gráfico
plt.grid(True)
plt.tight_layout()

plt.show()
