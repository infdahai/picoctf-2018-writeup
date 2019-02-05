# be-quick-or-be-dead-1
Points: 200

## Category
Reversing

## Question
>You [find](https://www.youtube.com/watch?v=CTt1vk9nM9c) this when searching for some music, which leads you to [be-quick-or-be-dead-1](files/be-quick-or-be-dead-1). Can you run it fast enough? You can also find the executable in /problems/be-quick-or-be-dead-1_3_aeb48854203a88fb1da963f41ae06a1c. 

### Hint
>What will the key finally be?

## Solution
Overwrite the _set_timer_ function with nops by patching the program.

```asm
[0x00400849]> pdf
|           ;-- main:
/ (fcn) sym.main 62
|   sym.main (int arg1, int arg2);
|           ; var int local_10h @ rbp-0x10
|           ; var int local_4h @ rbp-0x4
|           ; DATA XREF from entry0 (0x4005bd)
|           0x00400827      55             push rbp
|           0x00400828      4889e5         mov rbp, rsp
|           0x0040082b      4883ec10       sub rsp, 0x10
|           0x0040082f      897dfc         mov dword [local_4h], edi   ; arg1
|           0x00400832      488975f0       mov qword [local_10h], rsi  ; arg2
|           0x00400836      b800000000     mov eax, 0
|           0x0040083b      e8a9ffffff     call sym.header
|           0x00400840      b800000000     mov eax, 0
|           0x00400845      90             nop
|           0x00400846      90             nop
|           0x00400847      90             nop
|           0x00400848      90             nop
|           0x00400849      90             nop
|           0x0040084a      b800000000     mov eax, 0
|           0x0040084f      e842ffffff     call sym.get_key
|           0x00400854      b800000000     mov eax, 0
|           0x00400859      e863ffffff     call sym.print_flag
|           0x0040085e      b800000000     mov eax, 0
|           0x00400863      c9             leave
\           0x00400864      c3             ret
[0x00400849]> exit
```

Save and run the program to get the flag.

Patched binary [be-quick-or-be-dead-1_patched](solution/be-quick-or-be-dead-1_patched).

### Flag
`picoCTF{why_bother_doing_unnecessary_computation_27f28e71}`


https://tcode2k16.github.io/blog/posts/picoctf-2018-writeup/reversing/#be-quick-or-be-dead-1
将那个数值减少。

还有一种想法,
```asm
[0x004005a0]> aa
[x] Analyze all flags starting with sym. and entry0 (aa)
[0x004005a0]> pdf 
            ;-- section..text:
            ;-- _start:
            ;-- rip:
/ (fcn) entry0 41
|   entry0 (int arg3);
|           ; arg int arg3 @ rdx
|           0x004005a0      31ed           xor ebp, ebp                ; [14] -r-x section size 834 named .text
|           0x004005a2      4989d1         mov r9, rdx                 ; arg3
|           0x004005a5      5e             pop rsi
|           0x004005a6      4889e2         mov rdx, rsp
|           0x004005a9      4883e4f0       and rsp, 0xfffffffffffffff0
|           0x004005ad      50             push rax
|           0x004005ae      54             push rsp
|           0x004005af      49c7c0e00840.  mov r8, sym.__libc_csu_fini ; 0x4008e0
|           0x004005b6      48c7c1700840.  mov rcx, sym.__libc_csu_init ; 0x400870 ; "AWAVA\x89\xffAUATL\x8d%\x8e\x05 "
|           0x004005bd      48c7c7270840.  mov rdi, sym.main           ; 0x400827
\           0x004005c4      e897ffffff     call sym.imp.__libc_start_main ; int __libc_start_main(func main, int argc, char **ubp_av, func init, func fini, func rtld_fini, void *stack_end)
[0x004005a0]> pdf @ sym.main
            ;-- main:
/ (fcn) sym.main 62
|   int sym.main (int argc, char **argv, char **envp);
|           ; var int var_10h @ rbp-0x10
|           ; var int var_4h @ rbp-0x4
|           ; arg int argc @ rdi
|           ; arg char **argv @ rsi
|           ; DATA XREF from entry0 (0x4005bd)
|           0x00400827      55             push rbp
|           0x00400828      4889e5         mov rbp, rsp
|           0x0040082b      4883ec10       sub rsp, 0x10
|           0x0040082f      897dfc         mov dword [var_4h], edi     ; argc
|           0x00400832      488975f0       mov qword [var_10h], rsi    ; argv
|           0x00400836      b800000000     mov eax, 0
|           0x0040083b      e8a9ffffff     call sym.header
|           0x00400840      b800000000     mov eax, 0
|           0x00400845      e8f8feffff     call sym.set_timer
|           0x0040084a      b800000000     mov eax, 0
|           0x0040084f      e842ffffff     call sym.get_key
|           0x00400854      b800000000     mov eax, 0
|           0x00400859      e863ffffff     call sym.print_flag
|           0x0040085e      b800000000     mov eax, 0
|           0x00400863      c9             leave
\           0x00400864      c3             ret
0x004005a0]> pdf @ sym.set_timer 
/ (fcn) sym.set_timer 84
|   sym.set_timer ();
|           ; var int var_ch @ rbp-0xc
|           ; var int var_8h @ rbp-0x8
|           ; CALL XREF from sym.main (0x400845)
|           0x00400742      55             push rbp
|           0x00400743      4889e5         mov rbp, rsp
|           0x00400746      4883ec10       sub rsp, 0x10
|           0x0040074a      c745f4010000.  mov dword [var_ch], 1
|           0x00400751      be23074000     mov esi, sym.alarm_handler  ; 0x400723
|           0x00400756      bf0e000000     mov edi, 0xe                ; 14
|           0x0040075b      e810feffff     call sym.imp.__sysv_signal
|           0x00400760      488945f8       mov qword [var_8h], rax
|           0x00400764      48837df8ff     cmp qword [var_8h], 0xffffffffffffffff
|       ,=< 0x00400769      751e           jne 0x400789
|       |   0x0040076b      be3b000000     mov esi, 0x3b               ; ';' ; 59
|       |   0x00400770      bf28094000     mov edi, str.Something_went_terribly_wrong.___Please_contact_the_admins_with__be_quick_or_be_dead_1.c:_d_. ; 0x400928 ; "\n\nSomething went terribly wrong. \nPlease contact the admins with \"be-quick-or-be-dead-1.c:%d\".\n"
|       |   0x00400775      b800000000     mov eax, 0
|       |   0x0040077a      e8c1fdffff     call sym.imp.printf         ; int printf(const char *format)
|       |   0x0040077f      bf00000000     mov edi, 0
|       |   0x00400784      e8f7fdffff     call sym.imp.exit           ; void exit(int status)
|       |   ; CODE XREF from sym.set_timer (0x400769)
|       `-> 0x00400789      8b45f4         mov eax, dword [var_ch]
|           0x0040078c      89c7           mov edi, eax
|           0x0040078e      e8bdfdffff     call sym.imp.alarm
|           0x00400793      90             nop
|           0x00400794      c9             leave
\           0x00400795      c3             ret

```
感觉把set_timer中nop去掉酒醒，不过r2还没怎么学过
