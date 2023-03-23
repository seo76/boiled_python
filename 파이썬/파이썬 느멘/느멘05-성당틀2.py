import pygame, sys
from pygame.locals import *

wid,hei = 768,672 #화면 크기 값 설정
fps = 60 # 초당 프레임수
fpsc = pygame.time.Clock()
pygame.init() #게임 초기화 후 시작
screen = pygame.display.set_mode((wid,hei)) #설정한 값 적용
pygame.display.set_caption("Amen") #게임 이름

#▽이미지 업로드+어떤 크기로 업로딩할건지
n0d = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/캐릭터/n0d.png")
n0d= pygame.transform.scale(n0d,(23,50))
n0u = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/캐릭터/n0u.png")
n0u= pygame.transform.scale(n0u,(23,50))
n0l1 = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/캐릭터/n0l1.png")
n0l1= pygame.transform.scale(n0l1,(20,50))
n0l2 = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/캐릭터/n0l2.png")
n0l2= pygame.transform.scale(n0l2,(20,50))
n0r1 = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/캐릭터/n0r1.png")
n0r1= pygame.transform.scale(n0r1,(20,50))
n0r2 = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/캐릭터/n0r2.png")
n0r2= pygame.transform.scale(n0r2,(20,50))
pray = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/장면/scene1.png")
pray = pygame.transform.scale(pray,(12288,672))
cath = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/장면/성당초안.png")
cath = pygame.transform.scale(cath,(768,672))

def b_move(): #일반 움직임
    global bmy_change, bmx_change, bm_x, bm_y
    cath_cor()
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
bm_x,bm_y = 200,200


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
        
def cath_cor():
    global bmy_change, bmx_change, bm_x, bm_y, cir_x1, cir_x2, cir_y1, cir_y2, cir_y, y_nom

    cir_y_lst()
    
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
               
    
    if (((bm_x - 136)*(bm_x - 136))+((bm_y - 336)*(bm_y - 336)) > (141*141)\
        and ((bm_x < 136) and (bm_y < 336))):
        if event.type == pygame.KEYUP:
            ((bm_x - 136)*(bm_x - 136))+((bm_y - 336)*(bm_y - 336)) = (141*141)
            
            '''cir_x1 = 0
            cir_y1 = 0
            while cir_x1 < 136:
                cir_x1 += 1
                cir_y1 += 1
                if (((cir_x1 - 136)*(cir_x1 - 136))+((bm_y- 336)*(bm_y - 336)))\
                   <= 141*141 or 138*138 <=\
                   (((cir_x1 - 136)*(cir_x1 - 136))+((bm_y - 336)*(bm_y - 336))):
                    
                    if (((bm_x - 136)*(bm_x - 136))+((cir_y1- 336)*(cir_y1 - 336)))\
                       <= 141*141 or 138*138 <=\
                       (((bm_x - 136)*(bm_x - 136))+((cir_y1 - 336)*(cir_y1 - 336))):
                        bm_x, bm_y = cir_x1, cir_y1

    if (((bm_x - 136)*(bm_x - 136))+((bm_y - 286)*(bm_y - 286)) > (141*141)\
        and ((bm_x < 136) and (bm_y > 336))):
        if event.type == pygame.KEYUP:
            cir_x2 = 0
            while cir_x2 < 136:
                cir_x2 += 1
                if (((cir_x2 - 136)*(cir_x2 - 136))+((bm_y - 286)*(bm_y - 286)))\
                   <= 141*141 or 138*138 <=\
                   (((cir_x2 - 136)*(cir_x2 - 136))+((bm_y - 286)*(bm_y - 286))):
                    bm_x, bm_y = cir_x2, bm_y
'''           
           
            

def cir_y_lst():
    global cir_y, y_nom

    cir_y = []
    y_nom = 200

    while y_nom < 472:
        y_nom += 1
        cir_y.append(y_nom)




            




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        b_move()
        #캐릭터 기본움직임
        '''if (shot1 == 100):
            screen.blit(cath,(0,0))
            b_move()'''
             
        pygame.display.update()
        screen.blit(cath,(0,0))
       
        




