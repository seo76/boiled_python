icoffee_count = 2500
ccoffee_count = 3000
fcoffee_count = 3000


a = int(input(" 주문할 아메리카노의  잔 수를 입력하시오: "))
b = int(input(" 주문할 카페라떼의 잔 수를  입력하시오: "))
c = int(input(" 주문할 카푸치노의 잔 수를  입력하시오: "))


money = int(input("돈을 넣어주세요: "))

            
change = ((icoffee_count * a)+ (ccoffee_count * b) + (fcoffee_count * c))


if money == change:
    print("거스름돈 없습니다")
    
elif money > change:
    result = money - change
    print("거스름돈은 %d원 입니다." %result)
    
elif money < change:
    print("돈을 더 넣어주세요")
