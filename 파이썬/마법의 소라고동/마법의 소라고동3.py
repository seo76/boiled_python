import pygame, sys
import random
import time
import string
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

def writm():
    global mouse, mouse2
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = 100
        if textObj.collidepoint(event.pos):
            mouse2 = 100

mouse = 0
mouse2 = 0
def writ():
    global write, written, writy, textObj, clock, act, actcolor, inactcolor, \
           done, shot1, shot2, txtObj
    shot1 = 0
    shot2 = 100

    screen.blit(que,(0,0))
    writy = pygame.font.SysFont("Arial.ttf",27)
    #write = writy.render(written, True, (255,255,255))
    clock = pygame.time.Clock()
    textObj = pygame.Rect(12, 186, 428, 31)
    actcolor = pygame.Color(255,255,255)
    inactcolor = pygame.Color(180,180,180)
    color = inactcolor
    act = False
    written = " "
    write = " "
    #textObj.center = (220,200)#12,186 부터 w428 h31
    #screen.blit(write,(textObj))
    done = False


    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if textObj.collidepoint(event.pos):
                act = not act
            else:
                act = False
            color = actcolor if act else inactcolor
        if event.type == pygame.KEYDOWN:
            if act:
                #if event.key == pygame.K_RETURN:
                 #   shot1=100
                if event.key == pygame.K_BACKSPACE:
                    write = write[:-1]
                else:
                    write += event.unicode
               

    
    txtObj = writy.render(write, True, color)
    width = max(200, txtObj.get_width()+10)
    textObj.w=width
    screen.blit(txtObj,(textObj.x+5, textObj.y+5))
    pygame.draw.rect(screen,color,textObj,2)


    


    


def Ans():
    global ans, ans2
    if event.type == pygame.KEYUP:
        
        if event.key == pygame.K_RETURN:
            ans = random.randint(1,2)
            ans2 = ans
ans2 = 0
def Ans2():
    global ans, ans2
    if (ans2 == 1):
        screen.blit(yes,(0,0))
    elif (ans2 == 2):
        screen.blit(no,(0,0))
        

while 1:
    writ()
        
    for event in pygame.event.get():
        #writm()
        Ans()
        Ans2()
        #show()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if textObj.collidepoint(event.pos):
                act = not act
            else:
                act = False
            color = actcolor if act else inactcolor
        if event.type == pygame.KEYDOWN:
            if act:
                #if event.key == pygame.K_RETURN:
                 #   shot1=100
                if event.key == pygame.K_BACKSPACE:
                    write = write[:-1]
                else:
                    write += event.unicode

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()     
             
        pygame.display.update()
       
        




