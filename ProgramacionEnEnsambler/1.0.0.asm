; Example 1.1:
; Writes "Hello World!" to the text display

	JMP boot

stackTop    EQU 0xFF    ; Initial SP
txtDisplay  EQU 0x2E0

hello:	DB "PRIMERTABAJOQUEHAGODEENSAMBLER"	; Output string
		DB 0				; String terminator
        
erahe:  DB "                                   ";
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
	JNZ .loop		; Jump back to loop if not
    CALL pint 
    HLT             ;    
	RET
    
pint:

	MOV B,0

.lop:
	MOVB AL, [A] 	;
    MOVB [D], AL    ;
    INC A 
    INC D
    CMPB BL, [A]    ;
    JNZ  .lop       ;
    RET