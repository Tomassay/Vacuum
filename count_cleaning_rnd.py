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
                #print('w', w)
                for l in range(self.length):
                   # print('l', l)
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
                        # number += 1


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
        return '❤'

    def move_random(self, matrix):

        self.move_forward(matrix.map)

        up_w = self.whats_up(matrix.map)
        back_w = self.whats_down(matrix.map)
        right_w = self.whats_right(matrix.map)
        left_w = self.whats_left(matrix.map)
        directions = ['up', 'down', 'left', 'right']
        arrows = ['←', '→', '↓', '↑']
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

    def whats_up(self, matrix):
        return matrix[self.posy-1][self.posx]

    def whats_down(self, matrix):
        return matrix[self.posy+1][self.posx]

    def whats_left(self, matrix):
        return matrix[self.posy][self.posx-1]

    def whats_right(self, matrix):
        return matrix[self.posy][self.posx+1]

    def move_forward(self, matrix):
        # print('utolsó lépés move forward', self.last_step)
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
        number = self.whats_left(matrix)
        if number != "w":
            number += 1
            matrix[self.posy][self.posx] = number
            self.posx -= 1
            matrix[self.posy][self.posx] = self
            self.last_step = 'left'
        else:
            pass


    def move_right(self, matrix):
        number = self.whats_right(matrix)
        if number != 'w':
            number += 1
            matrix[self.posy][self.posx] = number
            self.posx += 1
            matrix[self.posy][self.posx] = self
            self.last_step = 'right'
        else:
            pass

    def move_up(self, matrix):
        number = self.whats_up(matrix)
        if number != "w":
            number += 1
            matrix[self.posy][self.posx] = number
            self.posy -= 1
            matrix[self.posy][self.posx] = self
            self.last_step = 'up'
        else:
            pass

    def move_down(self, matrix):
        number = self.whats_down(matrix)
        if number != "w":
            number += 1
            matrix[self.posy][self.posx] = number
            self.posy += 1
            matrix[self.posy][self.posx] = self

            self.last_step = 'down'
        #return matrix
        else:
            pass


kitchen = Room('kitchen', 10, 10)


kitchen.make_room()

robi = Vacuum_Robot(5, 5)
robi.move_down(kitchen.map)
kitchen.print_room()

w = 'w'

test_room = [[w,w,w,w,w,w,w,w,w,w],
             [w,1,2,3,4,5,6,7,8,w],
             [w,9,10,11,12,13,14,15,16,w],
             [w,17,18,19,20,21,22,23,24,w],
             [w,25,26,27,28,29,30,31,32,w],
             [w,33,34,35,36,37,38,39,40,w],
             [w,41,42,43,44,45,46,47,48,w],
             [w,49,50,w,51,w,52,53,54,w],
             [w,w,w,55,56,57,w,w,w,w],
             [w,w,w,w,w,w,w,w,w,w]]

steps = 0

while steps<500:

    robi.move_random(kitchen)
    robi.move_forward(kitchen.map)
    kitchen.print_room()

    # robi.move_random(test_room)
    # print(DataFrame(test_room))

    steps += 1
