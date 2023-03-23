book1 = {'이름':'안드로이드앱개발','저자':'최전산','출판사':'PCB','가격':'25000','출판연도':'2017'}
book2 = {'이름':'파이썬','저자':'강수라','출판사':'연두','가격':'22000','출판연도':'2019'}
book3 = {'이름':'자바스크립트','저자':'박정식','출판사':'SSS','가격':'23000','출판연도':'2018'}
book4 = {'이름':'HTML5','저자':'주환','출판사':'대한','가격':'27500','출판연도':'2012'}
book5 = {'이름':'컴파일러','저자':'장진웅','출판사':'PCB','가격':'19500','출판연도':'2011'}
book6 = {'이름':'C언어','저자':'홍말숙','출판사':'한국','가격':'22000','출판연도':'2010'}
book7 = {'이름':'프로그래밍언어','저자':'현정숙','출판사':'연두','가격':'15000','출판연도':'2019'}
j=0

print('도서검색키워드\n1.도서명\n2.저자명\n3.출판사명')
print(book1["이름"])
search=int(input("선택(1,2,3):"))


if search == 1:
    search_1 = input("도서명을 입력하세요.")

    for i in range(1,8):
        if globals()['book{}'.format(i)]["이름"] == search_1:
            print(globals()['book{}'.format(i)])
        if not globals()['book{}'.format(i)]["이름"] == search_1:
            j += 1
        if j == 7:
            print("도서를 찾을 수 없습니다.")

if search == 2:
    search_1 = input("저자명을 입력하세요.")

    for i in range(1,8):
        if globals()['book{}'.format(i)]["저자"] == search_1:
            print(globals()['book{}'.format(i)])
        if not globals()['book{}'.format(i)]["저자"] == search_1:
            j += 1
        if j == 7:
            print("도서를 찾을 수 없습니다.")
            
if search == 3:
    search_1 = input("출판사명을 입력하세요.")

    for i in range(1,8):
        if globals()['book{}'.format(i)]["출판사"] == search_1:
            print(globals()['book{}'.format(i)])
        if not globals()['book{}'.format(i)]["출판사"] == search_1:
            j += 1
        if j == 7:
            print("도서를 찾을 수 없습니다.")            
        
