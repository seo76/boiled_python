"""
a, q = map(int, input().split())

arr=[] 
arr2=[[0 for _ in range(a+1)]for _ in range(a+1)]
temp=0
temp2=0


for i in range(a):
    arr.append(list(map(int,input().split())))
    temp=0
    for k in range(a):
        temp += arr[i][k]
        arr2[i+1][k+1]= temp+arr2[i][k+1]

print(*arr2,sep="\n")

for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr2[x2][y2])
    print(arr2[x1-1][y2])
    print(arr2[x2][y1-1])
    print(arr2[x1-1][y1-1])
    print(arr2[x2][y2]-arr2[x1-1][y2]-arr2[x2][y1-1]+arr2[x1-1][y1-1])
"""
"""
a, q = map(int, input().split())

arr=[] 
arr2=[[0 for _ in range(a+1)]for _ in range(a+1)]
temp=0

for i in range(a):
    arr.append(list(map(int,input().split())))
    temp=0
    for k in range(a):
        temp += arr[i][k]
        arr2[i+1][k+1]= arr[i][k]+arr2[i][k+1]+arr2[i+1][k]-arr2[i][k]
print(*arr2,sep="\n")
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr2[x2][y2]-arr2[x1-1][y2]-arr2[x2][y1-1]+arr2[x1-1][y1-1])

"""

"""
a, q = map(int, input().split())

arr=[] 
arr2=[[0 for _ in range(a+1)]for _ in range(a+1)]

for i in range(a):
    arr.append(list(map(int,input().split())))
    for k in range(a):
        arr2[i+1][k+1]= arr[i][k]+arr2[i][k+1]+arr2[i+1][k]-arr2[i][k]
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr2[x2][y2]-arr2[x1-1][y2]-arr2[x2][y1-1]+arr2[x1-1][y1-1])

"""

"""

import sys

a, q = map(int, sys.stdin.readline().split())

arr=[] 
arr2=[[0]*(a+1)for _ in range(a+1)]

for i in range(a):
    arr.append(list(map(int, sys.stdin.readline().split())))
    for k in range(a):
        arr2[i+1][k+1]= arr[i][k]+arr2[i][k+1]+arr2[i+1][k]-arr2[i][k]
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr2[x2][y2]-arr2[x1-1][y2]-arr2[x2][y1-1]+arr2[x1-1][y1-1])

"""


import sys
input = sys.stdin.readline

a, q = map(int, input().split())

arr=[] 
arr2=[[0]*(a+1)for _ in range(a+1)]

for i in range(1,a+1):
    arr.append(list(map(int, input().split())))
    for k in range(1,a+1):
        arr2[i][k]= arr[i-1][k-1]+arr2[i-1][k]+arr2[i][k-1]-arr2[i-1][k-1]
#print(arr2)
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr2[x2][y2]-arr2[x1-1][y2]-arr2[x2][y1-1]+arr2[x1-1][y1-1])

    
