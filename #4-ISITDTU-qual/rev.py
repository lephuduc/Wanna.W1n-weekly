import base64
from pwn import *
import codecs
x = base64.b64decode(b'WUpZOpNKO3txchR0dXZ9')

codecs.encode('foobar', 'rot_13')
print(xor(x,b'ISITDTU{abcdef}'))