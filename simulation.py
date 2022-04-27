from pandas import *
import random

from findneighbors import findNeighbors

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
        self.falig(kitchen.map)

    def __str__(self):
        return '❤'

    def clean(self, Cell):
        if self.posx == Cell.posx and self.posy == Cell.posy:
            Cell.set_clean()

    def move_right(self, matrix):
        if self.whats_right(matrix.map) == 'w':
            matrix[self.posy][self.posx] = '→'
            self.posx += 1
            matrix[self.posy][self.posx] = self
        else:
            pass

    def collision_detection(self, elem):
        return elem == 'w'

    def falig(self, matrix):
        try:
            # print(self.posx, self.posy)
            # print(self.collision_detection(matrix.map[self.posx+1][self.posy]))
            # print('térképteszt', matrix.map[0][2])
            # print('a vizsgált elem: ', matrix.map[self.posx+2][self.posy])
            # print('W-E',self.collision_detection(matrix.map[self.posx+2][self.posy]))
            print('*****A FELTÉTEL****', self.whats_down(matrix))
            #if not self.collision_detection(matrix.map[self.posx+2][self.posy]):
            if self.whats_down(matrix) != 'w':
                print('itt vagyok:', self.posx, self.posy)
                self.move_down(matrix.map)
            else:
                if not self.collision_detection(matrix.map[self.posx][self.posy-1]):
                    self.move_left(matrix.map)

            #matrix.print_room()
        except:
            print("FAL")


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

    def move_left(self, matrix):
        if self.whats_left(matrix) != "w":
            matrix[self.posy][self.posx] = '←'
            self.posx -= 1
            matrix[self.posy][self.posx] = self
        else:
            pass

    def move_up(self, matrix):
        #print(self.possible_move_x(matrix))
        if self.whats_up(matrix) != "w":
            matrix[self.posy][self.posx] = '↑'
            self.posy -= 1
            matrix[self.posy][self.posx] = self
        else:
            pass

    def move_down(self, matrix):
        if self.whats_down(matrix) != "w":
            matrix[self.posy][self.posx] = '↓'
            self.posy += 1
            matrix[self.posy][self.posx] = self
        #return matrix
        else:
            pass

    def move_up_right(self, matrix):
        matrix[self.posy][self.posx] = '↗'
        self.posy -= 1
        self.posx += 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_up_left(self, matrix):

        matrix[self.posy][self.posx] = '↖'
        self.posy -= 1
        self.posx -= 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_down_right(self, matrix):
        matrix[self.posy][self.posx] = '↘'
        self.posy += 1
        self.posx += 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_down_left(self, matrix):
        matrix[self.posy][self.posx] = '↙'
        self.posy += 1
        self.posx -= 1
        matrix[self.posy][self.posx] = self
        return matrix

    def possible_move_x(self, matrix):
        print('posx', self.posx, 'len', len(matrix))
        if self.posx >= len(matrix):
           self.posx = len(matrix)
           possible = False
        elif self.posx <= 0:
            self.posx = 0
            possible = False
        else:
           possible = True
        return possible


kitchen = Room('kitchen', 10, 10)


kitchen.make_room()

# kitchen.map[3][3].set_clean() így jó

print('Robi példányosítása')
robi = Vacuum_Robot(2, 4)
print('Nincs robi a képen')
kitchen.print_room()

robi.place_robot(kitchen.map)
print('Robi ott a képen')
kitchen.print_room()
print('Robi PXPY: ', robi.posy, robi.posx)

robi.move_up_right(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ', robi.posy, robi.posx)

robi.move_down(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ', robi.posy, robi.posx)

n = list(findNeighbors(kitchen.map, 2, 1))  # 9 szomszédai
# print(n)
#
# print(n[1])

# Declare the visited array
vis = [[False for i in range(4)] for i in range(4)]
    # vis, False, sizeof vis)
#
# print(DataFrame(BFS(kitchen.map, vis, 0, 0)))
#

kitchen.print_room()
print('innentől nem szabadna lépnie')
robi.falig(kitchen)
#robi.falig(kitchen)
#robi.falig(kitchen)
kitchen.print_room()
print('Ez nem fal', robi.collision_detection(kitchen.map[5][5]))
print('Ez egy fal',robi.collision_detection(kitchen.map[0][0]))

print('Ez egy fal',robi.collision_detection(kitchen.map[8+1][1]))
print('Hello')

# robi.falig(kitchen)
# kitchen.print_room()
#
# robi.falig(kitchen)
# kitchen.print_room()
#
# robi.falig(kitchen)
# kitchen.print_room()
#
# robi.falig(kitchen)
# kitchen.print_room()
#
# robi.falig(kitchen)
# kitchen.print_room()
#
# robi.falig(kitchen)
# kitchen.print_room()

steps = 0
while steps<25:
    #robi.falig(kitchen)
    robi.mdl(kitchen)
    kitchen.print_room()
    steps += 1

print('FElette',robi.whats_up(kitchen.map))
print('Robi PYPX: ', robi.posy, robi.posx)

print('ALATTA',robi.whats_down(kitchen.map))
print('Robi PYPX: ', robi.posy, robi.posx)

print('JOBBRA',robi.whats_left(kitchen.map))
print('Robi PYPX: ', robi.posy, robi.posx)

print('BALLRA',robi.whats_right(kitchen.map))
print('Robi PYPX: ', robi.posy, robi.posx)

print('FElette',robi.whats_up(kitchen.map))
print('Robi PYPX: ', robi.posy, robi.posx)

print(kitchen.map[9][2])