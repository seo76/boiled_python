import pygame, sys
import random
import time
from pygame.locals import *

wid,hei = 768,672 #화면 크기 값 설정
fps = 60 # 초당 프레임수
fpsc = pygame.time.Clock()
pygame.init() #게임 초기화 후 시작
screen = pygame.display.set_mode((wid,hei)) #설정한 값 적용
pygame.display.set_caption("Amen") #게임 이름

#▽이미지 업로드+어떤 크기로 업로딩할건지
n0d = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/캐릭터/n0d.png")
n0d= pygame.transform.scale(n0d,(23,50))
n0u = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/캐릭터/n0u.png")
n0u= pygame.transform.scale(n0u,(23,50))
n0l1 = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/캐릭터/n0l1.png")
n0l1= pygame.transform.scale(n0l1,(20,50))
n0l2 = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/캐릭터/n0l2.png")
n0l2= pygame.transform.scale(n0l2,(20,50))
n0r1 = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/캐릭터/n0r1.png")
n0r1= pygame.transform.scale(n0r1,(20,50))
n0r2 = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/캐릭터/n0r2.png")
n0r2= pygame.transform.scale(n0r2,(20,50))
pray = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/장면/scene1.png")
pray = pygame.transform.scale(pray,(12288,672))
cath = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/장면/성당초안.png")
cath = pygame.transform.scale(cath,(768,672))
g_way = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/장면/길초안.png")
g_way = pygame.transform.scale(g_way,(768,672))
g_board = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/장면/게임판예시.png")
g_board = pygame.transform.scale(g_board,(768,672))
con0 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/게임판-0SE.png")
con0 = pygame.transform.scale(con0,(67,67))
con1 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/게임판-1적.png")
con1 = pygame.transform.scale(con1,(67,67))
con2 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/게임판-2버섯.png")
con2 = pygame.transform.scale(con2,(67,67))
con3 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/게임판-3아이템.png")
con3 = pygame.transform.scale(con3,(67,67))
con4 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/게임판-4일반.png")
con4 = pygame.transform.scale(con4,(67,67))
con5 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/게임판-5뱀의축복.png")
con5 = pygame.transform.scale(con5,(67,67))
dice1 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/주사위1.png")
dice1 = pygame.transform.scale(dice1,(78,22))
dice2 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/주사위2.png")
dice2 = pygame.transform.scale(dice2,(78,22))
dice3 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/주사위3.png")
dice3 = pygame.transform.scale(dice3,(78,22))
dice4 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/주사위4.png")
dice4 = pygame.transform.scale(dice4,(78,22))
dice5 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/주사위5.png")
dice5 = pygame.transform.scale(dice5,(78,22))
dice6 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/주사위6.png")
dice6 = pygame.transform.scale(dice6,(78,22))
dice7 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/주사위7.png")
dice7 = pygame.transform.scale(dice7,(78,22))
dice8 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/주사위8.png")
dice8 = pygame.transform.scale(dice8,(78,22))
dice_b = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/아이콘/주사위판.png")
dice_b = pygame.transform.scale(dice_b,(78,22))







"""―――――――――――――――――――――――――――――――――――――"""
#―――――――――――――――――――――――――――――――――――――――#
"""―――――――――――――――――――――――――――――――――――――"""

def b_move(): #일반 움직임
    global bmy_change, bmx_change, bm_x, bm_y
    
    #방향키만큼 이동
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            bmy_change = bmy_change + 10
            screen.blit(n0d,(bm_x,bm_y))
        elif event.key == pygame.K_UP:
            bmy_change = bmy_change - 10
            screen.blit(n0u,(bm_x,bm_y))
        elif event.key == pygame.K_LEFT:
            bmx_change = bmx_change - 10
            screen.blit(n0l1,(bm_x,bm_y))
        elif event.key == pygame.K_RIGHT:
            bmx_change = bmx_change + 10
            screen.blit(n0r1,(bm_x,bm_y))
        else: 
            screen.blit(n0d,(bm_x,bm_y))
    #▽L과 R키는 이미지변화ㅇ
    elif event.type == pygame.KEYUP:        
        if event.key == pygame.K_DOWN:
            screen.blit(n0d,(bm_x,bm_y))
            bmx_change = 0
            bmy_change = 0
        elif event.key == pygame.K_UP:
             screen.blit(n0u,(bm_x,bm_y))
             bmx_change = 0
             bmy_change = 0
        elif event.key == pygame.K_LEFT: 
            screen.blit(n0l2,(bm_x,bm_y))
            bmx_change = 0
            bmy_change = 0
        elif event.key == pygame.K_RIGHT:
            screen.blit(n0r2,(bm_x,bm_y))
            bmx_change = 0
            bmy_change = 0
        else:
            screen.blit(n0d,(bm_x,bm_y))
    else: #아무상태도 아닐 때 기본이미지
        screen.blit(n0d,(bm_x,bm_y))

    #▽바뀐값을 좌표값에 설정 
    bm_x += bmx_change
    bm_y += bmy_change

bmx_change,bmy_change = 0,0 #변수값 비워두기
bm_x,bm_y = 700,336


def scene1_pray(): #장면전환1
    global pray_x, pray_change, pray_y, shot1

    #사진을 놓는 좌표값을 리턴 키 누를 때 마다 변경
    #장면전환이 끝나면 shot1값=10으로 설정
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            shot1 += 1
            if (shot1 < 16):
                pray_change = pray_change - 768
                screen.blit(pray,(pray_x,pray_y))
            else:
                shot1 = 100
        else:
            pray_change = 0
            screen.blit(pray,(pray_x,pray_y))
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RETURN:
            pray_change = 0
            screen.blit(pray,(pray_x,pray_y))
        else:
            pray_change = 0
            screen.blit(pray,(pray_x,pray_y))
    else:
        screen.blit(pray,(pray_x,pray_y))


    

    pray_x += pray_change    

pray_x,pray_y = 0,0
pray_change = 0
shot1 = 0
        
def cath_cor(): #성당 내에서 좌표제한
    global bmy_change, bmx_change, bm_x, bm_y, shot1, shot2

    if (bm_y < 90):
        bm_y = 90
    if (bm_y > 532):
        bm_y = 532
    
    if (bm_y < 200 or bm_y > 422):
        if (bm_x >= 748):
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT)\
               or(event.type == pygame.KEYUP and event.key == pygame.K_RIGHT):
                bm_x = 748
        if (bm_x <= 136):
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT)\
               or (event.type == pygame.KEYUP and event.key == pygame.K_LEFT):
                bm_x = 136

    if (bm_x < 136):
        if (bm_y < 200):
            bm_y = 200
        if (bm_y > 422):
            bm_y = 422
    if (bm_x < 114):
        if (bm_y < 206):
            bm_y = 204
        if (bm_y > 416):
            bm_y = 418
    if (bm_x < 92):
        if (bm_y < 212):
            bm_y = 210
        if (bm_y > 410):
            bm_y = 412

    if (bm_x < 70):
        bm_x = 70

    #함수가 실행되었던 shot1값을 0으로 두고 shot2를 100으로 변경
    if (bm_x > 768): 
        shot1 = 0
        shot2 = 100
        bm_x = 700    

shot2 = 0

def gway_cor():
    global bmy_change, bmx_change, bm_x, bm_y, shot1, shot2, shot3, jopal

    #함수가 실행되었던 다시 이전장면으로 돌아가고 싶은 경우
    if (bm_x < 0):
        shot2 = 0
        shot1 = 100
        bm_x = 768

    if (bm_x > 768): 
        shot2 = 0
        shot3 = 100
        jopal = 100
        bm_x, bm_y = 23, 9 

shot3 = 0
jopal = 0

def g_move():
    global gmy_change, gmx_change, gm_x, gm_y, gm_pls, step
    g_cor()
    if (step == 100):
        if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_DOWN)):
            screen.blit(n0d,(gm_x,gm_y))
            gmy_change = gmy_change + gm_pls
        elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_DOWN)):
            screen.blit(n0d,(gm_x,gm_y))
            gmx_change = 0
            gmy_change = 0
        else: 
            screen.blit(n0d,(gm_x,gm_y))
            
        if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_UP)):
            screen.blit(n0u,(gm_x,gm_y))
            gmy_change = gmy_change - gm_pls
        elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_UP)):
            screen.blit(n0u,(gm_x,gm_y))
            gmx_change = 0
            gmy_change = 0
        else: 
            screen.blit(n0d,(gm_x,gm_y))

        if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_LEFT)):
            screen.blit(n0l1,(gm_x,gm_y))
            gmx_change = gmx_change - gm_pls
        elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_LEFT)):
            screen.blit(n0l2,(gm_x,gm_y))
            gmx_change = 0
            gmy_change = 0
        else: 
            screen.blit(n0d,(gm_x,gm_y))

        if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_RIGHT)):
            screen.blit(n0r1,(gm_x,gm_y))
            gmx_change = gmx_change + gm_pls
        elif ((event.type == pygame.KEYUP) and (event.key == pygame.K_RIGHT)):
            screen.blit(n0r2,(gm_x,gm_y))
            gmx_change = 0
            gmy_change = 0
        else: 
            screen.blit(n0d,(gm_x,gm_y))

        

        
        gm_x += gmx_change
        gm_y += gmy_change
    

gmx_change,gmy_change = 0,0 #변수값 비워두기
gm_x,gm_y = 23,9
    
def g_cor():
    global gm_x, gm_y
    if gm_x < 23:
        gm_x = 23
        #return 그 전값으로 돌려야됨
    if gm_x > 626: 
        gm_x = 626
    if gm_y < 9:
        gm_y = 9
    if gm_y > 612:
        gm_y = 612


def minigame():
    global c_lst, c_lst2, con_x, con_y, c_num1, c_num2, c_num3, c_num4, c_num5, jopal

    c_lst = []
    con_x = 0
    con_y = 0
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
            
    screen.blit(con0, (c_lst[0]))
    screen.blit(con0, (c_lst[99]))
    c_lst.remove(c_lst[0])
    c_lst.remove(c_lst[98])
        
    if (jopal == 100):
        random.shuffle(c_lst)
        c_lst2 = c_lst
        jopal = 200
    if (jopal == 200):
        screen.blit(n0d,(gm_x,gm_y))
        
    for c_num1 in range (-1, 46, 1):
        c_num1 += 1
        screen.blit(con1, (c_lst2[c_num1]))
    for c_num2 in range (46, 62, 1):
        c_num2 += 1
        screen.blit(con2, (c_lst2[c_num2]))
    for c_num3 in range (62, 78, 1):        
        c_num3 += 1
        screen.blit(con3, (c_lst2[c_num3]))
    for c_num4 in range (78, 93, 1):
        c_num4 += 1
        screen.blit(con4, (c_lst2[c_num4]))
    for c_num5 in range (93, 97, 1):
        c_num5 += 1
        screen.blit(con5, (c_lst2[c_num5]))

c_lst2 = [] #여기로 두니까 오류안나고 실행됨. 왜..?


def dice_sie():
    global ms_x, ms_y, step1, step2, step3, d_n, d_n2
    
    step1 = 0
    step2 = 0
    step3 = 0
    d_n2 = 0
    ms_x = pygame.mouse.get_pos()[0]
    ms_y = pygame.mouse.get_pos()[1]
    
    #DICE#
    if (ms_x > 680 and ms_x < 760)and(ms_y > 226 and ms_y < 248):
        if (event.type == pygame.MOUSEBUTTONDOWN): 
            held_down = True
            screen.blit(dice_b,(681,226))    
        if (event.type == pygame.MOUSEBUTTONUP):
            held_down = False
            d_n2 = random.randint(1,8)
            d_n = d_n2
            
            '''if (ms_y > 531 and ms_y < 551): #save

            if (ms_y > 576 and ms_y < 596): #import'''
    #EXIT#     
    if (ms_x > 680 and ms_x < 760)and (ms_y > 621 and ms_y < 641): 
        if (event.type == pygame.MOUSEBUTTONDOWN): 
            held_down = True
            pygame.quit()
            sys.exit()
d_n = 0

def dice_run():
    global gm_pls, step, step1, step2, step3, jopal, d_n2, d_n
    
    
    if (d_n == 1):
        screen.blit(dice_b,(681,226))
        screen.blit(dice1,(681,226))
        step1 = 100
    if (d_n == 2):
        screen.blit(dice_b,(681,226))
        screen.blit(dice2,(681,226))
        step1 = 100
    if (d_n == 3):
        screen.blit(dice_b,(681,226))
        screen.blit(dice3,(681,226))
        step1 = 100
    if (d_n == 4):
        screen.blit(dice_b,(681,226))
        screen.blit(dice4,(681,226))
        step1 = 100
    if (d_n == 5):
        screen.blit(dice_b,(681,226))
        screen.blit(dice5,(681,226))
        step1 = 100
    if (d_n == 6):
        screen.blit(dice_b,(681,226))
        screen.blit(dice6,(681,226))
        step1 = 100
    if (d_n == 7):
        screen.blit(dice_b,(681,226))
        screen.blit(dice7,(681,226))
        step1 = 100
    if (d_n == 8):
        screen.blit(dice_b,(681,226))
        screen.blit(dice8,(681,226))
        step1 = 100
    jopal = 200
    
    if (step1 == 100):
        if (d_n <= 4):
            gm_pls = 67
            step = 100
        elif (d_n > 4):
            gm_pls = 134
            step = 100
        step1 = 0
            
    if (step == 100):
        g_move()
        jopal = 0        
        step2 = 100
            
    '''if (step2 == 100):
        if ((d_n % 4 == 1)or(d_n % 4 == 2)):
            gm_pls = 67
            step = 100
            step2 = 0
            g_move()
            step3= 100
        elif ((d_n % 4 == 3)or(d_n % 4 == 0)):
            gm_pls = 134
            step = 100
            step2 = 0
            g_move()
            step3= 100
                            
    if (step3 == 100):
        if (d_n % 2 == 1):
            gm_pls = 67
            step = 100
            step3 = 0
            g_move()
        elif (d_n % 2 == 0):
            gm_pls = 134
            step = 100
            step3 = 0
            g_move()'''
            
                
#g_move가 유지되는 조건은 스텝 100이고 함수내에서 스텝값을 0으로 맞추니 종료
#그러나 이 곳의 이프문 조건유지가 계속 되고 움직이는 이프값세개가 동시에 실행됨
step = 0                
    

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        scene1_pray()
        if (shot1 == 100): #cath
            screen.blit(cath,(0,0))
            b_move()
            cath_cor()            
        if (shot2 == 100): #game_way
            screen.blit(g_way,(0,0))
            b_move()
            gway_cor()
        if (shot3 == 100): #minigame
            screen.blit(g_board,(0,0))
            minigame()
            dice_sie()
            dice_run()

        pygame.display.update()
        




