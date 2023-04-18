#https://www.acmicpc.net/problem/11003
#bb

import sys
from collections import deque

input=sys.stdin.readline

n, L = map(int, input().split())
I = input().split()

a = deque()
dq = []


def dqbx(inp):
    a.append(inp)
    if len(a)>L:
        a.popleft() #a안은 L개씩 요소의 개수 유지
    return inp

j=0
for i in I:
    dqbx(i)
    print(a)
    dq.append(i)
    if j>0:
        if a[-1]>a[-2]: #a에 추가된 게 이전 것 보다 클 경우
            dq[j]=a[-2] #D에는 이전 것으로 숫자 채우기
        elif a[-1]<a[-2]: #추가 된 게 더 작을 경우
            dq[j]=a[-1] #추가 된 것으로 숫자 채우기
    print(j)
    print(dq)

    j +=1

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
