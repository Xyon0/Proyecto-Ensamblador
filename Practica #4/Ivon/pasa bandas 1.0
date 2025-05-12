#parte uno del código
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Configuración de estilo para las gráficas
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

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

def crear_grafica(tiempo, original, filtrado, titulo):
    """Crea una gráfica con datos originales y filtrados"""
    plt.figure()
    plt.plot(tiempo, original, 'b-', label='Datos originales', alpha=0.7)
    plt.plot(tiempo, filtrado, 'r-', label='Filtro pasa bandas (0.1-0.3 Hz)', linewidth=1.5)
    plt.title(titulo)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Archivos CSV a leer (cambiar por tus rutas reales)
archivos_csv = ['temperatura.csv', 'humedad.csv', 'viento.csv']

# Frecuencia de muestreo (¡IMPORTANTE! ajusta este valor según tus datos)
fs = 10  # Ejemplo: 10 Hz (muestras por segundo)

# Procesar cada archivo CSV y crear una gráfica individual
for archivo in archivos_csv:
    try:
        tiempo, original, filtrado = cargar_y_procesar_csv(archivo, fs)
        crear_grafica(tiempo, original, filtrado, f'Comparación: {archivo} (fs={fs} Hz)')
    except Exception as e:
        print(f'Error procesando {archivo}: {str(e)}')
