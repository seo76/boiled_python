#https://www.acmicpc.net/problem/12891

"""
import sys
input=sys.stdin.readline

fac=math.factorial

s, p=map(int, input().split())

D=input()

a,c,g,t=map(int, input().split())

st=0
ed=p

Dlist=[]
while ed<=s:
    print(st, ed, D[st:ed])
    #Dlist.append(D[st:ed])
    A, C, G, T=D[st:ed].count('A'),D[st:ed].count('C'),D[st:ed].count('G'),D[st:ed].count('T')
    print(A, C, G, T)
    #A, C, G, T=Dlist[st].count('A'),Dlist[st].count('C'),Dlist.count[st]('G'),Dlist[st].count('T')
    if (a<=A and c<=C and g<=G and t<=T):
        Dlist.append(D[st:ed])
        my_set=set(Dlist)
        print("D",Dlist)
    st +=1
    ed +=1


        
        
        
print("e", len(Dlist))
"""

import sys
input=sys.stdin.readline

s, p=map(int, input().split())

D=input()

a,c,g,t=map(int, input().split())

st=0
ed=p

Dlist=[]
for _ in range(p,s+1):
    A, C, G, T=D[st:ed].count('A'),D[st:ed].count('C'),D[st:ed].count('G'),D[st:ed].count('T')
    if (a<=A and c<=C and g<=G and t<=T):
        Dlist.append(D[st:ed])
        my_set=set(Dlist)
    st +=1
    ed +=1      
        
print(len(Dlist))


