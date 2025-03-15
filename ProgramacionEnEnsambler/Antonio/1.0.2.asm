#en esta tercera prueba finalice la funcion del delay, en si lo que logre es la escritura en uno de los arreglos que aun tenia disponibles, ademas de que sobreescribi los datos 
#los intercambie por datos vacios, es decir ceros, que no ocupan espacio pero logran borrar las letras que ya estaban en la pantalla



; Example 1.1:
; Writes "Hello World!" to the text display

	JMP boot

stackTop    EQU 0xFF    ; le da a stacktop el valor de 0xFF que corresponde a una direcccion de la memoria 
txtDisplay  EQU 0x2E0	; a txtDisplay se le da el valor de 0x2E0 que es donde empieza el espacio de la memoria que corresponde a la pantalla de texto

hello:	DB "PRIMERTABAJOQUEHAGODEENSAMBLER"	; se le da a el arreglo hello los caracteres necesario para cubrir completamente la pantalla de texto
		DB 0				; se define el valor de 0 para acabar el arreglo 
        
erahe:  DB "                               "; se le da a erahe los suficientes espacios en blanco como para borrar todo el arreglo hello 
		DB 0; se finaliza el arreglo para no tener errores a futuro 

boot:
	MOV SP, stackTop	; se mueve el puntero a la pusicion que tenga stacktop
	MOV C, hello		;se le da a el arreglo C los caracteres del arreglo hello
        MOV A, erahe            ; se le da a A los caracteeres del arreglo erahe 
	MOV D, txtDisplay	; se le da a D el valor de txtDisplay 
	CALL print		; se manda a llamar la subrutina print 
	HLT			; se finaliza la subrutina

print:				; empieza la subrutina print 
	
	MOV B, 0                ; se le da a al arreglo el valor de 0
.loop:
	MOVB AL, [C]	;se le da a AL el caracterer que en la posicion de C este definada
	MOVB [D], AL	; se le escribe en la posicion que D marque el valor que AL tiene 
	INC C           ; C aumenta en uno
	INC D		; D aumenta en uno 
	CMPB BL, [C]	; se compara el valor de C si es el cero definido termina si no  sigue 
                ;
	JNZ .loop		; si se cumple lo anterior finaliza la subrutina
    MOV D, txtDisplay		; se le vuelve a dar a D el valor dde txtDisplay 
    MOV C, erahe		; se le dan a C los caracteres que en erahe hay 
    MOV B, 1			; B cambia a 1
    CALL pint 			; se llama a la subrutina pint 
    HLT     			; fin de la subrutina
	RET
   
    
pint:

	MOV B,0		; se deja a B en 0 

.lop:
    MOVB AL, [C] 	; se toma de la posicion del arreglo de C para darle ese caracter a AL
    MOVB [D], AL        ; en la posicion de D se escribe el valor de AL que es en 8 bits 
    INC C 		; se aumenta en uno el valor de C
    INC D		; se aumenta en unoo el  valor de D
    CMPB BL, [C]        ; se compara el  valor que en C halla si es igual a cero se termina la subrutina si no continua  
    JNZ  .lop           ; si no se cumple la anterior funcion se regresa a lop 
    RET
