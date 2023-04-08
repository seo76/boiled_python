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

"""

import sys
from collections import deque
input=sys.stdin.readline

s, p=map(int, input().split())

D=input()

a,c,g,t=map(int, input().split())

Dlist=[0,0,0,0]
Dlist[0]=a
Dlist[1]=c
Dlist[2]=g
Dlist[3]=t

cnt=0
#st=0
#ed=p


sw=''
ew=''
dq = deque()
def pbox(inp, sz):
    global sw, ew
    dq.append(inp)
    ew=dq[-1]
    if len(dq)>sz:
        sw=dq[0]
        dq.popleft()
    return sw, ew

for i in D:
    i=i.strip()
    pbox(i,p)
    if (sw=='A'):
        Dlist[0]+=1
    elif (sw=='C'):
        Dlist[1]+=1
    elif (sw=='G'):
        Dlist[2]+=1
    else:
        Dlist[3]+=1

    if (ew=='A'):
        Dlist[0]-=1
    elif (ew=='C'):
        Dlist[1]-=1
    elif (ew=='G'):
        Dlist[2]-=1
    else:
        Dlist[3]-=1

    if (a<=Dlist[0] and c<=Dlist[1] and g<=Dlist[2] and t<=Dlist[3]):
        cnt+=1

print(cnt)

"""


for i in range(s-1):
    Dlist




    A, C, G, T=D[st:ed].count('A'),D[st:ed].count('C'),D[st:ed].count('G'),D[st:ed].count('T')
    if (a<=A and c<=C and g<=G and t<=T):
        Dlist.append(D[st:ed])
        my_set=set(Dlist)
    st +=1
    ed +=1      
        
print(len(Dlist))

"""






