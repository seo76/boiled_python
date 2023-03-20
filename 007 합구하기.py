"""
import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
l=list(map(int,input().split()))

a=0
l2=[0]

for i in range (n):
    a += l[i]
    l2.append(a)

s, e, h, c= 0, 0, 0, 0

while (e<=n):
    c=l2[e]-l2[s]
    if (c<m):
        e+=1
        print("작",e,s,c)
    elif (c>m):
        s+=1
        print("큰",e,s,c)
    else:
        s+=1
        e+=1
        h+=1
        print("같",e,s,c)
        
print(h)
"""
"""
import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
l=list(map(int,input().split()))

a=0
l2=[0]

for i in range (n):
    a += l[i]
    l2.append(a)

s, e, h, c= 0, 0, 0, 0

while (e<=n):
    c=l2[e]-l2[s]
    if (c<m):
        e+=1
    elif (c>m):
        s+=1
    else:
        s+=1
        e+=1
        h+=1
        
print(h)
"""
"""
import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
l=list(map(int,input().split()))

s, e, h, c= 0, 1, 0, 0

while (s<n):   
    h = l[s]+l[e]
    if (h==m)and(s<e):
        print("m",h,s,e)
        s +=1
        c +=1
    else:
        print("e",h,s,e)
        e +=1
        if (e>=n):
            e = s
            s +=1
#
for _ in range(n):
    h = l[s]+l[e]
    if (h==m):
        s +=1
        c +=1
        print(h)
    elif (h==!m):
        e +=1
        if (e>)
#
print(c)
"""

"""
#Can you calculate the time this code takes up?


import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
l=list(map(int,input().split()))
l.insert(0,0)

s, e, h, c= 0, 1, 0, 0

for _ in range(n):
    s+=1
    for _ in range(n-s):
        e+=1
        h = l[s]+l[e]
        if (h==m):
            c+=1
        if (e>=n):
            e = s+1

print(c)

"""

import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
l=list(map(int,input().split()))
l.insert(0,0)

s, e, h, c= 0, 1, 0, 0

for _ in range(n):
    s+=1
    for _ in range(n-s):
        e+=1
        h = l[s]+l[e]
        if (h==m):
            c+=1
        if (e>=n):
            e = s+1

print(c)







