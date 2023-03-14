#006연속된 자릿수..

import sys
input = sys.stdin.readline
l=[]
l2=[0]
temp=0
n = int(input())

for i in range (n): #(1,n+1):
    i+=1    
    l.append(i)
    """l2.append(int(i*(i+1)/2))
    i+=1"""
    temp +=i
    l2.append(temp)
    
print(l2)

#    l2.append(temp)

m, a, b= 0, 0, 1


while (b<n):
    h=l2[b]-l2[a]
    if (h<n):
        b+=1
        print("큰:",h)
    if (h>n):
        a+=1
        print("작:",h)
    if (h==n):
        m+=1
        a+=1
        b+=1
        print("같:",a,b,h)
    if (a>b):
        print("z")
        break

print(m+1)
    

    

     
