import pygame, sys

wid,hei = 768,672
fps = 60 # 초당 프레임수
fpsc = pygame.time.Clock()
pygame.init() #게임 초기화 후 시작
screen = pygame.display.set_mode((wid,hei)) #설정한 값 적용
pygame.display.set_caption("Amen") #게임 이름

prh = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/장면/scene1.png")
prh = pygame.transform.scale(prh,(12288,672))
con0 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/아이콘/게임판-0SE.png")
con0 = pygame.transform.scale(con0,(67,67))


def minigame():
    global c_lst, c_num, con_x, con_y, i

    c_lst = []
    con_x = 0
    con_y = 0
    i = 0
    
    for con_y in range (-67, 603, 67):
        con_y += 67
        for con_x in range (-67, 603, 67):
            con_x += 67
            c_lst.append((con_x,con_y))

    for i in range(7):
        i += 1
        screen.blit(con0,(c_lst[i]))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()#파이게임 종료한다고 신호를 보내면 파이게임 끄고
            sys.exit() #시스템도 끄기
        minigame()

        pygame.display.update()
        screen.blit(prh,(-4608,0))
  
