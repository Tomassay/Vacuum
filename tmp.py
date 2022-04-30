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

def difference_one(num1, num2):
    return num1 + 1 == num2 or num2 +1 == num1

def nbr(tuple1, tuple2):
    if tuple1[0] == tuple2[0] and difference_one(tuple1[1], tuple2[1]) \
            or tuple1[1] == tuple2[1] and difference_one(tuple1[0], tuple2[0]) \
            or difference_one(tuple1[0], tuple2[0]) and difference_one(tuple1[1], tuple2[1]):
        return True
    else:
        return False

def nbr_list(dict, elem):
    neigbours = []
    for k,v in dict.items():
        if nbr(k, elem):
            neigbours.append(k)
    return neigbours

nbr_dict = dict.fromkeys(matrix)

for key, value in matrix.items():
   nbr_dict[key] = nbr_list(matrix, key)

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

move_robi(robi.get_posx(), robi.get_posy(), 2, 2, robi)
draw_robot(robi.get_posx(), robi.get_posy())
simulation_over = False
print('NBR', nbr_dict)
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

message("SIMULATION IS OVER", RED)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()


