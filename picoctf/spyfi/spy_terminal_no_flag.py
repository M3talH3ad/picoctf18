#!/usr/bin/python2 -u
from Crypto.Cipher import AES

agent_code = """flag"""
key= """key"""

def pad(message):
    if len(message) % 16 != 0:
        message = message + '0'*(16 - len(message)%16 )
    return message

def encrypt(key, plain):
    cipher = AES.new( key.decode('hex'), AES.MODE_ECB )
    return cipher.encrypt(plain).encode('hex')

welcome = "Welcome, Agent 006!"

sitrep = raw_input("Please enter your situation report: ")

message = """Agent,
Greetings. My situation report is as follows:
{0}
My agent identifying code is: {1}.
Down with the Soviets,
006
""".format( sitrep, agent_code )

message = pad(message)


cipher_text = encrypt( """key""", message )
print cipher_text

cipher = AES.new( key.decode('hex'), AES.MODE_ECB)

print cipher.decypt(cipher_text)
