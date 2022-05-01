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

rows = int(dis_width / ROBOT_RADIUS)
cols = int(dis_height / ROBOT_RADIUS)

# matrix = {(row, col):0 for row in range(rows) for col in range(rows)}
#rows = 4
#cols = 4
matrix = {(row, col): 0 for row in range(rows) for col in range(cols)}

def difference_one(num1, num2):
    return num1 + 1 == num2 or num2 +1 == num1

def is_near(tuple1, tuple2):
    if tuple1[0] == tuple2[0] and difference_one(tuple1[1], tuple2[1]) \
            or tuple1[1] == tuple2[1] and difference_one(tuple1[0], tuple2[0]) \
            or difference_one(tuple1[0], tuple2[0]) and difference_one(tuple1[1], tuple2[1]):
        return True
    else:
        return False

def neigbors(dict, elem):
    neigbours = []
    for k,v in dict.items():
        if is_near(k, elem):
            neigbours.append(k)
    return neigbours

neigbors_dict = dict.fromkeys(matrix)

for key, value in matrix.items():
   neigbors_dict[key] = neigbors(matrix, key)

matrix[(1,1)] = 1

#(0,1): [(0,0),(1,0),(1,1)]

def valid_move(destination, coord_list):
    #print(coord_list)
    #print(destination)
    #print(coord_list)
    if destination in coord_list:
        return True
    else:
        return False

# print(neigbors_dict[(0,0)])
#
# print(valid_move((0,1), neigbors_dict[(0,0)]))



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

def check_right():
    return valid_move((robi.get_posx(), robi.get_posy()), neigbors_dict[(robi.get_posx()+1, robi.get_posy())])

def make_valid_move_right():
    global robot_motion_x
    try:
        if check_right():
            move_robi(robi.get_posx(), robi.get_posy(), robi.get_posx()+1, robi.get_posy(), robi)
            robot_motion_x = 1
        else:
            print('fal')
    except:
            pass

def make_valid_move_left():
    global robot_motion_x
    try:
        if valid_move((robi.get_posx(), robi.get_posy()), neigbors_dict[(robi.get_posx()+1, robi.get_posy())]):
            move_robi(robi.get_posx(), robi.get_posy(), robi.get_posx()+1, robi.get_posy(), robi)
            robot_motion_x = -1
        else:
            print('fal')
    except:
            pass

def make_valid_move_up():
    global robot_motion_y
    try:
        if valid_move((robi.get_posx(), robi.get_posy()), neigbors_dict[(robi.get_posx()+1, robi.get_posy())]):
            move_robi(robi.get_posx(), robi.get_posy(), robi.get_posx()+1, robi.get_posy(), robi)
            robot_motion_y = 1
        else:
            print('fal')
    except:
            pass

def make_valid_move_down():
    global robot_motion_y
    try:
        if valid_move((robi.get_posx(), robi.get_posy()), neigbors_dict[(robi.get_posx()+1, robi.get_posy())]):
            move_robi(robi.get_posx(), robi.get_posy(), robi.get_posx()+1, robi.get_posy(), robi)
            robot_motion_y = -1
        else:
            print('fal')
    except:
            pass


move_robi(3,3, 0, 0, robi)
print(matrix)

print(matrix[(3,2)])
print(robi.get_posy())
def draw_robot(posx, posy):
    dis.fill((0, 0, 0))
    pygame.draw.ellipse(dis, ROBOT_COLOR, [posx*BLOCK_SIZE, posy*BLOCK_SIZE, ROBOT_RADIUS, ROBOT_RADIUS])

pygame.display.update()
time.sleep(2)
x1 = dis_width/2
y1 = dis_height/2



clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)


# draw_robot(robi.get_posx(), robi.get_posy())
simulation_over = False
#print('NBR', neigbors_dict)

# move_robi(robi.get_posx(), robi.get_posy(), 2, 2, robi)
# #print(matrix)
#
# draw_robot(robi.get_posx(), robi.get_posy())
# draw_grid()
# pygame.display.update()
# time.sleep(1)
#
# move_robi(robi.get_posx(), robi.get_posy(), 1, 1, robi)
# draw_robot(robi.get_posx(), robi.get_posy())
# draw_grid()
# print(matrix)
# pygame.display.update()

move_robi(robi.get_posx(), robi.get_posy(), 0, 1, robi)
draw_robot(robi.get_posx(), robi.get_posy())
draw_grid()

pygame.display.update()
time.sleep(1)

print('Robi pozi', robi.get_posx(), robi.get_posy())

arg_t = (robi.get_posx(), robi.get_posy())
print(valid_move((robi.get_posx(), robi.get_posy()), neigbors_dict[(robi.get_posx()+1, robi.get_posy()+1)]))
print(matrix)


robot_position_x = robi.get_posx()
robot_position_y = robi.get_posy()
robot_motion_x = 0
robot_motion_y = 0


steps = 0

while steps < 20:
    print("1 robot_x, robot_y", robot_position_x, robot_position_y)
    print("1 robot_motion_x, 1 robot_motion_y", robot_motion_x, robot_motion_y)
    make_valid_move_right()
    draw_robot(robot_position_x, robot_position_y)
    draw_grid()
    # make_valid_move_down()
    # print("2 robot_x, robot_y", robot_position_x, robot_position_y)
    # draw_robot(robot_position_x, robot_position_y)
    # draw_grid()
    # make_valid_move_down()
    # draw_robot(robot_position_x, robot_position_y)
    # draw_grid()
    # make_valid_move_right()
    # draw_robot(robot_position_x, robot_position_y)
    # draw_grid()
    # make_valid_move_left()
    # draw_robot(robot_position_x, robot_position_y)
    # draw_grid()
    # make_valid_move_up()
    # #draw_robot(robi.get_posx(), robi.get_posy())
    # draw_robot(robot_position_x, robot_position_y)
    # draw_grid()
    pygame.display.update()
    time.sleep(1)
    print(matrix)
    robot_position_x += robot_motion_x
    robot_position_y += robot_motion_y
    #robot_position_y += robot_motion_y

    #print("2 robot_motion_x", robot_motion_x)
    steps += 1




# while not simulation_over:
#     draw_grid()
#     draw_robot(robi.get_posx(), robi.get_posy())
#     for event in pygame.event.get():
#
#         if event.type ==pygame.QUIT:
#             simulation_over = True
#
#     x1 = 5
#     y1 = 5
#
#     pygame.display.update()
#     clock.tick(30)
#
# message("SIMULATION IS OVER", RED)
# pygame.display.update()
# time.sleep(2)
# pygame.quit()
# quit()


