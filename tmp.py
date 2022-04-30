import pygame
import time
from pandas import *
pygame.init()

ROBOT_COLOR = (240, 240, 240)
BACKGROUND_COLOR = (200, 219, 199)
RED = (240, 0, 0)
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
ROBOT_RADIUS = 20

dis_width = 400
dis_height = 300
dis = pygame.display.set_mode(size=(dis_width, dis_height))

pygame.display.update()
pygame.display.set_caption("Robot Vacuum Cleaner Simulation by Tamas Levay")


rows = int(dis_width / ROBOT_RADIUS)
cols = int(dis_height / ROBOT_RADIUS)


#matrix = [[0]*cols]*rows
matrix = [ [0] * 5 for i1 in range(6) ]

matrix[4][4] = 1
matrix[3][3] = 1
#
# x=0
# y=0
# for row in matrix:
#     for col in row:
#         box = pygame.Rect(x,y,ROBOT_RADIUS, ROBOT_RADIUS)
#         pygame.draw.rect(dis, (255,255,255), box)
#         x += ROBOT_RADIUS
#     y += ROBOT_RADIUS
#     x = 0
def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(rows):
        for y in range(cols):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(dis, WHITE, rect, 1)

def drawObstacle(obstacle):
    block_size = 20
    rect = pygame.Rect(block_size, block_size, block_size, block_size)
    pygame.draw.rect(dis, RED, rect, 10)


# def drawMatrix(elem):
#     block_size = 20
#     rect = pygame.Rect(block_size, block_size, block_size, block_size)
#     if elem == 1:
#         pygame.draw.rect(dis, RED, rect, 10)
#         print('HELLO')




def drawRobot():
    pygame.draw.ellipse(dis, ROBOT_COLOR, [x1, y1, ROBOT_RADIUS, ROBOT_RADIUS])

x1 = dis_width/2
y1 = dis_height/2


x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])


def detect_wall():
    if x1 >= dis_width - ROBOT_RADIUS or x1 < ROBOT_RADIUS or y1 >= dis_height - ROBOT_RADIUS or y1 < ROBOT_RADIUS:
        return True
    else:
        return False

def move_left():
    global  x1_change
    x1_change = -ROBOT_RADIUS


def move_right():
    if not detect_wall():
        global x1_change
        x1_change = ROBOT_RADIUS

def move_down():
    global  y1_change
    y1_change = -ROBOT_RADIUS

simulation_over = False

while not simulation_over:
    drawGrid()
    for event in pygame.event.get():

        if event.type ==pygame.QUIT:
            simulation_over = True

    x1 += x1_change
    y1 += y1_change
    #dis.fill(BACKGROUND_COLOR)
    drawRobot()
    #elem = 1
    #drawObstacle(matrix[5][5])
    drawObstacle(matrix[3][3])
    drawObstacle(matrix[4][4])

    print(DataFrame(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            #drawObstacle(matrix[i][j]
            #print(i, j, matrix[i][j])
            pass
    #drawMatrix(matrix)
    print(DataFrame(matrix))
    pygame.display.update()
    clock.tick(30)
message("SIMULATION IS OVER", RED)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()

