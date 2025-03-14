#en esta tercera prueba finalice la funcion del delay, en si lo que logre es la escritura en uno de los arreglos que aun tenia disponibles, ademas de que sobreescribi los datos 
#los intercambie por datos vacios, es decir ceros, que no ocupan espacio pero logran borrar las letras que ya estaban en la pantalla



; Example 1.1:
; Writes "Hello World!" to the text display

	JMP boot

stackTop    EQU 0xFF    ; Initial SP
txtDisplay  EQU 0x2E0

hello:	DB "PRIMERTABAJOQUEHAGODEENSAMBLER"	; Output string
		DB 0				; String terminator
        
erahe:  DB "                               ";
		DB 0;

boot:
	MOV SP, stackTop	; Set SP
	MOV C, hello		; Point register C to string
    MOV A, erahe        ;
	MOV D, txtDisplay	; Point register D to output
	CALL print
	HLT				; Halt execution

print:				; Print string
	
	MOV B, 0
.loop:
	MOVB AL, [C]	; Get character
	MOVB [D], AL	; Write to output
	INC C
	INC D
	CMPB BL, [C]	; Check if string terminator
                ;
	JNZ .loop		; Jump back to loop if not
    MOV D, txtDisplay	; 
    MOV C, erahe		; Point register C to string
    MOV B, 1
    CALL pint 
    HLT     
	RET
   
    
pint:

	MOV B,0

.lop:
	MOVB AL, [C] 	;
    MOVB [D], AL    ;
    INC C 
    INC D
    CMPB BL, [C]    ;
    JNZ  .lop       ;
    RET
