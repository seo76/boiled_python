start=0
print("====================\n        MENU    \n====================\n1. 덧셈\n2. 뺄셈\n3. 곱셈\n4. 나눗셈\n5. 나머지")
def calculator():
    global a,b,z
    
    a=int(input("숫자1:"))
    b=int(input("숫자2:"))
    if (z==1):
        print(a+b)
    if (z==2):
        print(a-b)
    if (z==3):
        print(a*b)
    if (z==4):
        print(a/b)
    if (z==5):
        print(a%b)

while (start == 0):
    z=int(input("원하는 메뉴를 선택하시오(1-5):"))
    if (z > 0 and z<6):
        calculator()
        start = 1
        restart=input("y키를 눌러 계속하시오:")
        if (restart == 'y'):
            start = 0
        if not(restart == 'y'):
            print("종료합니다.")
    if not(z > 0 and z<6):
        print("잘못누르셨습니다.")

        


   







