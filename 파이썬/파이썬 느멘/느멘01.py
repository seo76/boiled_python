import pygame, sys

def moving():
    global y_change, x_change, x, y
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            y_change = y_change + 10
        if event.key == pygame.K_UP:
            y_change = y_change - 10
        if event.key == pygame.K_LEFT:
            x_change = x_change - 10
        if event.key == pygame.K_RIGHT:
            x_change = x_change + 10
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN or \
            event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0
            y_change = 0
    x += x_change
    y += y_change

def nono():
    global x,y

    if x < 0:
        x = 0
    if x > 512:
        x = 512
    elif y < 0:
        y = 0
    elif y > 330:
        y = 330

color = (255,255,255)
wid,hei = 512,448

pygame.init()
screen = pygame.display.set_mode((wid,hei))
pygame.display.set_caption("Amen")

x_change,y_change = 0,0
x,y = 236,330

Amen = pygame.image.load("C:/Users/LG/Desktop/파이썬 던전/적용이미지/주인공 수녀-앞 30 62.png")
bg = pygame.image.load("C:/Users/LG/Desktop/파이썬 던전/이미지/bgbg.png")
Amen = pygame.transform.scale(Amen,(30,62))
bg = pygame.transform.scale(bg,(512,448))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        moving()
        nono()
                
        pygame.display.update()
        screen.fill(color)
        screen.blit(bg,(0,0))
        screen.blit(Amen,(x,y))
