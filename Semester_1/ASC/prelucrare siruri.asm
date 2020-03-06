bits 32 ; assembling for the 32 bits architecture
;

;se dau doua siruri. Sa se scrie literele mici din primul, din al doilea cifrele



; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,scanf,printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import printf msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    msg1 db "dati sirul 1: ",0
    msg2 db 13,10,"dati sirul 2: ",0
    s1 times 100 db 0
    s2 times 100 db 0
    format db "%s",0
    formatc db "%c",0

; our code starts here
segment code use32 class=code
    start:
        push dword msg1
        call [printf]
        add esp,4
        
        push dword s1
        push dword format
        call [scanf]
        add esp,4*2
        
        mov esi,0
        repeta:
        mov al,[s1+esi]
        inc esi
        cmp al,0
        je sir2
        cmp al,96
        jg mica
        jmp repeta
        mica:
            cmp al,123
            jl afis
            jmp repeta
            afis:
                cbw
                cwde
                pushad
                push eax
                push formatc
                call [printf]
                add esp,4*2
                popad
                jmp repeta
                
        sir2:
        push msg2
        call [printf]
        add esp,4
        
        push dword s2
        push dword format
        call [scanf]
        add esp,4*2
        
        mov esi,0
        repeta2:
        mov al,[s2+esi]
        inc esi
        cmp al,0
        je final
        cmp al,47
        jg cifra
        jmp repeta2
            cifra:
            cmp al,58
            jl afisare
            jmp repeta2
            afisare:
                cbw
                cwde
                pushad
                push dword eax
                push dword formatc
                call [printf]
                add esp,4*2
                popad
                jmp repeta2
        final:
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
