
#primer código 

stackTop EQU 0xFF       
textDisplay EQU 0x2E0   
vslDisplay EQU 0x301    

Text: DB " Ensamblador corto! ", 0  
Borrar: DB "                 ", 0  
sprite: DB "\x2F"  

Inicio:
    MOV SP, stackTop     
    MOV C, Text         
    MOV D, textDisplay  
    CALL print                   
    CALL clearScreen    
    CALL drawSprite     
    HLT                

print:
    MOV B, 0            
nextChar:
    MOVB AL, [C]        
    CMPB AL, 0          
    JZ donePrint        
    MOVB [D], AL        
    INC C               
    INC D               
    JMP nextChar        
donePrint:
    RET                               

clearScreen:
    MOV C, Borrar       
    MOV D, textDisplay  
    CALL print          
    RET                

drawSprite:
    MOV D, vslDisplay   
    MOVB [D], 0x2F      
    RET
