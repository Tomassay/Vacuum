
rows, cols = 3, 3


matrix = {(row, col): 0 for row in range(rows) for col in range(cols)}

matrix[2,2] = 1


matrix[0,0], matrix[2,2] = matrix[2,2], matrix[0,0]

def difference_one(num1, num2):
    return num1 + 1 == num2 or num2 +1 == num1

def nbr(tuple1, tuple2):
    #print(dict)
    #print(tuple)
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
    #print(neigbours)
    return neigbours

#neighbor_dict = {k:v for k,v in matrix.items() if nbr(matrix, k, k)}

#neighbor_dict = {k: [v for v in len(matrix.keys()) if nbr(matrix, v, k)] in matrix.keys() }


#print(matrix, (1,1), (0,0))
#print(len(matrix.keys()))

#G = { k: [v for v in range(n) if v != k] for k in range(n) }

#print(neighbor_dict)

#print(neigbours)

nbr_dict = dict.fromkeys(matrix)

for key, value in matrix.items():
   nbr_dict[key] = nbr_list(matrix, key)
    #nbr[key] = nbr_list(matrix, key)


print(matrix)
print(nbr_dict)
# print(nbr(matrix, (0,0), (1,1)))
# print(nbr_list(matrix,(0,0)))
#
# print(difference_one(7,8))
#
# print(check_key(matrix, (0,0)))

