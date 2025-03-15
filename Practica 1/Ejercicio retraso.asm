;Esta es la ultima version del delay, el tiempo que tarde en borrarse el texto es deacuerdo al tamaño del arreglo llamado time, sinembargo tiene un espacio limitado que depende del numero de datos que pueda guardar un arreglo





	JMP boot

stackTop    EQU 0xFF    ; se define el valor de stacktop como 0xFF 
txtDisplay  EQU 0x2E0   ;se define txtDisplay con el valor de 0x2E0

hello:	DB "PRIMERTABAJOQUEHAGODEENSAMBLER"	; se define el arreglo hello con los caracteres para cubrir la pantalla de texto
		DB 0				; se define cero para terminar el arreglo 
        
Time:	DB "123456789101112131415161718192021222324252627282930"	; se define el arreglo time con una cantidad de numeros a leer 
		DB 0				; se define el final del arreglo con cero         
        
            
erahe:  DB "                               ";se define erahe para borrar los caracteres en la pantalla de texto 
		DB 0; se define el final del arreglo con un cero 

boot:
	MOV SP, stackTop	; se estable el puntero en stacktop 
	MOV C, hello		; se le da al arreglo el valor que hello tiene 
  
	MOV D, txtDisplay	;se le da a D el valor de txtDisplay que es una posicion en la memoria que refiere a donde empieza la pantalla de texto
	CALL print              ; se manda a llamar la subrutina print 
	HLT				; finaliza la subrutina 

print:				; Print string
	
	MOV B, 0 ; se establece a B en cero 
.loop:
	MOVB AL, [C]	; toma el caracter que en la possicion del arreglo C este y se la da a AL
	MOVB [D], AL	; en a posicion D se esrcribe lo que AL tenga 
	INC C		; aumenta en uno el valor de C
	INC D		; aumenta en uno el valor de D
	CMPB BL, [C]	; compara si el valor de la posicion de C es cero o no
                ;
	JNZ .loop		; si lo es termina la subrutina 
 
    MOV C, Time		; le da a C el valor del arreglo Time
    MOV B, 1		; pone a B en 1 
    CALL time		; llama a la subrutina time 
    HLT    		; termina la subrutina time 
	RET
    
    
    
time:
	MOV B,0 ; pone a B en cero
    
.lup:
    MOVB AL, [C]	; le da a AL el valor que en la posicion de C este 
    INC C               ; aumenta en uno C
    CMPB BL, [C]	; compara C si es que ya no tiene caracteres 
    JNZ .lup		; si ya no tiene se acaba la subrutina 
    MOV D, txtDisplay	; se le da a D el valor de txtDisplay que es una posicion de la memoria 
    MOV C, erahe        ; se le da a C el valor  de erahe 
    MOV B, 1		; se pone a B en 1
    CALL pint 		; se llama la subrutina pint 
    HLT     		; se termina la subrutina 
    
	RET
	
pint:

	MOV B,0		; se define a B en cero 

.lop:
    MOVB AL, [C]    ;se le da a AL el valor que en la posicion de C este 
    MOVB [D], AL    ;se escribe en la posicion de D lo que AL tenga 
    INC C 	    ; se aumenta en uno el valor de C
    INC D	    ; se aumenta en uno el valor de D
    CMPB BL, [C]    ; se compara el valor de C si es cero termina la subrutina 
    JNZ  .lop       ; si no se cumple la condicion anterior regresa a lop
    RET
