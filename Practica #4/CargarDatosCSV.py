#En este trabajo fuimos capaces de desarrollar todo el trabajo al menos todo lo pedido, sin embargo no pudimos desarrollar la transformada de fourier en si
#no pudimos graficarlar, no comprendimos el manejo de los datos obtenidos por la funcion como compararlas con las demas 



# en este apartado agregamos todas las librerias 
import matplotlib.pyplot as plt     
import pandas as pd
import numpy as np
from scipy.signal import filtfilt
from scipy.signal import butter, sosfiltfilt
from scipy import signal
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq



# definimos como se veran las graficas en el archivo 
plt.style.use('seaborn-v0_8')  #adoptamos un estilo de matplotlib  
plt.rcParams['figure.figsize'] = [12, 8] #definimos tamaños
plt.rcParams['font.size'] = 12 #el tamaño de la letra 

def cargar_datos(): #creamos una "funcion" para obtener los datos de los csv
    
    try:
        #le damos a tres valores los datos de los documentos CSV
        df_temp = pd.read_csv('temperatura.csv') 
        df_hum = pd.read_csv('humedad.csv')
        df_wind = pd.read_csv('viento.csv')
        
        #lee archivos por si alguno esta vacio
        if df_temp.empty or df_hum.empty or df_wind.empty:
            raise ValueError("Uno o más archivos están vacíos")
        
        #regresa al programa los datos ya procesados 
        return df_temp, df_hum, df_wind
    #este es otro error aparte de tener vacios los documentos     
    except FileNotFoundError as e:#si hay un error escribe en consola
    #    todo lo siguente se muestra en consola   #
        print(f"Error al cargar archivos: {e}")
        print("Asegúrate de que los archivos estén en el directorio correcto y se llamen:")
        print("- temperatura.csv")
        print("- humedad.csv")
        print("- viento.csv")
        return None, None, None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None, None, None
#se define la "funcion" para el promedio movil
def aplicar_promediado_movil(serie, ventana=3):
    #con ayuda de filfilt calculamos de manera rapida el promedio movil y lo guardamos en kernel 
    kernel = np.ones(ventana) / ventana
    #lo regresamos a donde se a donde se pidio 
    return filtfilt(kernel, 1, serie)
#se definio el filtro pasa bajas con los valores pedidos en el trabajo
def filtro_pasa_bajas_simple(data, cutoff_freq = 0.1 , sample_rate= (1/0.1), order=5):
    # se diseño como un sos
    sos = butter(order, cutoff_freq, btype='low', fs=sample_rate, output='sos')
    # sos se regresa el dato filtrado
    return sosfiltfilt(sos, data)
#se define la funcion de pasa bandas con los valores definidos en el trabajo silicitado 
def aplicar_filtro_pasa_bandas(datos, fs= 1000 , lowcut_hz=0.1, highcut_hz=(1/0.1)):
 #como variable de apoyo se utiliza ny como parte de la libreria que se necesita para el filtro pasa bandas 
    nyquist = 0.5 * fs
    low = lowcut_hz / nyquist
    high = highcut_hz / nyquist
    
#utilizamos parte de la libreria butter para utilizar el filtro pasa bandas esto no los facilito 
    b, a = signal.butter(4, [low, high], btype='band')
    
#se regresa el valor ya filtrado 
    return signal.filtfilt(b, a, datos)
#definimos la funcion para poder calcular la transformada de fourier 
def calculo_FFT(datos):
   
    N=len(datos) #definimos el numero de datos que entran
    
    frec= fftfreq(N, d=1/5)[:N//2] #se define un vector utilizado en el calculo
    
    magnitud= np.abs(fft(datos))[:N//2] #se calcula la magnitud 
    
    return frec, magnitud #se regresa a donde se solicito frecuencia y magnitud

#Como parte de nuestro primer programa se graficaron por separado esta funcion lograba todo eso 
def graficar_comparacion(tiempo, original, filtrado, titulo, ylabel, color):

    plt.figure(figsize=(12, 5))
    plt.plot(tiempo, original, color=color, linestyle='-', alpha=0.5, label='Original')
    plt.plot(tiempo, filtrado, color=color, linestyle='-', linewidth=2, label='Filtrado')
    plt.xlabel('Tiempo (minutos)')
    plt.ylabel(ylabel)
    plt.title(f'{titulo} - Original vs Filtrado')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
 #esta segunda tambien lo hacia, ya que solo procesabamos las funciones sin utlizar plot 
def procesar_y_graficar(df_temp, df_hum, df_wind):
    """Procesa los datos y genera los gráficos comparativos"""
    n_muestras = min(len(df_temp), len(df_hum), len(df_wind))
    tiempo = np.arange(0, n_muestras * 5, 5)
    tiempo_min = tiempo / 60
    
    # Obtener nombres de columnas de los csv
    col_temp = 'valor' if 'valor' in df_temp.columns else df_temp.columns[1]
    col_hum = 'valor' if 'valor' in df_hum.columns else df_hum.columns[1]
    col_wind = 'valor' if 'valor' in df_wind.columns else df_wind.columns[1]
    
    # se extren los datoas como arreglos o series 
    temp_original = df_temp[col_temp].values[:n_muestras]
    hum_original = df_hum[col_hum].values[:n_muestras]
    wind_original = df_wind[col_wind].values[:n_muestras]
    
    #teiendolos en serie es mas facil ocupar todas las funciones ya definidas 
    
    # buscamos el promedio movil en todos las seriees de csv
    temp_filtrado = aplicar_promediado_movil(temp_original)
    hum_filtrado = aplicar_promediado_movil(hum_original)
    wind_filtrado = aplicar_promediado_movil(wind_original)
    
    
    # Aplicar filtro PBajas en todos las seriees de csv
    temp_fpasab = filtro_pasa_bajas_simple(temp_original)
    hum_fpasab = filtro_pasa_bajas_simple(hum_original)
    wind_fpasab = filtro_pasa_bajas_simple(wind_original)
    
    # Aplicar filtro PBandas en todos las seriees de csv
    temp_fpasabs = aplicar_filtro_pasa_bandas(temp_original)
    hum_fpasabs = aplicar_filtro_pasa_bandas(hum_original)
    wind_fpasabs = aplicar_filtro_pasa_bandas(wind_original)
    
    # buscamos Aplicar FFT en todos las seriees de csv
    # para temperatura
    temp_FFTO  = calculo_FFT(temp_original)
    temp_FFTB  = calculo_FFT(temp_fpasab)
    temp_FFTBs = calculo_FFT(temp_fpasabs)
    # para humedad
    
    hum_FFTO = calculo_FFT(hum_original)
    hum_FFTB = calculo_FFT(hum_fpasab)
    hum_FFTBs = calculo_FFT(hum_fpasabs)
    
    # para humedad
    wind_FFTO = aplicar_filtro_pasa_bandas(wind_original)
    wind_FFTB = aplicar_filtro_pasa_bandas(wind_fpasab)
    wind_FFTBs = aplicar_filtro_pasa_bandas(wind_fpasabs)
    
        
    
    
    
    
    
    # Aqui se grafican todas las señales, de todas las variables obtenidas anteriormente para graficarlas en una sola ventam¿na comparandolas
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 10))#se define el grupo de graficas y como se van a dividir en bloques 
    
    ax1.plot(tiempo_min, temp_original, 'b-', alpha=0.5, label='Temperatura (Original)')#se define la primera linea, graficada con el original
    ax1.plot(tiempo_min, temp_filtrado, 'b-', linewidth=2, label='Temperatura (Filtrado)')#se define la segunda linea, graficada el promedio movil
    ax1.plot(tiempo_min, temp_fpasab, 'b--', linewidth=1, label='Temperatura (Filtra B)')#se define la tercera linea, graficada el filtro pasa bandas
    ax1.plot(tiempo_min, temp_fpasabs, 'b:', linewidth=2, label='Temperatura (Filtra Bs)')#se define la cuarta linea, graficada el filtro pasa bajas 
    ax1.set_ylabel('°C')#se define la variable graficada
    ax1.set_title('Comparación de señales originales y filtradas')#aqui se le dio un titulo al conjunto de graficas
    ax1.legend()#termino este apartado de la graficas
    ax1.grid(True)
    #despues se repite lo mismo para todas la variables de las funciones calculadas 
    ax2.plot(tiempo_min, hum_original, 'g-', alpha=0.5, label='Humedad (Original)')
    ax2.plot(tiempo_min, hum_filtrado, 'g-', linewidth=2, label='Humedad (Filtrado)')
    ax2.plot(tiempo_min, hum_fpasab, 'g--', linewidth=1, label='Humedad (Filtra B)')
    ax2.plot(tiempo_min, hum_fpasabs, 'g:', linewidth=2, label='Humedad (Filtra Bs)')
    ax2.set_ylabel('%')
    ax2.legend()
    ax2.grid(True)
    
    ax3.plot(tiempo_min, wind_original, 'r-', alpha=0.5, label='Viento (Original)')
    ax3.plot(tiempo_min, wind_filtrado, 'r-', linewidth=2, label='Viento (Filtrado)')
    ax3.plot(tiempo_min, wind_fpasab, 'r--', linewidth=1, label='Viento (Filtra B)')
    ax3.plot(tiempo_min, wind_fpasabs, 'r:', linewidth=2, label='Viento (Filtra Bs)')
    ax3.set_xlabel('Tiempo (minutos)')
    ax3.set_ylabel('km/h')
    ax3.legend()
    ax3.grid(True)
#se cierra el grupo de graficas
    plt.tight_layout()
    plt.show()
    

# se ejecuta todo el programa es decir la funciones 
if __name__ == "__main__":
    df_temp, df_hum, df_wind = cargar_datos()
    if df_temp is not None and df_hum is not None and df_wind is not None:
        procesar_y_graficar(df_temp, df_hum, df_wind)