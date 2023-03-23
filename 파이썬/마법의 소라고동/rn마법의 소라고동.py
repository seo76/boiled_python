import pygame, sys
import random
import time
from pygame.locals import *

wid,hei = 450,226 #화면 크기 값 설정
fps = 60 # 초당 프레임수
fpsc = pygame.time.Clock()
pygame.init() #게임 초기화 후 시작
screen = pygame.display.set_mode((wid,hei)) #설정한 값 적용
pygame.display.set_caption("Magical Sora Rhythm") #게임 이름

#▽이미지 업로드+어떤 크기로 업로딩할건지
no = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 과제/마법의 소라고동/no.png")
no= pygame.transform.scale(no,(wid,hei))
yes = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 과제/마법의 소라고동/yes.png")
yes= pygame.transform.scale(yes,(wid,hei))
que = pygame.image.load\
      ("C:/Users/LG/Desktop/파이썬 과제/마법의 소라고동/Q.png")
que= pygame.transform.scale(que,(wid,hei))


def write():
    global write, written, writy, textObj

    writy = pygame.font.SysFont("Arial",25)
    written = input(" ")
    write = writy.render(wirtten,True, BLACK, WHITE)
    textObj = write.get_Rect()
    textObj.center=(220,200)
    screen.blit(write,textObj)

def Ans():
    global ans, ans2

    
    
    if (event.type == pygame.MOUSEBUTTONDOWN): 
        held_down = True
    if (event.type == pygame.MOUSEBUTTONUP):
        held_down = False
        ans = random.randint(1,2)
        ans2 = ans
ans2 = 0

    if (ans2 == 1):
        screen.blit(yes,(0,0))
    elif (ans2 == 2):
        screen.blit(no,(0,0))
    '''if (ans == 1):
        screen.blit(yes,(0,0))
    else:
        screen.blit(no,(0,0))'''
        

    
    
    



            



while 1:
    for event in pygame.event.get():
        screen.blit(que,(0,0))
        Ans()
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        
       
             
        pygame.display.update()
       
        




