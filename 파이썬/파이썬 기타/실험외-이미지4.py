import pygame, sys
from pygame.locals import *


wid,hei = 768,672 #화면 크기 값 설정


pygame.init() #게임 초기화 후 시작
screen = pygame.display.set_mode((wid,hei)) #설정한 값 적용
pygame.display.set_caption("Amen") #게임 이름
keyget = pygame.key.get_pressed()

def g_move():
    global gmy_change, gmx_change, gm_x, gm_y, gm_pls, gm_cnt
    gm_cnt = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            gmy_change = gmy_change + gm_pls
            screen.blit(n0d,(gm_x,gm_y))
        elif event.key == pygame.K_UP:
            gmy_change = gmy_change - gm_pls
            screen.blit(n0u,(gm_x,gm_y))
        elif event.key == pygame.K_LEFT:
            gmx_change = gmx_change - gm_pls
            screen.blit(n0l1,(gm_x,gm_y))
        elif event.key == pygame.K_RIGHT:
            gmx_change = gmx_change + gm_pls
            screen.blit(n0r1,(gm_x,gm_y))
        else: 
            screen.blit(n0d,(gm_x,gm_y))
    elif event.type == pygame.KEYUP:        
        if event.key == pygame.K_DOWN:
            screen.blit(n0d,(gm_x,gm_y))
            gmx_change = 0
            gmy_change = 0
            gm_cnt += 1
        elif event.key == pygame.K_UP:
             screen.blit(n0u,(gm_x,gm_y))
             gmx_change = 0
             gmy_change = 0
             gm_cnt += 1
        elif event.key == pygame.K_LEFT: 
            screen.blit(n0l2,(gm_x,gm_y))
            gmx_change = 0
            gmy_change = 0
            gm_cnt += 1
        elif event.key == pygame.K_RIGHT:
            screen.blit(n0r2,(gm_x,gm_y))
            gmx_change = 0
            gmy_change = 0
            gm_cnt += 1
        else:
            screen.blit(n0d,(gm_x,gm_y))
    else: #아무상태도 아닐 때 기본이미지
        screen.blit(n0d,(gm_x,gm_y))
    
        
    gm_x += gmx_change
    gm_y += gmy_change

    return 0
    

gmx_change,gmy_change = 0,0 #변수값 비워두기
gm_x,gm_y = 23,9






x_change,y_change = 0,0 #변수값 비워두기
x,y = 200,300 #캐릭터 초기 좌표값


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
bg = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 느그멘/적용이미지/배경/이동과정 예시.png")
bg = pygame.transform.scale(bg,(wid,hei))


'''
def nono():#캐릭터 좌표제한을 함수
    global x,y 

    if x < 0:
        x = 0
    if x > 482:
        x = 482
    if y < 32:
        y = 32
    if y > 353:
        y = 353
'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()#파이게임 종료한다고 신호를 보내면 파이게임 끄고
                sys.exit() #시스템도 끄기
        elif event.type == pygame.QUIT:
            pygame.quit()#파이게임 종료한다고 신호를 보내면 파이게임 끄고
            sys.exit()
        g_move() #if함수 적용이 안된다면 무빙과 노노함수 적용
        gm_pls = 67 
        pygame.display.update()
        #▽스크린에 해당 좌표값으로 이미지 업로드.
        screen.blit(bg,(0,0))
        
