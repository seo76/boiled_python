class CharClass:
    a = ['Seoul','Kyeongi','Inchon','Daejeon','Daegu','Pusan'];
myVar = CharClass()
srt01 = ''
for i in myVar.a:
    str01 = srt01+i[2]
print(str01)
