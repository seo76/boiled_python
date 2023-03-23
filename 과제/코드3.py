f = open("maze.txt",'r')
lines=f.readlines()
f.close()

Mlist=[]
"""
for line in lines:
    for char in line:
        cj
    m = line.strip()
    Mlist.append(list(map(str,m.split())))

print(Mlist)
"""
"""
for line in lines:
    m = list(line.strip())
    print(m)
    for char in line:
        Mlist.append(char)
print(Mlist)
"""
l, c=0, 0


for line in lines:
    l +=1
for char in line:
    c +=1
print(l,c)
Mlist=[[0]*(c+1) for _ in range (l)]

f = open("maze.txt",'r')
for i in range(l):
    for j in range(c+1):
        n = f.read(1)
        
        if (n=="#"):
            Mlist[i][j]=1
        elif (n==" "):
            Mlist[i][j]=0
        elif(n=="\n"):
            Mlist[i][j]=1
        else:
            Mlist[i][j]=n
   
f.close()
print(*Mlist, sep="\n")












