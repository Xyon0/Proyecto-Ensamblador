#team losnadios
# Este código imprime los elemetos de la variable "frutas" (manzana, platano y naranja) agregando tambien el metodo .append (pera) al final haciendo lista primero, para despues imprimir otra vez los elementos pero esta vez en una lista vertical haciendo referencia que frutas tiene en ese momento.
# 2025 / 03/ 03 - V. 1. 0. 0 - SE  AGREGO EL ECANBEZADO AL CÓDIGO E INFORMACIÓN DEL EQUIPO   
# 2025 / 03/ 03 - V. 1. 0. 2 - SE AGREGARON COMENTARIOS LA VARIABLE "frutas" Y EN LOS COMANDOS PRINT
# 2025 / 03/ 03 - V. 1. 0. 3 - SE AGREGAN COMENTARIO EN LA LINEA 9, EXPLICANDO EL FUNCIONAMIENTO DEL .append
# 2025 / 03/ 03 - V. 1. 0. 4 - SE AGREGO COMENTARIO EN LA LINEA 18 EXPLICANDO EL FUNCIONAMENTO DE FOR
# TRABAJARON: Daniel Alberto y Josué

frutas = ["manzana", "plátano", "naranja"] #Se crea una variable llamada "frutas" en la cual contiene elementos que referencian 3 frutas que se utilizaran en el codigo.


frutas.append("pera") #Se usa la variable llamada "frutas", junto con el metodo .append con la palabra pera, siendo esta utilizado para agregar dicha palabra al final de la lista de frutas.


print("Lista de frutas:", frutas) #Se llama a imprimir una palanbra siendo "Lista de frutas" para despues usar las variables de "frutas" y finalizando con el elemento del metodo .append.


for fruta in frutas: #Se crea un bucle llamado "fruta" el cual usa los elementos de la variable "frutas" mientras va aumenta de 1 en 1 su valor, asi usando el elemento "manzana" despues "plátano" y asi sucesivamente
    print("Tengo una", fruta) #Se llama a imprimir la palabar "Tengo una" junto con el primer elemento de la variable "frutas" sucesivamente hasta que acaba la lista con el elemeneto del metodo .append
