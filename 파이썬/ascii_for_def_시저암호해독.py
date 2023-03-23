


def decryption():
    n1 = int(input('a로부터 얼마나 떨어져있는지 숫자로 쓰시오.'))
    d = input('복호화 할 문자를 소문자로 쓰시오.')

    for dtoa in d:
        de = ord(dtoa)-n1



        if (de < 97):
            de = (ord(dtoa)-n1)+26
        if (ord(dtoa)==32):
            de = 32
                 
        print (chr(de), end="")
        

def encryption():
    n2 = int(input('a로부터 얼마나 떨어뜨릴 지 숫자로 쓰시오.'))
    e = input('암호화 할 문자를 소문자로 쓰시오.')

    for etoa in e:
        en = ord(etoa)+n2
        
        if (en > 122):
            en = 96+(ord(etoa)+n2-122)
        if (ord(etoa)==32):
            en = 32
        
        print (chr(en), end="")


a = input("무엇을 할 지 선택하시오.(암호화=e/복호화=d)")

if (a=='e'):
    encryption()
    
if (a=='d'):
    decryption()


