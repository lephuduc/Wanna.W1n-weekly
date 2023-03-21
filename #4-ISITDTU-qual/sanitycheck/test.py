from pwn import *
f = open('flag.luac','rb')

h = b'auL\x1B'[::-1] + b'\x04\x01\0Q'[::-1] + b'\b\x04\x04'[::-1]


b = f.read()
header = b[:12]
body = xor(b[12:],b'snailgame')


wf = open('flagnew.lua','wb')
wf.write(header+body)

