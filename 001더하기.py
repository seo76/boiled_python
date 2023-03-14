
"""
i = -5

while True:
    try:
        i = int(input("1-100사이의 숫자를 입력하세요\n"))
        if(i < 0 or i > 100):
            print ("올바른 숫자를 입력하세요")
        if(i>0 and i<101):
            break
    except ValueError:
        print("숫자가 뭔지 몰라?\n")
    

print(i,"부터 내림차순으로 숫자를 정렬하겠습니다. \n")
for i in range (i,0,-1):
    print(i)


while True:
    try:
        a, b, c, d, e = map(int,input("숫자 다섯 개를 입력하세요(띄어쓰기로 구분)\n").split())
        break
    except ValueError:
        print("숫자 다섯 개를 입력하세요!\n")

"""

"""
#N개의 숫자가 공백없이 있을 때, 각 숫자의 합을 구하여라

i = []
sum = 0

i = input("띄어쓰기 구분 없이 숫자를 입력하세요\n")

for j in range (len(i)):
    
    sum = sum+int(i[j])

print(sum)
"""

#N개의 숫자가 공백없이 있을 때, 각 숫자의 합을 구하여라2

i = []
sum = 0

i = input("띄어쓰기 구분 없이 숫자를 입력하세요\n")

for j in range (len(i)):

    if (i[j].isdecimal()):
        sum = sum+int(i[j])

print(sum)



"""

i = []
sum = 0


i = input("띄어쓰기 구분 없이 숫자를 입력하세요\n")


if (i.isdigit()==False):
    while True:
        print("선생님.. 숫자요..\n")
        i = input("띄어쓰기 구분 없이 숫자를 입력하세요\n")
        if (i.isdigit()==True):
            break

    
for j in range (len(i)):
    sum = sum+int(i[j])

print(sum)
"""


