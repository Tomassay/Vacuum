
# A dictionary comprehension to create a dict.
# Coords as the keys and '.' as the values.
board = {(x, y): '.' for x in range(10) for y in range(10)}

# To change the value just set some coords to 'X' or '.'.




class Dog():
    pass

kutya = Dog()

board[(2, 3)] = kutya
def move(oldx,oldy, newx, newy, t):
    board[(newx, newy)] = t
    board[(oldx, oldy)] = '.'

# Print the board.
for y in range(10):
    for x in range(10):
        print(board[(x, y)], end=' ')
    print()

move(2,3, 0,0, kutya)

print('\n')
for y in range(10):
    for x in range(10):
        print(board[(x, y)], end=' ')
    print()







# cols = 4
# rows = 4
#
# matrix = {(row, col): 0 for row in range(cols) for col in range(cols)}
# print(matrix)
#
# matrix[1,1] = 'alma'
#
# print(matrix)
#
# #matrix[0,0] = 'alma'
# #matrix[1,1] = 0
# #print(matrix)
#
#
# def move_from(*old_pos):
#
#
#
#
# move_from(matrix[1,1])
# print(matrix)
#
