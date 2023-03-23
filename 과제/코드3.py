
f = open("maze.txt",'r')
lines=f.readlines()
f.close()
"""
Mlist=[]

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
#print(l,c)
Mlist=[[0]*(c+1) for _ in range (l)]

f = open("maze.txt",'r')
for i in range(l):
    for j in range(c+1):
        n = f.read(1)
        
        if (n=="#"):
            Mlist[i][j]=0
        elif (n==" "):
            Mlist[i][j]=1
        elif(n=="\n"):
            Mlist[i][j]=0
        else:
            Mlist[i][j]=n
            if (Mlist[i][j]=="S"):
                s=(i,j)
            elif (Mlist[i][j]=="G"):
                g=(i,j)
                
f.close()
print(*Mlist, sep="\n")

dx, dy=[1,0,-1,0], [0,1,0,-1]#우하좌상
'''
def room(p):
    if (p[0]<0 or point[])

'''
queue = [(s)]
x, y = s

while True:
    #queue.pop(0)
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if ((0<mx<c+1)and(0<my<l)):
            if ((Mlist[mx][my] == 1)and(mx,mx!=queue[-1])):
                queue.append((mx,my))
                



                Mlist[mx][my]="*"
                print(mx,my)
                x =mx
                y =my
            elif(Mlist[mx][my] == 0):
                queue.pop()
            if (Mlist[mx][my] == "G"):
                break

print(queue.count())





