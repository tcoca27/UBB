bits 32
;se da o propozitie in fisier, afisati palindroamele
global start

extern scanf,fread,printf,exit,fopen,fclose
import scanf msvcrt.dll
import fread msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll

segment data use32 class=data
    filename dd 0
    formatfn dd "%s",0
    msg db "Dati numele fisierului: ",0
    moda db "r",0
    handle dd -1
    cuvant times 10 db 0
    c dd 0
    len db 0
    format db "%c",0
    formats db "%s ",0
    message db "display", 0
    
segment code use32 class=code
start:
    push dword msg
    call [printf]
    add esp,4
    
    push dword filename
    push dword formatfn
    call [scanf]
    add esp,4*2
    
    push dword moda
    push dword filename
    call [fopen]
    add esp,4*2
    
    mov [handle],eax
    cmp eax,0
    je final
    
    mov esi,0
    citire:
        push dword [handle]
        push dword 1
        push dword 1
        push dword c
        call [fread]
        add esp,4*4
        
        cmp eax,0
        je final
        
        
        mov al,byte [c]
        
        
        cmp al,32
        je cuvantnou
        
        mov [cuvant+esi],al
        inc esi
        jmp citire
        
        cuvantnou:
            mov ecx,esi
            mov dword [len],ecx
            mov edi,0
            jmp palindromq
            nupalindrom:
                mov ecx,[len]
                mov edi,0
                sterge:
                    mov byte [cuvant+edi],0
                    inc edi
                    loop sterge
                    jmp continuare
            
                palindromq:
                    mov al,[cuvant+edi]
                    inc edi
                    dec esi
                    mov bl,[cuvant+esi]
                    
                    cmp al,bl
                    jne nupalindrom
                    loop palindromq
            palindromda:
                mov ecx,[len]
                mov esi,0
                
                pushad
                    push dword cuvant
                    push dword formats
                    call [printf]
                    add esp, 4*2
                popad
               
            continuare:
                mov esi,0
                mov edi,0
                mov ecx,0
                jmp citire
    final:
        push dword [handle]
        call [fclose]
        add esp,4*1
        
        push dword 0
        call [exit]