import pygame
import time

ROBOT_RADIUS = 20
WHITE = (200, 200, 200)
RED = (240, 0, 0)
BACKGROUND_COLOR = (200, 219, 199)
ROBOT_COLOR = (240, 240, 240)
BLOCK_SIZE = 20  # Set the size of the grid block
pygame.init()

dis_width = 400
dis_height = 300
dis = pygame.display.set_mode(size=(dis_width, dis_height))
dis = pygame.display.set_mode(size=(dis_width, dis_height))


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__setattr__('_initializing', True)
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
        super(AttrDict, self).__setattr__('_initializing', False)

    def __setattr__(self, x, value):
        if x == '_initializing':
            raise KeyError("You should not edit _initalizing")
        if self._initializing or x in self.__dict__.keys():
            super(AttrDict, self).__setattr__(x, value)
        else:
            raise KeyError("No new keys allowed!")

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

pygame.display.update()
pygame.display.set_caption("Robot Vacuum Cleaner Simulation by Tamas Levay")

#rows = int(dis_width / ROBOT_RADIUS)
#cols = int(dis_height / ROBOT_RADIUS)

# matrix = {(row, col):0 for row in range(rows) for col in range(rows)}
rows = 4
cols = 4
matrix = {(row, col): 0 for row in range(rows) for col in range(cols)}


matrix[(1,1)] = 1

def draw_grid():

    for x in range(rows):
        for y in range(cols):
                if(matrix[x,y] == 1):
                    rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE,
                                       BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(dis, RED, rect, 1)
                else:
                    rect = pygame.Rect(x*BLOCK_SIZE, y*BLOCK_SIZE,
                                       BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(dis, WHITE, rect, 1)


class Robot():

    def __init__(self):
        self.posx = None
        self.posy = None

    def set_posx(self, cord):
        self.posx = cord

    def set_posy(self, cord):
        self.posy = cord

    def get_posx(self):
        return self.posx

    def get_posy(self):
        return self.posy

robi = Robot()
# print(matrix[3,2])
# print(matrix)
#
# robi.set_posx(3)
# robi.set_posy(2)
#matrix[(3,2)] = robi

# robi.set_posx(1)
# robi.set_posy(1)
#matrix[(1,1)] = robi
#matrix[3,2] = 'alma'
print(matrix)


def place_robi():
    x = robi.get_posx()
    y = robi.get_posy()
    matrix[(x,y)] = robi

def move_robi(oldx, oldy, newx, newy, rb):
    matrix[(newx, newy)] = rb
    matrix[(oldx, oldy)] = 0
    robi.set_posx(newx)
    robi.set_posy(newy)
    print('robi most',rb.posx, rb.posy)


move_robi(3,3, 0, 0, robi)
print(matrix)



#print(robi.get_posx(), robi.get_posy())
print(matrix[(3,2)])
print(robi.get_posy())
def draw_robot(posx, posy):
    pygame.draw.ellipse(dis, ROBOT_COLOR, [posx*BLOCK_SIZE, posy*BLOCK_SIZE, ROBOT_RADIUS, ROBOT_RADIUS])

pygame.display.update()
time.sleep(2)
x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

#move_robi(robi.get_posx(), robi.get_posy(), 2, 2, robi)
#draw_grid()
#draw_robot(robi.get_posx(), robi.get_posy())
#move_robi(robi.get_posx(), robi.get_posy(), 3,3, robi)
#drawGrid()
#draw_robot(robi.get_posx(), robi.get_posy())
move_robi(robi.get_posx(), robi.get_posy(), 2, 2, robi)
draw_robot(robi.get_posx(), robi.get_posy())
simulation_over = False

while not simulation_over:
    draw_grid()
    draw_robot(robi.get_posx(), robi.get_posy())
    for event in pygame.event.get():

        if event.type ==pygame.QUIT:
            simulation_over = True


    x1 = 5
    y1 = 5

    pygame.display.update()
    clock.tick(30)

    #print(matrix)

message("SIMULATION IS OVER", RED)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()


# import pygame
# import time
# from pandas import *
# pygame.init()
#
# ROBOT_COLOR = (240, 240, 240)
# BACKGROUND_COLOR = (200, 219, 199)
# RED = (240, 0, 0)
# BLACK = (0, 0, 0)
# WHITE = (200, 200, 200)
# ROBOT_RADIUS = 20
#
# dis_width = 400
# dis_height = 300
# dis = pygame.display.set_mode(size=(dis_width, dis_height))
#
# pygame.display.update()
# pygame.display.set_caption("Robot Vacuum Cleaner Simulation by Tamas Levay")
#
#
# #rows = int(dis_width / ROBOT_RADIUS)
# #cols = int(dis_height / ROBOT_RADIUS)
#
# rows = 10
# cols = 10
#
# #matrix = [[0]*cols]*rows
#
# def make_matrix():
#     matrix = {(i,j):0 for i in range(cols) for j in range(rows)}
#     print(matrix)
#     return matrix
#
# matrix = make_matrix()
#
# def put_6_6():
#     matrix['(0,1)'] = 1
#
# def search_matrix(elem):
#     if elem in matrix:
#         return True
#
#
# put_6_6()
#
#
# #
# # x=0
# # y=0
# # for row in matrix:
# #     for col in row:
# #         box = pygame.Rect(x,y,ROBOT_RADIUS, ROBOT_RADIUS)
# #         pygame.draw.rect(dis, (255,255,255), box)
# #         x += ROBOT_RADIUS
# #     y += ROBOT_RADIUS
# #     x = 0
# def drawGrid():
#     BLOCK_SIZE = 20 #Set the size of the grid block
#     for x in range(rows):
#         for y in range(cols):
#             rect = pygame.Rect(x*BLOCK_SIZE, y*BLOCK_SIZE,
#                                BLOCK_SIZE, BLOCK_SIZE)
#             pygame.draw.rect(dis, WHITE, rect, 1)
#
# def drawObstacle(obstacle):
#     block_size = 20
#     rect = pygame.Rect(block_size, block_size, block_size, block_size)
#     pygame.draw.rect(dis, RED, rect, 10)
#
# def drawRobot():
#     pygame.draw.ellipse(dis, ROBOT_COLOR, [x1, y1, ROBOT_RADIUS, ROBOT_RADIUS])
#
# x1 = dis_width/2
# y1 = dis_height/2
#
# x1_change = 0
# y1_change = 0
#
# clock = pygame.time.Clock()
#
# font_style = pygame.font.SysFont(None, 50)
#
#
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width/2, dis_height/2])
#
#
# def detect_wall():
#     if x1 >= dis_width - ROBOT_RADIUS or x1 < ROBOT_RADIUS or y1 >= dis_height - ROBOT_RADIUS or y1 < ROBOT_RADIUS:
#         return True
#     else:
#         return False
#
# def move_left():
#     global  x1_change
#     x1_change = -ROBOT_RADIUS
#
#
# def move_right():
#     if not detect_wall():
#         global x1_change
#         x1_change = ROBOT_RADIUS
#
# def move_down():
#     global  y1_change
#     y1_change = -ROBOT_RADIUS
#
# simulation_over = False
#
# while not simulation_over:
#     drawGrid()
#     for event in pygame.event.get():
#
#         if event.type ==pygame.QUIT:
#             simulation_over = True
#
#     x1 += x1_change
#     y1 += y1_change
#     #dis.fill(BACKGROUND_COLOR)
#     drawRobot()
#     #elem = 1
#     #drawObstacle(matrix[5][5])
#
#
#     #print(DataFrame(matrix))
#     print(matrix)
#
#     #drawMatrix(matrix)
#     #print(DataFrame(matrix))
#     pygame.display.update()
#     clock.tick(30)
# message("SIMULATION IS OVER", RED)
# pygame.display.update()
# time.sleep(2)
# pygame.quit()
# quit()
#
