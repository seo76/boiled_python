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

filename = 'maze.txt'
f = open(filename, 'r')
lines = f.readline() #readline, readlines
print(lines)
print()
lines2 = f.readlines()
i = 0
for line in lines:
    if 'S' in line:
        i+=1
        print(i)







print(myFile.read().count("\n")+1)









                    
        
