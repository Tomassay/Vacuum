from pandas import *
import random
#import numpy as np

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

        if self.cleanness:
            cleanness = '.'
        else:
            cleanness = '#'
        return cleanness

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

    def scan_room(self, robot):
        for w in range(self.width-1):
            for l in range(self.length-1):
                if robot.posx == self.map[w] and robot.posy == self.map[l]:
                    self.map[w][l] = robot

    def make_room(self):
        try:
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
                        self.map[w][l] = Cell(posy=w, posx=l, definition='basic', cleanness=True)

        except:
            pass
            # print(range(self.length))
            # print('itt szállt el: oszlop: ' + str(w) + ' sor: ' + str(l))

    def make_dirt(self):

        for w in range(1,self.width-1):
            #print('w', w)
            for l in range(1,self.length-1):
                #print('l', l)
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
        return 'o'

    def clean(self, Cell):
        if self.posx == Cell.posx and self.posy == Cell.posy:
            Cell.set_clean()

    def move_right(self, matrix):

        #matrix[self.posy][self.posx] = Cell(posy=self.posy, posx=self.posx, definition='basic', cleanness=True)
        matrix[self.posy][self.posx] = '→'
        self.posx += 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_left(self, matrix):

        #matrix[self.posy][self.posx] = Cell(posy=self.posy, posx=self.posx, definition='basic', cleanness=True)
        matrix[self.posy][self.posx] = '←'
        self.posx -= 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_up(self, matrix):
        print(self.possible_move_x(matrix))
        matrix[self.posy][self.posx] = '↑'
        #matrix[self.posy][self.posx] = Cell(posy=self.posy, posx=self.posx, definition='basic', cleanness=True)
        self.posy -= 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_down(self, matrix):
        matrix[self.posy][self.posx] = '↓'
        #matrix[self.posy][self.posx] = Cell(posy=self.posy, posx=self.posx, definition='basic', cleanness=True)
        self.posy += 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_up_right(self, matrix):
        matrix[self.posy][self.posx] = '↗'
        # matrix[self.posy][self.posx] = Cell(posy=self.posy, posx=self.posx, definition='basic', cleanness=True)
        self.posy -= 1
        self.posx += 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_up_left(self, matrix):

        matrix[self.posy][self.posx] = '↖'
        # matrix[self.posy][self.posx] = Cell(posy=self.posy, posx=self.posx, definition='basic', cleanness=True)
        self.posy -= 1
        self.posx -= 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_down_right(self, matrix):
        matrix[self.posy][self.posx] = '↘'
        # matrix[self.posy][self.posx] = Cell(posy=self.posy, posx=self.posx, definition='basic', cleanness=True)
        self.posy += 1
        self.posx += 1
        matrix[self.posy][self.posx] = self
        return matrix

    def move_down_left(self, matrix):
        matrix[self.posy][self.posx] = '↙'
        # matrix[self.posy][self.posx] = Cell(posy=self.posy, posx=self.posx, definition='basic', cleanness=True)
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



kitchen.print_room()
kitchen.make_room()
# kitchen.make_dirt()
# kitchen.print_room()
# kitchen.make_dirt()
# kitchen.print_room()
# kitchen.make_dirt()
# kitchen.make_dirt()
# kitchen.make_dirt()
# kitchen.make_dirt()
# kitchen.make_dirt()
# print('TISZTA')
# kitchen.print_room()
#

kosz = Cell(posy=3, posx=3, definition="kitakarított", cleanness=True)
kosz.set_dirty()

kitchen.map[3][3] = kosz
kitchen.print_room()
# robi = Vacuum_Robot(1,1)
# kitchen.map[3][3] = robi
# robi.move_right()
# kitchen.map[robi.posx][robi.posy] = robi
#
# kitchen.place_robot(robi, 5,5)
# print(robi.posx, robi.posy)
#
# kitchen.scan_room(robi)

# kitchen.map[3][3] = robi
# kitchen.map[3][3] = Cell(posy=3, posx=3, definition="kitakarított", cleanness=True)
# kitchen.map[3][4] = robi

# kitchen.map[3][3].set_clean() így jó


robi = Vacuum_Robot(2, 4)
print('Robi PXPY: ' , robi.posy, robi.posx)
#print('Robi PXPY: ' , robi.posy, robi.posx)
#robi.move_right(kitchen.map)
#print('Robi PXPY: ' , robi.posy, robi.posx)
#print(kitchen.map)

# kitchen.map[3][3] = Cell(posy=3, posx=3, definition="kitakarított", cleanness=True)
# print('TISZTA')
# kitchen.print_room()
# kitchen.map[3][3] = Cell(posy=3, posx=3, definition="kitakarított", cleanness=False)
#
# print('KOSZOS-E', kitchen.map[3][3])
# robi = Vacuum_Robot(3,3)
# kitchen.place_robot(robi,3,3)
# kitchen.map[robi.posx][robi.posy] = Vacuum_Robot(robi.posx, robi.posy)
# kitchen.map[3][3].set_clean()

kitchen.print_room()

robi.move_right(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)

robi.move_right(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)

robi.move_down(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)


robi.move_left(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)


robi.move_up(kitchen.map)
robi.move_up(kitchen.map)
robi.move_up(kitchen.map)
robi.move_up(kitchen.map)
robi.move_up(kitchen.map)
robi.move_up(kitchen.map)
robi.move_up(kitchen.map)

kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)

robi.move_up_right(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)

robi.move_down(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)

robi.move_down_right(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)

robi.move_left(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)


robi.move_down_left(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)

robi.move_up_left(kitchen.map)
kitchen.print_room()
print('Robi PXPY: ' , robi.posy, robi.posx)




#
# print('hármas-hármas rublika takarítás előtt:',kitchen.map[3][3])
# robi = Vacuum_Robot(3,3)
# robi.move_right()
# print('hármas-hármas rublika takarítás után:', kitchen.map[3][3])
# kitchen.print_room()



# myRoom = [[0 for x in range(columns)] for x in range(rows)]
#
# def place_walls(myRoom):
#
#     for i in range(rows):
#         for j in range(columns):
#             #myRoom[i][j] = '%s,%s'%(i,j)
#             if i == 0:
#                 myRoom[i][j] = wall
#             elif i == rows-1:
#                 myRoom[i][j] = wall
#             elif j == 0:
#                 myRoom[i][j] = wall
#             elif j == columns - 1:
#                 myRoom[i][j] = wall
#     return myRoom


#place_walls(myRoom)
#print(DataFrame(myRoom))

#kitchen.print_room()