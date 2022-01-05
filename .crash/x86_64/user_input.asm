section .data
		prompt db "What is your name? "
		hello db "Hello, "

section .bss
		name resb 16

section .text
		global _start
_start:
		call _promptUser
		call _getUser
		call _helloUser
		call _nameUser
		call _exitCode

_promptUser:
		mov rax, 1
		mov rdi, 1
		mov rsi, prompt
		mov rdx, 19
		syscall
		ret

_helloUser:
		mov rax, 1
		mov rdi, 1
		mov rsi, hello
		mov rdx, 7
		syscall
		ret

_nameUser:
		mov rax, 1
		mov rdi, 1
		mov rsi, name
		mov rdx, 16
		syscall
		ret

_getUser:
		mov rax, 0
		mov rdi, 0
		mov rsi, name
		mov rdx, 16
		syscall
		ret

_exitCode:
		mov rax, 60
		mov rdi, 0
		syscall
		ret
