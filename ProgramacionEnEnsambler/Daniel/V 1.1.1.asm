;Version 1.1.1
JMP Inicio	;Funcion para saltar a Inicio

;Posicion de la pantalla y el stackPoint
stackTop EQU 0xFF	;Ubicacion del stackPoint
textDisplay EQU 0x2E0	;Ubicacion del display

;Variables 
Text: 	DB " Primer version   de assembler"	;Texto a imprimir en el display
		DB 0	;Termina la cadena
Contador: 	DB "12345678910" ;Contador del 1 al 10 para que se borre lo que hay en el display
			DB 0	;Termina la cadena
;Codigo de Inicio
Inicio:
	MOV SP, stackTop		; Funcion del punto de stack
    MOV C, Text		; Funcion para obtener el texto a poner en el display
    MOV D, textDisplay	;Funcion para obtener las cordenadas del display
    CALL print		;Funcion para mandar a impimir al display
    JMP Conta
    
print:	
    MOV B, 0	;Sobrescribe el valor B a 0
Aparicion:	;Loop para imprimir la palabra en el display
	MOVB AL, [C]	;Obtiene la letra
    MOVB [D], AL	;Escribe la letra
    INC C	;Incrementa el valor en C
    INC D	;Incrementa el valor en D
    CMPB BL, [C]	;Revisa si el texto es igual a 0
    JNZ Aparicion	;Regresa a Inicio y detiene el loop
    RET
Conta:
	MOV C, Contador	;Obtiene el texto para el contador
    CALL Tiempo	;Llama a Tiempo
    HLT
Tiempo:
	MOV B, 0 ;Sobrescribe el valor B a 0
Contar:
	MOVB AL, [C]	;Obtiene la letra
    INC C	;Incrementa el valor en C
    CMPB BL, [C]	;Revisa si el texto es igual a 0
    JNZ Contar	;Regresa a Inicio y detiene el loop
    
    RET	;Regresa a la funcion CALL