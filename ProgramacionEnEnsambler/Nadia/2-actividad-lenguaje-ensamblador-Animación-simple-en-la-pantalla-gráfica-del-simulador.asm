; 2- actividad de animación simple en la pantalla gráfica del simulador
; El punto se moverá de izquierda a derecha en un ciclo continuo.

ORG 0x1000           ; Establece la dirección de inicio del código en modo real (dirección de arranque del programa)

; Establecer el modo gráfico 0x13 (320x200 píxeles, 256 colores)
MOV AH, 0x0E         ; Función 0x0E de la interrupción 0x10 cambia el modo gráfico
MOV AL, 0x13         ; El valor 0x13 corresponde al modo gráfico 320x200 con 256 colores
INT 0x10             ; Llama a la interrupción BIOS para cambiar al modo gráfico

; Dirección de la memoria VGA (memoria de video comienza en 0xA0000 en modo gráfico)
MOV AX, 0xA000       ; Cargar el segmento de memoria VGA (0xA000) en el registro AX
MOV ES, AX           ; Asignar el valor de AX (memoria VGA) al segmento ES, para acceder a la memoria de video

; Inicialización de variables para la animación
MOV CX, 0            ; Inicializa la coordenada X en 0, es la posición del punto en el eje horizontal
MOV DX, 100          ; Inicializa la coordenada Y en 100, coloca el punto en el medio vertical de la pantalla
MOV AL, 0x0F         ; El color del punto es 0x0F, que es blanco en la paleta de 256 colores (0x0F es blanco)

; Comienza el ciclo de animación que moverá el punto
AnimLoop:
    ; Borrar la pantalla (poner todo en negro)
    MOV DI, 0x0000    ; Inicializa DI en 0, apuntando al inicio de la memoria VGA
    MOV SI, 0         ; Inicializa SI como contador de píxeles, cuenta cuántos píxeles hemos procesado

ClearScreen:
    MOV BYTE PTR [ES:DI], 0x00  ; Establece el valor del píxel en negro (0x00)
    INC DI                    ; Avanza a la siguiente dirección de memoria (próximo píxel)
    INC SI                    ; Incrementa el contador de píxeles
    CMP SI, 320*200           ; Compara el contador de píxeles con el número total de píxeles en pantalla (320x200)
    JL ClearScreen            ; Si no hemos procesado todos los píxeles, continúa borrando la pantalla

    ; Dibujar el punto en la nueva posición (CX, DX)
    MOV DI, DX         ; Carga la coordenada Y (almacenada en DX) en DI (dirección de memoria)
    SHL DI, 8          ; Multiplica DX por 256 desplazando 8 bits a la izquierda, esto ajusta la memoria a la fila correcta
    ADD DI, CX         ; Suma la coordenada X (almacenada en CX) a DI, obteniendo la dirección exacta para el píxel
    MOV [ES:DI], AL    ; Establece el valor del píxel en la memoria de video en la dirección ES:DI con el valor de AL (blanco)

    ; Espera pequeña (aproximación de delay para que se vea el movimiento)
    CALL Delay         ; Llama a la subrutina Delay que introduce una pausa antes de continuar

    ; Mover el punto a la derecha en el eje X
    INC CX             ; Incrementa la coordenada X (mueve el punto hacia la derecha)
    CMP CX, 320        ; Compara si la coordenada X ha alcanzado 320 (borde derecho de la pantalla)
    JGE ResetPosition  ; Si la coordenada X es mayor o igual a 320, reinicia la posición del punto

    ; Continuar el ciclo de animación
    JMP AnimLoop       ; Salta al principio del ciclo para seguir moviendo el punto

ResetPosition:
    ; Resetear la posición del punto al inicio de la pantalla
    MOV CX, 0          ; Resetea la coordenada X a 0 (vuelve a la parte izquierda de la pantalla)
    JMP AnimLoop       ; Regresa al ciclo de animación para seguir moviendo el punto

; Subrutina de Delay (aproximación simple de un retraso)
Delay:
    MOV BX, 0xFFFF     ; Establece el valor de BX en 0xFFFF para crear un retraso largo
DelayLoop:
    DEC BX             ; Decrementa el valor de BX
    JNZ DelayLoop      ; Si BX no es cero, regresa a la etiqueta DelayLoop para continuar el retraso
    RET                ; Regresa al punto de llamada de la subrutina

; Fin del programa
MOV AH, 0x0E         ; Función 0x0E de la interrupción 0x10 para cambiar al modo de texto
MOV AL, 0x03         ; Modo de texto 80x25
INT 0x10             ; Llama a la interrupción BIOS para volver al modo de texto

HLT                  ; Detiene la ejecución del programa (Fin de la ejecución)
