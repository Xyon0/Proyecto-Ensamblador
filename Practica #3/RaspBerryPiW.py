import machine
import utime
import os

# Configuración de pines
an1 = machine.ADC(26)
an2 = machine.ADC(27)
an3 = machine.ADC(28)
dg1 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

# Configuración del archivo
filename = 'datos.csv'

# Crear archivo con encabezados (si no existe)
if filename not in os.listdir():
    with open(filename, 'w') as f:
        f.write("Tiempo,Temp,Distancia,Temp2,Presencia")

# Función para leer sensores
def leer_sensores():
    return (
        an1.read_u16(),
        an2.read_u16(),
        an3.read_u16(),
        0 if dg1.value() else 1
    )

try:
    with open(filename, 'a') as f:  # Mantenemos el archivo abierto
        while True:
            timestamp = utime.time()
            a1, a2, a3, d = leer_sensores()

            # Escribir en archivo
            linea = f"{timestamp},{a1},{a2},{a3},{d}\n"
            f.write(linea)
            f.flush()  

            # Mostrar en consola
            print(f"Tiempo     | Temp   Distancia Temp2 | Presencia")
            print(f"{timestamp} | {a1:>5}  {a2:>5}     {a3:>5} | {'ON' if d == 0 else 'OFF'}")
            print(f"_______________________________________________")

            utime.sleep(1)

except KeyboardInterrupt:
    print("\nCaptura detenida por usuario")

except Exception as e:
    print("Error:", e)

finally:
    print("Datos guardados en", filename)
