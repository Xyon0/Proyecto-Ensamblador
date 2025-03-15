#en esta segunda actualizacion logre hacer la funcion sin embargo no se borraban bien ademas de que aparecian cosas extrañas en la pantalla






; Example 1.1:
; Writes "Hello World!" to the text display

	JMP boot

stackTop    EQU 0xFF    ; le da a stacktop el valor que es la puntuacion del puntero
txtDisplay  EQU 0x2E0   ; le da a txtDisplay el valor de donde empieza en el espacio en la memoria de la pantalla 

hello:	DB "PRIMERTABAJOQUEHAGODEENSAMBLER"	; se le dio al arreglo hello los valores dentro de las comillas
		DB 0				; se definio un cero para marcar el fin del arreglo
        
erahe:  DB "                              "; se le dio al arreglo erahe el mismo numero de caracteres pero en espacios para que sean espacios en blanco 
		DB 0; 			     se definio un cero para marcar el fin del arreglo

boot:
	MOV SP, stackTop	; se le dio al puntero el valor que stackTop guarda
	MOV C, hello		; se le dio al arreglo los caracteres que hello tiene
    	MOV A, erahe        ; se le dio a A los caracteres del arreglo erahe
	MOV D, txtDisplay	; se le dio a D el valor de txtDisplay funcionando como un puntero 
	CALL print , llama a la funcion definida como print a que se ejecute 
	HLT				; se detiene la ejecucion de la subrutin 

print:				; comienza la subrutina print
	
	MOV B, 0 ; regresa a B a valores de 0
.loop:
	MOVB AL, [C]	; guarda en AL el caracterer en la posicion del arreglo C
	MOVB [D], AL	; en la posicion de D se escribe el valor que AL tenga 
	INC C ; se incrementa en uno la posicion del caracterer en el arreglo 
	INC D ; aumenta en uno  el valor que D tenga 
	CMPB BL, [C]	; analiza si el numero de caracteres que C tiene se acabaron o no
                
	JNZ .loop		; si no se cumple la anterior condicion se regresa a loop
    MOV D, txtDisplay	; le da a D el valor que txt Display tenga 
    MOV C, erahe		; le da al arreglo C los caracteres que erahe tenga
    MOV B, 1 ;deja al arreglo B en 1
    CALL pint ; llama a la subrutina pint 
    HLT   ; finaliza la subrutina
	RET
   
    
pint:

	MOV B,0 ; deja al arreglo B en 0

.lop:
    MOVB AL, [C] 	; le da a AL el caracter que en la posicion del arreglo C halla 
    MOVB [D], AL    ; en la posicion del arreglo D se escribe lo que en AL halla 
    INC C ; se aumenta en uno la ubicacion del caracter que en C halla 
    INC D ; aumenta en uno el valor de D que es una ubicacion en la memoria 
    CMPB BL, [A]    ; compra el valor que en A halla si que se acabaron los datoss 
    JNZ  .lop       ; si se cumple el anterior cuestionamineto pasa, si no regresa a lop 
    RET
