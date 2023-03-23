print("두 수를 입력하시오")
n1, n2= map(int, input().split())
m1 = n1
m2 = n2

totalf = 0
totalw = 0

for i in range(n2-n1+1):
    totalf += n1
    n1 = n1 + 1

while (m1<=m2):
    totalw += m1
    m1 = m1 + 1


print("for 이용:",totalf)
print("while 이용:",totalw)
