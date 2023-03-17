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
