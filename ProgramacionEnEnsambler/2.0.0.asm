; Example 1.2:
; Prints a 16x16 sprite into the visual display

	JMP boot

vslDisplay EQU 0x300


sprite: 
	DB "\xC4"
Time:	DB "123456789101112131415161718192021222324252627282930"	; Output string
		DB 0				; String terminator  
    





    
    
    
	
    
  
boot:
	MOV C, sprite		; C points to the sprite
	MOV D, vslDisplay	; D points to the fb
    MOV B, Time
     

.loop:
	DEC D
	MOVB [D], 0xFF
   
    
    
    
	INC D
	MOVB AL, [C]	; Print all the pixels
	MOVB [D], AL
	INC D 
	CMP D, 0x30F 
    
	JNZ .loop
    
    
	HLT
    
    
    
    
    
    
