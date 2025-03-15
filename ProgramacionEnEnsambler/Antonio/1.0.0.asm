#para este primer vistazo alcance a agregar las dos lineas y ver donde se guardaban los datos ademas de donde lograr agregar las funciones necesarias 







; primer vistazo:


	JMP boot

stackTop    EQU 0xFF    ; 
txtDisplay  EQU 0x2E0   ; es la variable que nos indica donde va a estar el texto

hello:	DB "PRIMERTABAJOQUEHAGODEENSAMBLER"	; aqui se genera un arreglo que guarda el texto a imprimir 
		DB 0				; 
        
erahe:  DB "                                   "; este arreglo  tiene el mismo tamaño que el primero pero con puros espacios que en patalla de texto se ve como blanco 
		DB 0;

boot:
	MOV SP, stackTop	; le asigna al puntero de escritura la posicion de stackTop
	MOV C, hello		; le da a el registro C lo que tiene hello
    MOV A, erahe        ;
	MOV D, txtDisplay	; asigna D como la posicion de las salidas en la pantalla de texto
	CALL print		; llama a la funcion print 
	HLT				; Halt execution

print:				; Print string
	
	MOV B, 0 ;deja a B con varoles de cero 
.loop:
	MOVB AL, [C]	; Toma los datos que en el arreglo C esten siendo representados por AL  
	MOVB [D], AL	; toma de la representacion de AL el valor y lo escribe en D, D esta refieriendo a una direccion 
	INC C ; aumenta en uno el valor de la posicion del arreglo C
	INC D ; aumenta el valor de la direccion de que refiere D 
	CMPB BL, [C]	; se hace la revision del arreglo C es decir si los caracteres se acabaron
	JNZ .loop		; regresa al inicio del loop si la condicion no se cumple
    CALL pint ; al cumplirse la condicion llama a la funcion pint  
    HLT             ;  es para detener el proceso de la funcion cuando termine de ejecutarse 
	RET	    ; detiene la  la subrutina
    
pint:

	MOV B,0 ; regresa a 0 todos los valores de B 

.lop:
    MOVB AL, [A] 	; mueve de la posicion actual de A el valor que este tenga y  lo obtiene temporalmente AL
    MOVB [D], AL    ; la posicion actual del arreglo D obtiene el valor de AL
    INC A ; aumenta en uno la posicion que se tenga del arreglo A
    INC D ;  aumenta en uno la posicion que se tenga del arreglo D
    CMPB BL, [A]    ;se compara el valor de BL y la direccion actual de A en el arreglo
    JNZ  .lop       ; si se cumple la condicion antrior se termina el lop 
    RET ; se detiene la subrutina 
