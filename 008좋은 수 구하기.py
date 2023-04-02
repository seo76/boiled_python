"""
n=int(input())
l =list(map(int,input().split()))
l.append(0)

l.sort()
temp, k, cnt= 0,0,0

for i in range(n-1):
    i +=1
    for j in range(i,n-1):
        j +=1
        temp = l[i]+l[j]
        k = j
        while k<n:
            k +=1
            if (temp == l[k]):
                cnt +=1
                print(i, j, k)
                break
    

print(cnt)

"""
"""
import sys
input = sys.stdin.readline

n=int(input())
l =list(map(int,input().split()))
l.append(0)
l.sort()
temp, k, cnt= 0,0,[]

for i in range(n-1):
    i +=1
    for j in range(i,n-1):
        j +=1
        temp = l[i]+l[j]
        k = j
        while k<n:
            k +=1
            if (temp == l[k]):
                cnt.append(k)
                break
    

print(len(set(cnt)))
"""
"""
import sys
input = sys.stdin.readline

n=int(input())
l =list(map(int,input().split()))
l.append(0)
l.sort()
temp, cnt= 0,0
k = n+1

for _ in range(n):
    k -=1
    b = n
    a = 1
    while a<b:
        temp=l[a]+l[b]
        if (temp==l[k]):
            print("=",a,b,l[k],l[a]+l[b])
            cnt+=1
            break
        elif (temp<l[k]):
            print("<",a,b,l[k],l[a]+l[b])
            a +=1
            temp=l[a]+l[b]
        else:
            print(">",a,b,l[k],l[a]+l[b])
            b -=1
            temp=l[a]+l[b]


print(cnt)
        
"""



import sys
input = sys.stdin.readline

n=int(input())
l =list(map(int,input().split()))
#l.append()
l.sort()
temp, cnt= 0,0
n=n-1
k = n+1

for _ in range(n):
    k -=1
    b = n
    a = 0
    while a<b:
        temp=l[a]+l[b]
        if (temp==l[k]):
            cnt+=1
            print("=",a,b,k, l[a], l[b], l[k])
            break
        elif (temp<l[k]):
            print("ㅈ",a,b,k, l[a], l[b], l[k])
            a +=1           
        else:
            print("ㅋ",a,b,k, l[a], l[b], l[k])
            b -=1
            

print("c:", cnt)
        
"""

import sys
input = sys.stdin.readline

n=int(input())
l =list(map(int,input().split()))
l.sort()
temp, cnt= 0,0
n=n-1
k = n+1

for _ in range(n):
    k -=1
    b = n
    a = 0
    while a<b:
        temp=l[a]+l[b]
        if (temp==l[k]):
            cnt+=1
            break
        elif (temp<l[k]):
            a +=1           
        else:
            b -=1
            

print(cnt)

"""
