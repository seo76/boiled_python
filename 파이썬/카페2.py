print("아메리카노, 카페라떼, 카푸치노의 잔 수를 입력하시오.")

c1, c2, c3 = map(int, input().split())

c_total = 2500*c1 + 3000*c2 + 3000*c3

money = int(input("총 %d원입니다.현금을 넣어주세요: "%c_total))

if money == c_total:
    print("음료가 준비되면 진동벨로 알려드리겠습니다.")
    
elif money > c_total:
    charge = money - c_total
    print("거스름돈 %d원 입니다." %charge)
    
elif money < change:
    lack = c_tota - money
    print("%d원이 부족합니다."%lack)












