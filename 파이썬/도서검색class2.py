class Book:  #클래스 선언, 밑은 문자열 선언
    name = ''
    author= ''
    pblsh= ''
    price= ''
    pyear= ''

    def init(self, name, author, pblsh, price, pyear): #정보를 입력받을 메서드
        self.name = name
        self.author = author
        self.pblsh = pblsh
        self.price = price
        self.pyear = pyear

    def getName(self): #각각 정보를 얻을 메서드
        return self.name

    def getAuthor(self):
        return self.author

    def getPBlsh(self):
        return self.pblsh

    def getPRice(self):
        return self.price

    def getPYear(self):
        return self.pyear
    
book1 = Book() #변수에 Book인스턴스 할당
book2 = Book()
book3 = Book()
book4 = Book()
book5 = Book()
book6 = Book()
book7 = Book()

book1.init('안드로이드앱개발','최전산','PCB','25000','2017')
book2.init('파이썬','강수라','연두','22000','2019')
book3.init('자바스크립트','박정식','SSS','23000','2018')
book4.init('HTML5','주환','대한','27500','2012')
book5.init('컴파일러','장진웅','PCB','19500','2011')
book6.init('C언어','홍말숙','한국','22000','2010')
book7.init('프로그래밍언어','현정숙','연두','15000','2019')
j=0

print('도서검색키워드\n1.도서명\n2.저자명\n3.출판사명')
search=int(input("선택(1,2,3):"))

if search == 1:
    search_1 = input("도서명을 입력하세요.")

    for i in range(1,8):
        book = globals()['book{}'.format(i)]
        if book.getName() == search_1:
            print(book.getName()+'\n'+book.getAuthor()+'\n'+book.getPRice())
        if not book.getName() == search_1:
            j += 1
        if j == 7:
            print("도서를 찾을 수 없습니다.")


if search == 2:
    search_1 = input("저자명을 입력하세요.")

    for i in range(1,8):
        book = globals()['book{}'.format(i)]
        if book.getAuthor() == search_1:
            print(book.getName()+'\n'+book.getAuthor()+'\n'+book.getPRice())
        if not book.getAuthor() == search_1:
            j += 1
        if j == 7:
            print("도서를 찾을 수 없습니다.")

if search == 3:
    search_1 = input("출판사명을 입력하세요.")

    for i in range(1,8):
        book = globals()['book{}'.format(i)]
        if book.getPBlsh() == search_1:
            print(book.getName()+'\n'+book.getAuthor()+'\n'+book.getPRice())
        if not book.getPBlsh() == search_1:
            j += 1
        if j == 7:
            print("도서를 찾을 수 없습니다.")





            
