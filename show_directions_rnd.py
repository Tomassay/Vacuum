from pandas import *
import random

wall = 'w'
f = 0
d = 1
room = []

rows = 10
columns = 10


class Cell:
    def __init__(self, posy, posx, definition, cleanness):
        self.posy = posy,
        self.posx = posx,
        self.definition = definition
        self.cleanness = cleanness,

    def __str__(self):
        return str(self.definition)

    def set_clean(self):
        self.cleanness = True

    def get_clean(self):
        return self.cleanness

    def set_dirty(self):
        self.cleanness = False

class Room:

    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.map = [[0 for x in range(self.length)] for x in range(self.width)]

    def room_size(self):
        return str(self.length * self.width)

    def set_map(self, map):
        self.map = map

    def __str__(self):
        size = self.room_size()
        return 'Its a ' + self.name + ' and its ' + size +  'm2 and its clean'

    def get_definition(self):
        return self.definition

    def scan_room(self, robot):
        for w in range(self.width-1):
            for l in range(self.length-1):
                if robot.posx == self.map[w] and robot.posy == self.map[l]:
                    self.map[w][l] = robot

    def make_room(self):
        try:
            number = 0
            for w in range(self.width):
                for l in range(self.length):
                    if w == 0:

                        self.map[w][l] = wall
                    elif w == self.width-1:
                        self.map[w][l] = wall
                    elif l == 0:
                       self.map[w][l] = wall
                    elif l == self.length-1:
                        self.map[w][l] = wall
                    else:
                        self.map[w][l] = number
                        number += 1
        except:
            pass

    def make_dirt(self):

        for w in range(1,self.width-1):
            for l in range(1,self.length-1):
                dirt = random.randint(1,3)
                if dirt == 1:
                    dirty = Cell(w, l, 'sajt', False)
                    dirty.set_dirty()
                    self.map[w][l] = dirty
        return self.map

    def place_robot(self, Robot, posx, posy):
                self.map[posx][posy] = Robot(posx, posy)

    def print_room(self):
        print(DataFrame(self.map))

class Vacuum_Robot:

    def __init__(self, posy, posx):
        self.posy = posy
        self.posx = posx

    def __str__(self):
        return '???'

    def clean(self, Cell):
        if self.posx == Cell.posx and self.posy == Cell.posy:
            Cell.set_clean()

    def collision_detection(self, elem):
        return elem == 'w'

    def falig(self, matrix):
        try:

            if self.whats_down(matrix) != 'w':
                self.move_down(matrix.map)
            else:
                if not self.collision_detection(matrix.map[self.posx][self.posy-1]):
                    self.move_left(matrix.map)
        except:
            pass


    def random_walk2(self, matrix):
        arrows = [ '???','???','???','???']
        # print('utols?? l??p??s', self.last_step)
        front = self.whats_front(matrix.map)
        up_w = self.whats_up(matrix.map)
        back_w = self.whats_down(matrix.map)
        right_w = self.whats_right(matrix.map)
        left_w = self.whats_left(matrix.map)

        if front != 'w':
            self.move_forward(matrix.map)
        elif front == 'w' and left_w != 'w' and right_w != 'w':
            self.move_left(matrix.map)
        elif front == 'w' and left_w != 'w' and right_w == 'w':
            self.move_down(matrix.map)
        elif front == 'w' and left_w == 'w' and back_w != 'w':
            self.move_right(matrix.map)
        elif front == 'w' and back_w == 'w' and right_w != 'w':
            self.move_up(matrix.map)


    def rw(self, matrix):
        front = self.whats_front(matrix.map)
        up_w = self.whats_up(matrix.map)
        back_w = self.whats_down(matrix.map)
        right_w = self.whats_right(matrix.map)
        left_w = self.whats_left(matrix.map)
        self.VOLT = False
        print('front',front)
        if front != 'w':
            print('A')
            self.move_forward(matrix.map)
        elif front == 'w' and left_w != 'w':
            self.move_left(matrix.map)
        elif front == 'w' and right_w != 'w':
            self.move_right(matrix.map)
        elif front == 'w' and back_w != 'w':
            self.move_down(matrix.map)
        elif front == 'w' and up_w != 'w':
            self.move_up(matrix.map)
        else:
            print("*** kimaradt CASE")
            return self.VOLT

    def move_random(self, matrix):

        self.move_forward(matrix.map)
        up_w = self.whats_up(matrix.map)
        back_w = self.whats_down(matrix.map)
        right_w = self.whats_right(matrix.map)
        left_w = self.whats_left(matrix.map)
        directions = ['up', 'down', 'left', 'right']
        arrows = ['???', '???', '???', '???']
        random.shuffle(directions)
        suffled_var = directions.pop()
        if suffled_var == 'up':
            self.move_up(matrix.map)
        if suffled_var == 'down':
            self.move_down(matrix.map)
        if suffled_var == 'right':
            self.move_right(matrix.map)
        if suffled_var == 'left':
            self.move_left(matrix.map)

    def move_random_s(self, matrix):
        self.move_forward(matrix)
        up_w = self.whats_up(matrix)
        back_w = self.whats_down(matrix)
        right_w = self.whats_right(matrix)
        left_w = self.whats_left(matrix)
        directions = ['up', 'down', 'left', 'right']
        arrows = ['???', '???', '???', '???']
        random.shuffle(directions)
        suffled_var = directions.pop()
        if suffled_var == 'up':
            self.move_up(matrix)
        if suffled_var == 'down':
            self.move_down(matrix)
        if suffled_var == 'right':
            self.move_right(matrix)
        if suffled_var == 'left':
            self.move_left(matrix)

    def whats_front(self, matrix):
        if self.last_step == 'up':
            front = self.whats_up(matrix)
        elif self.last_step == 'right':
            front = self.whats_right(matrix)
        elif self.last_step == 'left':
            front = self.whats_left(matrix)
        elif self.last_step == 'down':
            front = self.whats_down(matrix)
        return front

    def mdl(self, matrix):
        if self.whats_down(matrix.map) == 'w':
            self.move_left(matrix.map)
        else:
            self.move_down(matrix.map)

    def whats_up(self, matrix):
        return matrix[self.posy-1][self.posx]

    def whats_down(self, matrix):
        return matrix[self.posy+1][self.posx]

    def whats_left(self, matrix):
        return matrix[self.posy][self.posx-1]

    def whats_right(self, matrix):
        return matrix[self.posy][self.posx+1]

    def is_grid_free(self, cell):
        if cell == 'w':
            return False
        else:
            return True

    def place_robot(self, matrix):
        matrix[self.posy][self.posx] = self

    def move_forward(self, matrix):
        if self.last_step == 'up':
            self.move_up(matrix)
        elif self.last_step == 'right':
            self.move_right(matrix)
        elif self.last_step == 'left':
            self.move_left(matrix)
        elif self.last_step == 'down':
            self.move_down(matrix)

    def whats_front(self, matrix):
        if self.last_step == 'up':
            front = self.whats_up(matrix)
        elif self.last_step == 'right':
            front = self.whats_right(matrix)
        elif self.last_step == 'left':
            front = self.whats_left(matrix)
        elif self.last_step == 'down':
            front = self.whats_down(matrix)
        return front

    def move_left(self, matrix):
        if self.whats_left(matrix) != "w":
            matrix[self.posy][self.posx] = '???'
            self.posx -= 1
            matrix[self.posy][self.posx] = self
            self.last_step = 'left'
        else:
            pass

    def move_right(self, matrix):
        if self.whats_right(matrix) != 'w':
            matrix[self.posy][self.posx] = '???'
            self.posx += 1
            matrix[self.posy][self.posx] = self
            self.last_step = 'right'
        else:
            pass

    def move_up(self, matrix):
        if self.whats_up(matrix) != "w":
            matrix[self.posy][self.posx] = '???'
            self.posy -= 1
            matrix[self.posy][self.posx] = self
            self.last_step = 'up'
        else:
            pass

    def move_down(self, matrix):
        if self.whats_down(matrix) != "w":
            matrix[self.posy][self.posx] = '???'
            self.posy += 1
            matrix[self.posy][self.posx] = self

            self.last_step = 'down'
        else:
            pass

    def move_up_right(self, matrix):
        matrix[self.posy][self.posx] = '???'
        self.posy -= 1
        self.posx += 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_up_left(self, matrix):
        matrix[self.posy][self.posx] = '???'
        self.posy -= 1
        self.posx -= 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_down_right(self, matrix):
        matrix[self.posy][self.posx] = '???'
        self.posy += 1
        self.posx += 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_down_left(self, matrix):
        matrix[self.posy][self.posx] = '???'
        self.posy += 1
        self.posx -= 1
        matrix[self.posy][self.posx] = self
        return matrix

    def possible_move_x(self, matrix):
        # print('posx', self.posx, 'len', len(matrix))
        if self.posx >= len(matrix):
           self.posx = len(matrix)
           possible = False
        elif self.posx <= 0:
            self.posx = 0
            possible = False
        else:
           possible = True
        return possible

    def turn(self, matrix):
        rotated = zip(*matrix[::-1])
        return list(rotated)

    def move_or_round(self, matrix):
        if self.whats_front(matrix) != 'w':
            self.move_forward(matrix)
        else:
            new_matrix = self.turn(matrix)
            self.move_forward(new_matrix)

kitchen = Room('kitchen', 10, 10)


kitchen.make_room()


robi = Vacuum_Robot(5, 5)

kitchen.print_room()

robi.place_robot(kitchen.map)

kitchen.print_room()


robi.move_up_right(kitchen.map)
kitchen.print_room()


robi.move_down(kitchen.map)
kitchen.print_room()

kitchen.print_room()

kitchen.print_room()


w = 'w'

test_room = [[w,w,w,w,w,w,w,w,w,w],
             [w,1,2,3,4,5,6,7,8,w],
             [w,9,10,11,12,13,14,15,16,w],
             [w,17,18,19,w,21,22,23,24,w],
             [w,25,26,27,w,29,30,31,32,w],
             [w,33,34,35,36,37,38,39,40,w],
             [w,41,42,43,44,45,46,47,48,w],
             [w,49,50,w,51,51,53,54,55,w],
             [w,w,w,56,57,58,w,w,w,w],
             [w,w,w,w,w,w,w,w,w,w]]

steps = 0

while steps<500:

    robi.move_random_s(test_room)

    print(DataFrame(test_room))


    steps += 1

