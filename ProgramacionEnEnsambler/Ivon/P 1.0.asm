#esta en al primera prueba de un código que tomaré como ejemplo de como usar algunas variables
#el código muestra en la pantalla la frase más común en los ejemplos: Hello word

    JMP start          ; Salta a la etiqueta 'start'

Hello: 
    DB "Hello World"   ; Definición de la cadena
    DB 0               ; Terminador de cadena

start:
    MOV C, Hello       ; Apunta a la variable 'Hello'
    MOV D, 232         ; Apunta a la salida (puerto de salida)
    CALL print         ; Llama a la rutina de impresión
    HLT                 ; Detiene la ejecución

print:
    PUSH A             ; Guarda el registro A
    PUSH B             ; Guarda el registro B

.loop:
    MOV A, [C]        ; Carga el carácter actual en A
    CMP A, 0          ; Compara A con 0 (fin de cadena)
    JE .end           ; Si es 0, salta a .end
    MOV [D], A        ; Escribe en la salida
    INC C             ; Incrementa el puntero de la cadena
    INC D             ; Incrementa el puntero de salida
    JMP .loop         ; Vuelve al inicio del bucle

.end:
    POP B             ; Restaura el registro B
    POP A             ; Restaura el registro A
    RET                ; Retorna de la subrutina
