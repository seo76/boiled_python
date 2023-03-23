import pygame, sys

wid,hei = 768,672
fps = 60 # 초당 프레임수
fpsc = pygame.time.Clock()
pygame.init() #게임 초기화 후 시작
screen = pygame.display.set_mode((wid,hei)) #설정한 값 적용
pygame.display.set_caption("Amen") #게임 이름

g_board = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/장면/게임판예시.png")
g_board = pygame.transform.scale(g_board,(768,672))
con0 = pygame.image.load \
      ("C:/Users/LG/Desktop/파이썬 던전/적용이미지/아이콘/게임판-0SE.png")
con0 = pygame.transform.scale(con0,(67,67))


def jodgatne():
    global rect1, x, y, lst

    lst=['con0,(700,60)']
    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    rect1 = pygame.draw.rect(screen,(255,255,255),[680,226,80,22])
    if (x > 680 and x < 760):
        if (event.type == pygame.MOUSEBUTTONDOWN):
            screen.blit(lst[1])

x,y = 0,0    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()#파이게임 종료한다고 신호를 보내면 파이게임 끄고
            sys.exit() #시스템도 끄기
        jodgatne()

        pygame.display.update()
        screen.blit(g_board,(0,0))
