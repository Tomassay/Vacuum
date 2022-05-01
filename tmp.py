import pygame
import time

ROBOT_RADIUS = 20
WHITE = (200, 200, 200)
RED = (240, 0, 0)
BACKGROUND_COLOR = (200, 219, 199)
ROBOT_COLOR = (240, 240, 240)
BLOCK_SIZE = 20
pygame.init()

dis_width = 400
dis_height = 300
dis = pygame.display.set_mode(size=(dis_width, dis_height))
clock = pygame.time.Clock()
robot_speed = 30


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])


# pygame.display.update()
pygame.display.set_caption("Robot Vacuum Cleaner Simulation by Tamas Levay")

rows = int(dis_width / ROBOT_RADIUS)
cols = int(dis_height / ROBOT_RADIUS)

matrix = {(row, col): 0 for row in range(rows) for col in range(cols)}


def difference_one(num1, num2):
    return num1 + 1 == num2 or num2 + 1 == num1


def is_near(tuple1, tuple2):
    if tuple1[0] == tuple2[0] and difference_one(tuple1[1], tuple2[1]) \
            or tuple1[1] == tuple2[1] and difference_one(tuple1[0], tuple2[0]) \
            or difference_one(tuple1[0], tuple2[0]) and difference_one(tuple1[1], tuple2[1]):
        return True
    else:
        return False


def neigbors(dict, elem):
    neigbours = []
    for k, v in dict.items():
        if is_near(k, elem):
            neigbours.append(k)
    return neigbours


def valid_move(destination, coord_list):
    if destination in coord_list:
        return True
    else:
        return False


def draw_grid():
    for x in range(rows):
        for y in range(cols):
            if (matrix[x, y] == 1):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE,
                                   BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(dis, RED, rect, 1)
            else:
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE,
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


def place_robi():
    x = robi.get_posx()
    y = robi.get_posy()
    matrix[(x, y)] = robi


def move_robi(oldx, oldy, newx, newy, rb):
    matrix[(newx, newy)] = rb
    matrix[(oldx, oldy)] = 0
    robi.set_posx(newx)
    robi.set_posy(newy)
    print('robi most', rb.posx, rb.posy)


def right_is_valid():
    return valid_move((robi.get_posx(), robi.get_posy()), neigbors_dict[(robi.get_posx() + 1, robi.get_posy())])


def move_right():
    global robot_motion_x
    move_robi(robi.get_posx(), robi.get_posy(), robi.get_posx() + 1, robi.get_posy(), robi)
    robot_motion_x = 1


def make_valid_move_right():
    try:
        if right_is_valid():
            move_right()
    except KeyError:
        pass


def left_is_valid():
    return valid_move((robi.get_posx(), robi.get_posy()), neigbors_dict[(robi.get_posx() - 1, robi.get_posy())])


def move_left():
    global robot_motion_x
    move_robi(robi.get_posx(), robi.get_posy(), robi.get_posx() - 1, robi.get_posy(), robi)
    robot_motion_x = -1


def make_valid_move_left():

    try:
        if left_is_valid():
            move_left()
    except KeyError:
        pass


def down_is_valid():
    return valid_move((robi.get_posx(), robi.get_posy()), neigbors_dict[robi.get_posx(), robi.get_posy() + 1])


def move_down():
    global robot_motion_y
    move_robi(robi.get_posx(), robi.get_posy(), robi.get_posx(), robi.get_posy() + 1, robi)
    robot_motion_y = 1


def make_valid_move_down():
    try:
        if down_is_valid():
            move_down()
    except KeyError:
        pass


def up_is_valid():
    return valid_move((robi.get_posx(), robi.get_posy()), neigbors_dict[robi.get_posx(), robi.get_posy() - 1])


def move_up():
    global robot_motion_y
    move_robi(robi.get_posx(), robi.get_posy(), robi.get_posx(), robi.get_posy() - 1, robi)
    robot_motion_y = -1


def make_valid_move_up():

    try:
        if up_is_valid():
            move_up()
    except KeyError:
        pass


def draw_robot(posx, posy):
    dis.fill((0, 0, 0))
    print('draw_pos_x', posx)
    pygame.draw.ellipse(dis, ROBOT_COLOR, [posx * BLOCK_SIZE, posy * BLOCK_SIZE, ROBOT_RADIUS, ROBOT_RADIUS])


neigbors_dict = dict.fromkeys(matrix)

for key, value in matrix.items():
    neigbors_dict[key] = neigbors(matrix, key)

matrix[(1, 1)] = 1

robi = Robot()

print(matrix)
pygame.display.update()
time.sleep(2)
x1 = dis_width / 2
y1 = dis_height / 2

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

simulation_over = False
# print('NBR', neigbors_dict)

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

robot_position_x = robi.get_posx()
robot_position_y = robi.get_posy()
robot_motion_x = 0
robot_motion_y = 0

steps = 0

while not simulation_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulation_over = True
    make_valid_move_right()
    draw_robot(robi.get_posx(), robi.get_posy())
    draw_grid()
    robot_position_x += robot_motion_x
    robot_position_y != robot_motion_y

    pygame.display.update()
    clock.tick(robot_speed)

    # steps += 1
#
# draw_robot(5, robot_position_y)


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
