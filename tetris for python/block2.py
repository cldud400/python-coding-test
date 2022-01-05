import sys, pygame
from backboard2 import *

BLACK = (  0,   0,   0)     #R, G, B
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
blocks = [
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [2, 0, 0, 0],
        [2, 2, 2, 0],
        [0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 3, 0],
        [3, 3, 3, 0],
        [0, 0, 0, 0]
    ],
    [   
        [0, 0, 0, 0],
        [4, 4, 0, 0],
        [0, 4, 4, 0],
        [0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 5, 5, 0],
        [5, 5, 0, 0],
        [0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 6, 6, 0],
        [0, 6, 6, 0],
        [0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 7, 0, 0],
        [7, 7, 7, 0],
        [0, 0, 0, 0]
    ]

]

cell = 0

def setCell(type):
    global cell
    cell = blocks[(type)][:][:]
setCell(0)

def drawBlock(screen, color, currentx, currenty, type):
    for i in range(4):
        for j in range(4):
            if blocks[type][i][j] != 0:
                pygame.draw.rect(screen, GREEN, [(currentx + i * 31), (currenty + j * 31), 30, 30])

def rotate():
    cell[0][0], cell[0][3], cell[3][3], cell[3][0] = cell[3][0], cell[0][0], cell[0][3], cell[3][3]
    cell[0][1], cell[1][3], cell[3][2], cell[2][0] = cell[2][0], cell[0][1], cell[1][3], cell[3][2]
    cell[0][2], cell[2][3], cell[3][1], cell[1][0] = cell[1][0], cell[0][2], cell[2][3], cell[3][1]
    cell[1][1], cell[2][1], cell[2][2], cell[1][2] = cell[2][1], cell[2][2], cell[1][2], cell[1][1]

def isMove(x, y):
    for i in range(4):
        for j in range(4):
            if cell[i][j] != 0:
                if  (i + x < 0) or (j + y < 0) or  (i + x > MAXWIDTH) or (j + y > MAXHEIGHT):
                    return False
                return True

if __name__ == '__main__':
    print(cell)

def BlockCanMove(x, y):
    check = []
    for k in range(4):
        for p in range(4):
            if blocks:
                check = BackGround[y + k][x + p + 1]
    if (check == 0):
        return True
    else:
        return False