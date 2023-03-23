i="*"
j=0

for j in range (5):
    j=j+1
    j=j*i
    print (j)

print("------------")
for j in range(5,0,-1):    
    print(" "*(5-j)+j*"*")

print("------------")
for j in range (5):
    j=j+1
    j=j*i
    print ("%5s"%(j))

print("------------")
for j in range (5):
    j=5-j
    j=j*i
    print ("%5s"%(j))


print("------------")
for j in range(5,0,-1):    
    print(" "*(5-j)+(2*j-1)*"*")

print("------------")
for j in range(5):    
    print(" "*(5-j)+(2*j+1)*"*")
    


        
