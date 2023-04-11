#https://www.acmicpc.net/problem/12891

import sys
from collections import deque

input=sys.stdin.readline

n, L = map(int, input().split())
I = input().split()

a = deque()
dq = deque()


def dqbx(inp):
    a.append(inp)
    if len(a)>L:
        a.popleft()

j=0
for i in I:
    j +=1
    dqbx(i)
    if a[j]>a[j-1]:
        dq[j]=a[j-1]
    elif a[j]<a[j-1]:
        dq[j]=a[j]


print(dq)

print(a)







"""
    if int(i) > 0:
        a.append(i)
        print(a)
        if len(a)>1:            
            if a[0]>a[1]:
                print("0",a[0])
                a.popleft()
            else:
                print("1",a[1])
                a.pop()

print(a)        
print(a[0])
"""
