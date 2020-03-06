bits 32
;se da un numar, se scrie numarul in baza 16 si numarul de biti 1
global start        
extern exit, printf, scanf,fopen,fprintf,fclose  	; exit, printf and scanf are external functions            
import exit msvcrt.dll    
import printf msvcrt.dll    		; tell the assembler that function printf is in msvcrt.dll
import scanf msvcrt.dll     	; 
import fopen msvcrt.dll     	; 
import fclose msvcrt.dll     	; 
import fprintf msvcrt.dll     	; 
                          
segment data use32 class=data
	n dd  0       		
	message  db "Dati urmatorul numar: ", 0  	; strings for C functions must end with ZERO (ASCIIZ strings)       
	format  db "%d", 0  	; strings for C functions must end with ZERO (ASCIIZ strings)       
    moda db "w",0
    nume db "numere.txt",0
    handle dd -1
    formatx db "%x ",0
    formatb db "%d",13,10,0
    
segment code use32 class=code
    start:
    push dword moda
    push dword nume
    call [fopen]
    add esp,4*2
    
    mov [handle],eax
    cmp eax,0
    je final
    
        citire:
        mov ebx,1
        push dword message 	; we store the offset of message (not its value) on the stack
        call [printf]      		; call printf 
        add esp, 4*1       	; free parameters from the stack; 4 = dword size in bytes

        push dword n       		;  push the offset of n
        push dword format		; push the offset of format
        call [scanf]       		; 
        add esp, 4 * 2 		; free 2 dwords from the stack
        
        mov eax,[n]
        cmp eax,0
        je final
        
        push dword eax
        push dword formatx
        push dword [handle]
        call [fprintf]
        add esp,4*3
        
        mov eax,[n]
        mov ecx,0
        bytes:
            mov ebx,1
            and ebx,eax
            shr eax,1
            cmp ebx,1
            je plus
            cmp eax,0
            je finalb
            jmp bytes
            plus:
                inc ecx
                cmp eax,0
                je finalb
                jmp bytes
            finalb:
                push ecx
                push formatb
                push dword [handle]
                call [fprintf]
                add esp,4*3
                jmp citire
            
        jmp citire
        
        final:
        push dword [handle]
        call [fclose]
        add esp,4
        
        push dword 0      		; punem pe stiva parametrul pentru exit
        call [exit]       		; apelam exit pentru a incheia programul

