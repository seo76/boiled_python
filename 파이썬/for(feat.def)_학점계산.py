x=int(input("점수입력:"))


def score():
    if 0<x<60:
         print("F")
    elif 60<= x <=69:
        print("D")
    elif 70<= x <=79:
        print("C")
    elif 80<= x <= 89:
        print("B")
    elif 90<= x <=100:
        print("A")



if x<0 or x>100:
    x=int(input("잘못입력함:"))
    score()
else:
    score()
