import pygame, sys

wid,hei = 512,448 #화면 크기 값 설정

pygame.init() #게임 초기화 후 시작
screen = pygame.display.set_mode((wid,hei)) #설정한 값 적용
pygame.display.set_caption("Amen") #게임 이름

def moving():
    global y_change, x_change, x, y #전역변수 선언
    #▽키보드 누를시의 해당 값으로 해당 수 만큼 이동
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            y_change = y_change + 10
            screen.blit(n0d,(x,y))
        if event.key == pygame.K_UP:
            y_change = y_change - 10
            screen.blit(n0u,(x,y))
        if event.key == pygame.K_LEFT:
            x_change = x_change - 10
            screen.blit(n0l1,(x,y))
        if event.key == pygame.K_RIGHT:
            x_change = x_change + 10
            screen.blit(n0r1,(x,y))
    #▽키보드를 놓을 시 변화 없음        
    elif event.type == pygame.KEYUP:        
        if event.key == pygame.K_DOWN:
            screen.blit(n0d,(x,y))
            x_change = 0
            y_change = 0
        if event.key == pygame.K_UP:
             screen.blit(n0u,(x,y))
             x_change = 0
             y_change = 0
        if event.key == pygame.K_LEFT: #L과 R키는 이미지변화o
            screen.blit(n0l2,(x,y))
            x_change = 0
            y_change = 0
        if event.key == pygame.K_RIGHT:
            screen.blit(n0r2,(x,y))
            x_change = 0
            y_change = 0
            
   # else: #아무상태도 아닐 시 기본이미지(정면) 업로드
       

    elif event.type == pygame.KEYDOWN:
        if not event.key == pygame.K_DOWN and not event.key == pygame.K_UP \
        and not event.key == pygame.K_LEFT and not event.key == pygame.K_RIGHT:
            screen.blit(n0d,(x,y))
            
    elif event.type == pygame.KEYUP:
        if not event.key == pygame.K_DOWN and not event.key == pygame.K_UP \
        and not event.key == pygame.K_LEFT and not event.key == pygame.K_RIGHT:
            screen.blit(n0d,(x,y))

#    else:
#        screen.blit(n0d,(x,y))
   





    x += x_change #체인지변수의 변화값에 따라 x,y값이 설정된 캐릭터좌표값 변경
    y += y_change


x_change,y_change = 0,0 #변수값 비워두기
x,y = 400,224 #캐릭터 초기 좌표값


#▽이미지 업로드+어떤 크기로 업로딩할건지
n0d = pygame.image.load("C:/Users/LG/Desktop/파이썬 던전/적용이미지/n0d.png")
n0d= pygame.transform.scale(n0d,(23,50))
n0u = pygame.image.load("C:/Users/LG/Desktop/파이썬 던전/적용이미지/n0u.png")
n0u= pygame.transform.scale(n0u,(23,50))
n0l1 = pygame.image.load("C:/Users/LG/Desktop/파이썬 던전/적용이미지/n0l1.png")
n0l1= pygame.transform.scale(n0l1,(20,50))
n0l2 = pygame.image.load("C:/Users/LG/Desktop/파이썬 던전/적용이미지/n0l2.png")
n0l2= pygame.transform.scale(n0l2,(20,50))
n0r1 = pygame.image.load("C:/Users/LG/Desktop/파이썬 던전/적용이미지/n0r1.png")
n0r1= pygame.transform.scale(n0r1,(20,50))
n0r2 = pygame.image.load("C:/Users/LG/Desktop/파이썬 던전/적용이미지/n0r2.png")
n0r2= pygame.transform.scale(n0r2,(20,50))
bg = pygame.image.load("C:/Users/LG/Desktop/파이썬 던전/적용이미지/예수.png")
bg = pygame.transform.scale(bg,(512,448))



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
    #물체 피하기(연두의자)
    if 32 <= y < 199:
        if 405< x <465:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x = 405
                if event.key == pygame.K_LEFT:
                    x = 465

    if 405 < x < 465:
       if 32 < y < 199:
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_UP:
                    y = 199
            

        
        




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()#파이게임 종료한다고 신호를 보내면 파이게임 끄고
            sys.exit() #시스템도 끄기
        moving() #if함수 적용이 안된다면 무빙과 노노함수 적용
        nono()
                
        pygame.display.update()
        #▽스크린에 해당 좌표값으로 이미지 업로드.
        screen.blit(bg,(0,0))
        
