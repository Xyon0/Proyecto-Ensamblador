;Version 1.0.0
JMP Inicio

;Posicion de la pantalla y el stackPoint
stackTop EQU 0xFF	;Ubicacion del stackPoint
textDisplay EQU 0x2E0	;Ubicacion del display

;Variables 
Text: 	DB " Primer version   de assembler"	;Texto a imprimir en el display
		DB 0
       
;Codigo de Inicio
Inicio:
	MOV SP, stackTop		; Funcion del punto de stack
    MOV C, Text		; Funcion para obtener el texto a poner en el display
    MOV D, textDisplay	;Funcion para obtener las cordenadas del display
    CALL print		;Funcion para mandar a impimir al display
    HLT
    
print:
	PUSH A
    PUSH B
    MOV B, 0
Aparicion:
	MOVB AL, [C]
    MOVB [D], AL
    INC C
    INC D
    CMPB BL, [C]
    JNZ Aparicion
    
    POP B
    POP A
    RET

    
