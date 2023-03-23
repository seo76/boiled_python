import random

c_lst = []
c_lst2 = []
con_x = 0
con_y = 0
jopal = 100
c_num1 = 0
c_num2 = 0
c_num3 = 0
c_num4 = 0
c_num5 = 0
    
for con_y in range (0, 604, 67):
        con_y += 1
        for con_x in range (0, 604, 67):
            con_x += 1
            c_lst.append((con_x,con_y))
c_lst.remove(c_lst[0])
c_lst.remove(c_lst[98])



c_lst2 = []
    
if (jopal == 100):
        random.shuffle(c_lst)
        c_lst2 = c_lst
        jopal = 0

for c_num1 in range (-1, 46, 1):
        c_num1 += 1
        print(c_lst2[c_num1])

