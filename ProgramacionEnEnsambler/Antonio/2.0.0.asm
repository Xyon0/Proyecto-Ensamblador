;este programa mueve un pixel o bit de informacion exadecimal que contiene el codigo de color sobre la primera fila de la pantalla, sin embargo no logre agregar la funcion de delay creada 


	

	JMP boot

vslDisplay EQU 0x300 ;se le da a vslDisplay el valor de 0x300


sprite: 								;se define el arreglo sprite con un valor hexadecimal que es un pixel de color 
	DB "\xC4"

Time:	DB "123456789101112131415161718192021222324252627282930"	; se define el arreglo Time con diferentes numeros para dar paso a un pequeño tiempo
		DB 0							; se define el fin del arreglo que es 0 

boot:
	MOV C, sprite		; se le da a C el valor que sprite tenga 
	MOV D, vslDisplay	; se le da a D el valor de vlsDisplay que es una posicion 
   	MOV B, Time		; se le da al arreglo B el valor que Time tiene
     

.loop:
	DEC D                   ; se disminuye en uno el valor de D para que no aparezca otra vez el pixel anterior 
	MOVB [D], 0xFF		; la posicion que D representa en la pantalla se define como un pixel blanco 
   
    
    
    
	INC D			; se aumenta en uno D que es una posicion 
	MOVB AL, [C]		; se le da a AL el valor que C tenga 
	MOVB [D], AL		; se le da a la posiciion en la memoria que representa D el valor que AL tenga 
	INC D 			; se aumenta en uno el valor que D tenga 
	CMP D, 0x30F		; se compara el valor de D con 0x30F  
    
	JNZ .loop               ; si son iguales si finaliza la subrutina
    
    
	HLT			;finaliza la subrutina 
    
    
    
    
    
    
