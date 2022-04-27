from pandas import *

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(DataFrame(matrix))
print(matrix[1][1])



def nexts(dir, x, y):
    return dir[y][x+1]

def turn_right(dir,x,y):
    global next_elem
    next_elem = dir[y+1][x]
    return next_elem

next_elem = nexts(matrix, 1, 1)
print(nexts(matrix,1,1))

print(turn_right(matrix,1,1))
print(next_elem)