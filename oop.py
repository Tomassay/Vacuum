
rows, cols = 3, 3


matrix = {(row, col): 0 for row in range(rows) for col in range(cols)}

matrix[2,2] = 1


matrix[0,0], matrix[2,2] = matrix[2,2], matrix[0,0]

class Tmp:

    def __init__(self, kulcs, value):
        self.kulcs = kulcs
        self.value = value

    def my_neighbor(self):
        pass



def check_key(dict, tuple):
    return (tuple[0], tuple[1]) in dict.keys()

def is_neighbor(dict, tuple):
    first_digit = tuple[0]
    first_digit_minus = tuple[0] - 1
    first_digit_plus = tuple[0] + 1
    second_digit = tuple[1]
    second_digit_minus = tuple[1] - 1
    seond_digit_plus = tuple[1] +1
    answer = []

def difference_one(num1, num2):
    return num1 + 1 == num2 or num2 +1 == num1

for key in matrix:
    # print(key, key[0], key[1], difference_one(key[0], key[1]))
    pass
#az egyik egyenlőe, és a másik difference_one akkor szomszédok

def nbr(dict, tuple1, tuple2):
    #print(dict)
    #print(tuple)
    if tuple1[0] == tuple2[0] and difference_one(tuple1[1], tuple2[1]) \
            or tuple1[1] == tuple2[1] and difference_one(tuple1[0], tuple2[0]) \
            or difference_one(tuple1[0], tuple2[0]) and difference_one(tuple1[1], tuple2[1]):
        return True
    else:
        return False

neigbours = []
for k,v in matrix.items():
    if nbr(matrix, k, (0,0)):
        neigbours.append([k,v])

neighbor_dict = {k:v for k,v in matrix.items() if nbr(matrix, k, k)}

neighbor_dict = dict.fromkeys(matrix)

print(neighbor_dict)

print(neigbours)

print(nbr(matrix, (0,0), (1,1)))

print(difference_one(7,8))

print(check_key(matrix, (0,0)))

