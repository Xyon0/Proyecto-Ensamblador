;Version 1.1
JMP Main            ;Salta al punto de entrada principal


stackPointer EQU 0xFF        
displayText EQU 0x2E0        
displayGraphic EQU 0x310     



WelcomeMsg:    DB " programa de    prueba "    ;Mensaje inicial
               DB 0                                     ;Terminador de cadena
            
ClearLine:     DB "                                "    ;Espacios para borrar texto
               DB 0                                     ;Terminador de cadena


Nave:
    DB "\xFF\xFF\xFF\xFF\xFF\xFF\x22\x22"
    DB "\x22\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
    DB "\xFF\xFF\xFF\xFF\xFF\x22\x22\x22"
    DB "\x22\x22\xFF\xFF\xFF\xFF\xFF\xFF"
    DB "\xFF\xFF\xFF\xFF\x22\x44\x44\x44"
    DB "\x44\x44\x22\xFF\xFF\xFF\xFF\xFF"
    DB "\xFF\xFF\xFF\x22\x44\x22\x44\x44"
    DB "\x44\x22\x44\x22\xFF\xFF\xFF\xFF"
    DB "\xFF\xFF\x22\x44\x44\x44\x44\x44"
    DB "\x44\x44\x44\x44\x22\xFF\xFF\xFF"
    DB "\xFF\xFF\x22\x44\x44\x44\x44\x44"
    DB "\x44\x44\x44\x44\x22\xFF\xFF\xFF"
    DB "\xFF\x22\x44\x44\x44\x44\x44\x44"
    DB "\x44\x44\x44\x44\x44\x22\xFF\xFF"
    DB "\xFF\x22\x44\x44\x33\x33\x33\x33"
    DB "\x33\x33\x33\x44\x44\x22\xFF\xFF"
    DB "\x22\x44\x44\x44\x33\x33\x33\x33"
    DB "\x33\x33\x33\x44\x44\x44\x22\xFF"
    DB "\x22\x44\x44\x33\x33\x11\x11\x11"
    DB "\x11\x11\x33\x33\x44\x44\x22\xFF"
    DB "\x22\x44\x44\x33\x33\x11\x11\x11"
    DB "\x11\x11\x33\x33\x44\x44\x22\xFF"
    DB "\x22\x44\x44\x44\x33\x33\x33\x33"
    DB "\x33\x33\x33\x44\x44\x44\x22\xFF"
    DB "\xFF\x22\x44\x44\x44\x44\x44\x44"
    DB "\x44\x44\x44\x44\x44\x22\xFF\xFF"
    DB "\xFF\x22\x44\x44\x44\x44\x44\x44"
    DB "\x44\x44\x44\x44\x22\x22\xFF\xFF"
    DB "\xFF\xFF\x22\x22\x22\x22\x22\x22"
    DB "\x22\x22\x22\x22\x22\xFF\xFF\xFF"
    DB "\xFF\xFF\xFF\xFF\xFF\x22\x22\x22"
    DB "\x22\x22\xFF\xFF\xFF\xFF\xFF\xFF"


Main:
    MOV SP, stackPointer        
    CALL DisplayWelcome         ;Muestra mensaje de bienvenida
    CALL ClearDisplay           ;Limpia el display
    CALL DisplayGraphics        ;Muestra gráficos
    HLT                         ;Detiene el simulador


DisplayWelcome:
    MOV C, WelcomeMsg           
    MOV D, displayText          ;Dirección del display
    CALL PrintText              ;Imprime el texto
    RET


PrintText:
    MOV B, 0                    
PrintLoop:
    MOVB AL, [C]                
    CMPB AL, 0                  ;Comprueba si es fin de cadena
    JZ PrintEnd                 ;Si es cero, termina
    MOVB [D], AL                ;Escribe caracter en display
    INC C                       ;Siguiente caracter
    INC D                       ;Siguiente posición en display
    JMP PrintLoop               ;Continúa bucle
PrintEnd:
    RET                         ;Retorna


ClearDisplay:
    MOV C, ClearLine            
    MOV D, displayText          ;Dirección del display
    CALL PrintText              ;Imprime espacios
    RET


DisplayGraphics:
    MOV C, Nave            ;Dirección del sprite
    MOV D, displayGraphic       ;Dirección del display gráfico
    MOV B, 0                    ;Inicializa contador
GraphicsLoop:
    MOVB AL, [C]                
    MOVB [D], AL                
    INC C                       ;Siguiente byte de gráfico
    INC D                       ;Siguiente posición en display
    INC B                       ;Incrementa contador
    CMP B, 448                  ;Comprueba si terminó (16*28 bytes)
    JNZ GraphicsLoop            ;Continúa si no ha terminado
    RET                         ;Retorn
