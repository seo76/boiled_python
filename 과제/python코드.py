filename="python.txt"
"""
f =open(filename,'r')
rln=f.read()
c= rln.count("\n")
f.closed
for i in range(c):
    f =open(filename,'r')
    rl=f.read()
    rlist=list(map(str,rl.split("\n")))
f.closed
print(rlist)
"""

rlist=[]
Plist=[]
c=0
with open(filename,"r") as file:
    for line in file:
        rlist.append(line.strip("\n"))
        c+=1

for i in range(c):
    rl=rlist[i]
    cont = rl
    leng = len(rl)
    capt = sum(a.isupper() for a in rl)
    lc = sum(a.islower() for a in rl)
    dc = sum(a.isdigit() for a in rl)
    schr = leng-capt-lc-dc
    print(cont, leng, capt, schr)
"""
print(Plist)

    

class output:
    def __init__(self, cont, leng, capt, schr):
        self.cont=cont
        self.leng=leng
        self.capt=capt
        self.schr=schr

    def content(self):
        while (i<c):
            for i in range (c):
                cont = 
"""

    
"""
    def __init__(self, cont, leng, capt, schr):
        self.cont=cont
        self.leng=len(rlist[1])#=leng
        self.capt=len(rlist[1])#=capt
        self.schr=len(rlist[1])#=schr

    def content(self, cont):
        self.cont = rlist[cont]

a=Data()
print(a.content(1))
"""
'''    return print(self.leng, self.capt, self.schr, self.cont)

    def output(self):
        print(self.leng, self.capt, self.schr, self.cont)


Data.rt()
#print(b)
'''

















"""


for i in range

class Data():
    f =open(filename,'r')
    rl=f.readlines()

    def cont(self,c):
        return self.rl[c]

a=Data.cont(3)
print(a)


    def sturct(self, cont, leng, capt, schr):
        self.cont=rl
        self.leng=len(rl)
        self.capt=len(rl)
        self.schr=len(rl)
"""



"""



    cont: str =None
    leng:int =None
    capt: int =None
    schar: int =None

test=Struct()

#a=f.readline()
test.leng=len(a)

print(test.leng)
"""
