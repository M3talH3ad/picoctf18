cipher_text="^WQ]1B4iQ/SaO@M1W>V3`AMXcABMO@3\BMa3QC`3k"
flag=''
for c in cipher_text:
	flag+=chr(ord(c)+18)

print flag
