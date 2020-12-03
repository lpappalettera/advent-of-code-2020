import math


def count_trees(m, x_step_size, y_step_size):
    result = 0
    y_length = len(m)
    x_length = len(m[0])
    for i in range(int(y_length / y_step_size)):
        x = i * x_step_size % x_length
        y = i * y_step_size
        if m[y][x] == '#':
            result += 1
    return result


with open("input.txt") as file:
    data = file.read().splitlines()

print("PART ONE")
part1 = count_trees(data, 3, 1)
print(part1)

print("PART TWO")
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
part2 = math.prod([count_trees(data, slope[0], slope[1]) for slope in slopes])
print(part2)
