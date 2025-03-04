
# TEAM Los Nadios
# ESTE CÓDIGO NOS DICE SI EL NUMERO QUE UN USUARIO INGRESA ES ENTERO O ES UN NUMERO IMPAR.
# 2025 / 03/ 03 - V. 1. 0. 0 - SE AGREGAN COMENTARIOS Y ECANBEZADO AL CÓDIGO
# TRABAJARON: NADIA / EDUARDO 
# Solicita al usuario ingresar un número y lo convierte en entero 
numero = int(input("Ingrese un número: "))  # La función 'int()' convierte la cadena de texto en un número entero.

# Verifica si el número es divisible entre 2 sin dejar residuo
if numero % 2 == 0: # Si el residuo de la división de 'numero' entre 2 es igual a 0, es un número par
    # Si el número es divisible por 2, es par
    print("El número es par") # La función print() muestra un mensaje en la pantalla en este caso "el numero es par 
else:
    # Si el número no es divisible por 2, es impar
    # Si la condición del 'if' no se cumple (es decir, el número no es divisible por 2), se ejecuta este bloque de código.
    print("El número es impar")
