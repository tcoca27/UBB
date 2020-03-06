bits 32 ; assembling for the 32 bits architecture


;se da numele fisierului si un N, se afiseazza suma bitilor N din fiecare byte din fisier


; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,fopen,fclose,scanf,printf,fread     ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fclose msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fread msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    filename dd 0
    handle dd -1
    formatfn dd "%s",0
    msg db "Dati numele fisierului: ",0
    n db 0
    formatn db "%d",0
    format db "%d",0
    msgn db "dati N: ",0
    modr db "r",0
    c db 0

; our code starts here
segment code use32 class=code
    start:
        push dword msg
        call [printf]
        add esp,4
        
        push dword filename
        push dword formatfn
        call [scanf]
        add esp,4*2
        
        push dword modr
        push dword filename
        call [fopen]
        add esp,4*2
        
        mov [handle],eax
        cmp eax,0
        je final
        
        push msgn
        call [printf]
        add esp,4
        
        push dword n
        push formatn
        call [scanf]
        add esp,4*2
        
        
        mov ebx,0
        citire:
            push dword [handle]
            push dword 1
            push dword 1
            push dword c
            call [fread]
            add esp,4*4

            cmp eax,0
            je final
            
            mov cl,[n]
            dec cl
            
            mov al, byte [c]
            shr eax,cl
            and al,1
            cmp al,1
            je adunare
            jmp citire
            adunare:
                inc ebx
                jmp citire
            
        final:
        pushad
            mov eax,ebx
            push dword eax
            push dword format
            call [printf]
            add esp,4*2
        popad
            
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
