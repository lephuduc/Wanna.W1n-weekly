from arc4 import ARC4
cipher = b'\xc1\xf5\xb3\x1a\x96=\\\xdb7:"J\x95\x07\x19\x19\xe9\xc3\xf6#60\xedT\x17\xb0\xe6F\xbe?'[:5]
try:
    for i in range(4191821096,0,-1):
        arc = ARC4(str(i).encode())
        decrypted = arc.decrypt(cipher)
        
        if b'ISITD' in decrypted:
            print(decrypted,i)
except:
    print(i)