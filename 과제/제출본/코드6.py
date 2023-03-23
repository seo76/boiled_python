from collections import deque

f = open("maze.txt",'r')
lines=f.readlines()
f.close()

l, c=0, 0
for line in lines:
    l +=1
for char in line:
    c +=1
#print(l,c)
Mlist=[[0]*(c+1) for _ in range (l)]
Vlist=[[0]*(c+1) for _ in range (l)]

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
        elif(n=="S"):
            Mlist[i][j]=10
            s=(i,j)
        else:
            Mlist[i][j]=100
            
                
f.close()
#print(*Mlist, sep="\n")

dx, dy=[1,-1,0,0], [0,0,1,-1]#우좌하상

queue = deque()
queue2 = deque()
queue.append((s))
queue2.append((s))

z = 0
while queue:
    x,y = queue[-1]
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if not((0<mx<c+1)and(0<my<l)):
            continue            
        if (Mlist[mx][my]==1)and((mx,my)not in queue):
            x=x+dx[i]
            y=y+dy[i]
            queue.append((x,y))
            #print(x,y)
            if (Mlist[mx+1][my]+Mlist[mx][my+1]+Mlist[mx-1][my]+Mlist[mx][my-1]==3):#갈래
                queue2.append((x,y))
                #print("rk",x,y)
            if (Mlist[mx+1][my]+Mlist[mx][my+1]+Mlist[mx-1][my]+Mlist[mx][my-1]==1):
                while True:
                    tx, ty = queue.pop()
                    Mlist[tx][ty]=0
                    if (queue[-1]==queue2[-1]):
                        break
                queue.clear()
                queue.append((s))
                #print(*Mlist, sep="\n")
                continue
        elif(Mlist[mx][my]==100):
            #print("end")
        else:
            continue
            
"""
        if (Mlist[mx][my]==0):
            z+=1
            if (z==2):
                print("z",x,y)
            if (z==3):
                print(z)
                queue2.append(queue)
                queue.clear()
                queue.append((s))
"""

"""        if (Mlist[mx][my]==1):
            z+=1
            if (z>2):
                print("갈",mx,my)"""
        
            
"""        
        while (z==1):
            mx =x+dx[i]
            my =y+dy[i]
            if (Mlist[mx][my]==1):
                queue.append((mx,my))
                print("직",mx,my)
                x = mx
                y = my
            else:
                break
            
                #if (Mlist[mx][my]==1)
        i
"""
print("왜지")












