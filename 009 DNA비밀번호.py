#https://www.acmicpc.net/problem/12891
import sys
input=sys.stdin.readline

s, p=map(int, input().split())

D=input()

a,c,g,t=map(int, input().split())

A, C, G, T=D.count('A'),D.count('C'),D.count('G'),D.count('T')

if (a>A or c>C or g>G or t>T):
    print(":)")
