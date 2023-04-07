#https://www.acmicpc.net/problem/12891
import sys
import math
input=sys.stdin.readline

fac=math.factorial

s, p=map(int, input().split())

D=input()

a,c,g,t=map(int, input().split())

A, C, G, T=D.count('A'),D.count('C'),D.count('G'),D.count('T')

if (a>A or c>C or g>G or t>T):
    ans = 0
else:
    if(p==a+c+g+t):
        ans=fac(p)/fac(a)/fac(c)/fac(g)/fac(t)
    else:
        
        
        
print(ans)
