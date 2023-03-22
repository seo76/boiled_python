"""
filename = 'maze.txt'
f = open(filename, 'r')
lines = f.readlines() #readline, readlines
print(lines)

lines2 = f.readlines()
i = 0
for line in lines:
    if 'S' in line:
        i+=1
        print(i)

print(i)
"""

"""
filename = 'maze.txt'
f = open(filename, 'r')
lines = f.read(1) #readline, readlines
line= f.read()
#print(lines)
listline=[]
for _ in range(line.count("\n")):
    while
    listline.append(list(map(str,(lines.split()))))

print(listline)
"""
"""
print("줄 수:",(lines.count('\n')+1))

line2 = f.readlines()

#print("공백 수",line.count(" "))
print(line2)
"""

filename = "maze.txt"
f = open(filename,'r')

e = len(list(enumerate(f)))


lines=f.readline()

Mlist=[char for char in list]
"""
for i in range(e):
    i +=1
    
    for j in range(e):
        Mlist[i][j]=(list(map(str,lines.split())))
                    
print(Mlist)
"""
