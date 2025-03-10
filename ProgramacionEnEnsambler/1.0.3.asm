; Example 1.1:
; Writes "Hello World!" to the text display

	JMP boot

stackTop    EQU 0xFF    ; Initial SP
txtDisplay  EQU 0x2E0

hello:	DB "PRIMERTABAJOQUEHAGODEENSAMBLER"	; Output string
		DB 0				; String terminator
        
Time:	DB "123456789101112131415161718192021222324252627282930"	; Output string
		DB 0				; String terminator        
        
            
erahe:  DB "                               ";
		DB 0;

boot:
	MOV SP, stackTop	; Set SP
	MOV C, hello		; Point register C to string
  
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
 
    MOV C, Time		; Point register C to string
    MOV B, 1
    CALL time
    HLT     
	RET
    
    
    
time:
	MOV B,0
    
.lup:
	MOVB AL, [C]	; Get character
    INC C
    CMPB BL, [C]	; Check if string terminator
    JNZ .lup		; Jump back to loop if not
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