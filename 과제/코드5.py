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
            
                
f.close()
#print(*Mlist, sep="\n")

dx, dy=[1,0,-1,0], [0,1,0,-1]#우하좌상

queue = deque()
queue2 = deque()
queue.append((s))
queue2.append((s))

z = 0
while queue:
    x,y = queue[-1]
    if (z>2):
        x,y = queue2[-1]
        queue.remove((x,y))
        print("재시")
        z = 0
    z = 0
    for i in range(1):
        mx = x+dx[i]
        my = y+dy[i]        
        if not((0<mx<c+1)and(0<my<l)):
            continue
        if (Mlist[mx][my]==1):#and((mx,my)not in queue):
            z+=1
            x=x+dx[i]
            y=y+dy[i]
            queue.append((x,y))
            print(x,y)
        if (z>2):
            queue2.append((mx,my))
            print("갈",mx,my)
                
                    
            
        


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
        if (z>1): #의미없음 걍 갈림길 지정 포인트
            print("갈",mx,my)
            print(queue[-1])
            x = mx
            y = my
            break
#                continue
"""
print("왜지")












