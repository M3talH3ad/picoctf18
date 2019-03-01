 .intel_syntax noprefix
.bits 32
	
.global asm2

# asm2(0xe,0x21)

asm2:
	push   	ebp  								# intialization
	mov    	ebp,esp								# intialization
	sub    	esp,0x10							# 16 byte offset
	mov    	eax,DWORD PTR [ebp+0xc]				
	mov 	DWORD PTR [ebp-0x4],eax
	mov    	eax,DWORD PTR [ebp+0x8]
	mov	DWORD PTR [ebp-0x8],eax
	jmp    	part_b
part_a:	
	add    	DWORD PTR [ebp-0x4],0x1
	add	DWORD PTR [ebp+0x8],0x41
part_b:	
	cmp    	DWORD PTR [ebp+0x8],0x9886
	jle    	part_a
	mov    	eax,DWORD PTR [ebp-0x4]
	mov	esp,ebp
	pop	ebp
	ret
