"""#006연속된 자릿수..

import sys
input = sys.stdin.readline
l=[]
l2=[0]
temp=0
n = int(input())

for i in range (n): #(1,n+1):
    i+=1    
    l.append(i)
    l2.append(int(i*(i+1)/2))
    i+=1
    temp +=i
    l2.append(temp)
    
print(l2)

#    l2.append(temp)

m, a, b= 0, 0, 1


while (b<n):
    h=l[b]-l[a]
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
    
"""


"""

import sys
input = sys.stdin.readline
l=[]
l2=[0]
temp=0
n = int(input())

for i in range (n):
    i+=1    
    l.append(i)
    temp +=i
    l2.append(temp)

m, a, b= 0, 0, 1


for _ in range(n):
    h=l2[b]-l2[a]
    if (h<n):
        b+=1
    if (h>n):
        a+=1
    if (h==n):
        m+=1
        a+=1
        b+=1

print(m+1)


"""

"""
l=[0]
temp, m, a, b=0, 0, 0, 1

n = int(input())

for i in range(n):
    i+=1    
    temp +=i
    l.append(temp)
    h=l[b]-l[a]
    if (h<n):
        b+=1
    elif (h>n):
        a+=1
    else:
        m+=1
        a+=1
        b+=1
        
print(m+1)
"""


"""
l=[0]
temp, m, a, b=0, 0, 0, 1

n = int(input())

for i in range(n):
    i+=1    
    temp +=i
    l.append(temp)
    h=l[b]-l[a]
    if (h<n):
        print("큰",h,l[a],l[b],b)
        b+=1
        #h=l[b]-l[a]
    elif (h>n):

        print("작",h,l[a],l[b],a)
        a+=1
        #h=l[b]-l[a]
    else:
        print("같",h,l[a],l[b],b,"★")
        m+=1
        a+=1
        b+=1
        #h=l[b]-l[a]

print(l)
print(m+1)
"""


n=int(input())
temp, a, b, m = 0, 0, 0, 0

while (b<n+1):
    if (temp == n):
        m+=1
        a+=1
        b+=1
        temp=temp+b-a
        print("같:",a,b,temp,"★")
    elif (temp < n):
        b+=1
        temp+=b
        print("작:",a,b,temp)
    else:
        a+=1
        temp-=a
        print("큰:",a,b,temp)
        
        

    
print(m)

        




    
     
