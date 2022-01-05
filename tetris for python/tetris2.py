import sys, pygame
from block2 import *
from backboard2 import *

pygame.init()

size = width, height = 398, 802
BLACK = (  0,   0,   0)     #R, G, B
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
x = 120
y = 0
currentx = 3
currenty = 0

clock = pygame.time.Clock()
speed = 0

screen = pygame.display.set_mode(size)      #pygame 라이브러리 추가

delay = 200
interval = 50
pygame.key.set_repeat(delay, interval)

while 1:
    backBoard()
    speed += clock.get_rawtime()
    clock.tick()
    if speed / 1000 > 0.5:
        speed = 0
        y += 31
        currenty  += 1
        if not isMove(currentx, currenty):
            y -= 31
            currenty -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if BlockCanMove(currentx, y):
                    currentx -= 1
            #    if isMove(currentx ,currenty):
            #         x += 31
            #         currentx += 1
            #         if not isMove(currentx ,currenty):
            #             x -= 31
            #             currentx -= 1
            elif event.key == pygame.K_LEFT:
                if BlockCanMove(currentx +1, currenty):
                    currentx += 1
                
                # if isMove(currentx ,currenty):
                #     x -= 31
                #     currentx -= 1
                #     if not isMove(currentx ,currenty):
                #         x += 31
                #         currentx += 1
            elif event.key == pygame.K_UP:
                rotate()
                if not isMove(currentx , currenty):
                    for _ in range(3):
                        rotate()
            elif event.key == pygame.K_DOWN:
                if isMove(currentx, currenty):
                    y += 31
                    currenty += 1
                    if not isMove(currentx ,currenty):
                        y -= 31
                        currenty -= 1
            elif event.key == pygame.K_SPACE:
                if isMove(currentx, currenty):
                    pass


    
    screen.fill(WHITE)
    drawBlock(screen, GREEN, x, y, 0)
    pygame.display.flip()

    

    # def LeftMove():
    #     if BlockCanMove(currentx, y):
    #        currentx -= 1

    # def RightMove():
    #     if BlockCanMove(currentx +1, currenty):
    #         currentx += 1
