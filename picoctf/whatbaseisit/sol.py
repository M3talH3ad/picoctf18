import pwn
import re

host, port = '2018shell.picoctf.com', 15853
s = pwn.remote(host, port)

st = s.recv()
print st
binary_string = re.findall('the (.*) as a word', st)[0]
answer=hex(int(binary_string.replace(' ', ''), 2))[2:].decode('hex')
s.sendline(answer)

st = s.recv()
print st
hex_string = re.findall('the (.*) as a word', st)[0]
s.sendline(hex_string.decode('hex'))

st = s.recv()
print st
octal_string = re.findall('the (.*) as a word', st)[0]
answer=''.join([ chr(int(c, 8)) for c in octal_string.split() ])
s.sendline(answer)

st = s.recv()
print st

s.close()
