#https://www.acmicpc.net/problem/11003
#bb
"""

import sys
from collections import deque

input=sys.stdin.readline

n, L = map(int, input().split())
I = list(map(int, input().split()))

a = deque()
D = []


def dqbx(inp):
    global m
    if inp<1:
        inp=1
    a.append(inp)
    if len(a)>L:
        a.popleft() #a안은 L개씩 요소의 개수 유지
    m=a[0]
    for aa in a:
        if m<aa: #m보다 다른 요소가 더 크면
            m=m #m이 min
        else: #m보다 다른 요소가 같거나 작으면
            m=aa #min은 그 다른 요소
    return m

for i in I:
    dqbx(i)
    print(a)
    D.append(m)
    print(D)


print(*D, sep=" ")
"""


import sys
from collections import deque

input=sys.stdin.readline

n, L = map(int, input().split())
I = list(map(int, input().split()))

a = deque()
D = []


def dqbx(inp):
    global m
    if inp<1:
        inp=1
    a.append(inp)
    if len(a)>L:
        a.popleft()
    m=a[0]
    for aa in a:
        if m<aa:
            m=m 
        else:
            m=aa
    return m

for i in I:
    dqbx(i)
    D.append(m)
    
print(*D, sep=" ")




"""

for d in D:
    print(d)
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
