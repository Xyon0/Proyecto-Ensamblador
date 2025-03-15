;Primera actividad de lenguaje ensamblador
JMP Inicio              ; Salta directamente al inicio del código, ignorando el resto antes de la etiqueta 'Inicio'

; Posición de la pantalla y el stackPoint
stackTop EQU 0xFF        ; Define la ubicación en la memoria donde se almacenará la pila (Stack Pointer).
textDisplay EQU 0x2E0    ; Dirección de memoria donde se encuentra la pantalla (el lugar donde se imprimirá el texto).

; Variables
Text:   DB " Primera actividad Nadia "  ; El texto que será mostrado en el display
        DB 0            ; El texto termina con un valor nulo (0) que indica el final de la cadena.

Inicio: ; Esta es la etiqueta que marca el inicio del programa.
    MOV SP, stackTop       ; Establece el puntero de la pila (Stack Pointer) en la dirección definida por 'stackTop'.
    MOV C, Text            ; Carga la dirección de inicio del texto ('Text') en el registro C. Esto nos permite acceder a los caracteres de la cadena.
    MOV D, textDisplay     ; Carga la dirección de inicio del display ('textDisplay') en el registro D. Esto define dónde se escribirán los caracteres en el display.
    CALL print             ; Llama a la subrutina 'print' para imprimir el texto en el display.
    HLT                    ; Detiene la ejecución del programa después de que se haya mostrado el texto.

; Subrutina 'print' para imprimir el texto
print:
    PUSH A                 ; Guarda el contenido del registro A en la pila (Stack), para que pueda recuperarse más tarde.
    PUSH B                 ; Guarda el contenido del registro B en la pila, encima de A.
    MOV B, 0               ; Inicializa el registro B a 0. Usaremos B para controlar el loop de impresión.

Aparicion:   ; Comienza el loop para imprimir cada carácter de la cadena.
    MOVB AL, [C]          ; Carga el valor de la dirección que apunta C (el siguiente carácter del texto) en el registro AL.
    MOVB [D], AL          ; Escribe el valor de AL (el carácter) en la dirección que apunta D (en el display).
    INC C                 ; Incrementa la dirección de C, avanzando al siguiente carácter en la cadena de texto.
    INC D                 ; Incrementa la dirección de D, avanzando al siguiente espacio en el display.
    CMPB BL, [C]          ; Compara el valor en BL (que tiene el valor 0) con el siguiente carácter en la cadena.
    JNZ Aparicion         ; Si el carácter no es 0 (fin de la cadena), regresa a 'Aparicion' para imprimir el siguiente carácter.

    ; Si se llega aquí, significa que la cadena ha terminado.
    POP B            

