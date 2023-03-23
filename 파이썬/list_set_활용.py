print("양의 정수 네 개를 입력하시오")
n1, n2, n3, n4= map(int, input().split())
lista=[n1, n2, n3, n4]
L3=[]
L4=[]


print("최소값:",min(lista), "최대값:", max(lista))

for i in range(0,max(lista)+1,3):
    if (min(lista) <= i):
        L3.append(i)
print("L3=",L3)

for i in range(0,max(lista)+1,4):
    if (min(lista) <= i):
        L4.append(i)
print("L4=",L4)

s1=set(L3)
s2=set(L4)

print("L5",s1&s2)
print("L6",s1|s2)
