from itertools import product, starmap, islice


def findNeighbors(grid, x, y):
    xi = (0, -1, 1) if 0 < x < len(grid) - 1 else ((0, -1) if x > 0 else (0, 1))
    yi = (0, -1, 1) if 0 < y < len(grid[0]) - 1 else ((0, -1) if y > 0 else (0, 1))
    return islice(starmap((lambda a, b: grid[x + a][y + b]), product(xi, yi)), 1, None)


class Car():
    def __init__(self, color):
        self.color = color

    def drive(self):
        print('brümm-brümm')


car = Car('red')

grid = [[0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, car, 11],
        [12, 13, 14, 15]]
n = list(findNeighbors(grid, 2, 1))  # 9 szomszédai
print(n)