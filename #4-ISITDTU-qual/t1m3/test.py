def unpack(s):
    return [int(s.split()[2]),int(s.split('>')[1].split(',')[0])]
f = open('dk.sql','r')
dk = []
for e in f.readlines():
    if e=='\n':
        continue
    dk.append(e)
D = {}
for i in range(len(dk)):
    s,num = unpack(dk[i])
    D[s]=num    

for c in D.values():
    print(chr(c+1),end = "")