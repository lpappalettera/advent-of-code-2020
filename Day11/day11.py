import copy


def occupied_seats(map, x, y, limit_range):
    directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    result = 0
    for dir_x, dir_y in directions:
        searching = True
        row = y
        seat = x
        while searching:
            row += dir_y
            seat += dir_x
            if 0 <= row < h and 0 <= seat < w:
                if map[row][seat] == '#':
                    result += 1
                    searching = False
                elif limit_range or map[row][seat] == 'L':
                    searching = False
            else:
                searching = False
    return result


def updated_map(map, limit, limit_range):
    result = copy.deepcopy(map)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'L':
                result[y][x] = '#' if occupied_seats(map, x, y, limit_range) <= 0 else 'L'
            elif map[y][x] == '#':
                result[y][x] = 'L' if occupied_seats(map, x, y, limit_range) >= limit else '#'
    return result


with open("input.txt") as file:
    data = list(map(list, file.read().splitlines()))

h = len(data)
w = len(data[0])

print('PART ONE')
a = data
b = updated_map(a, 4, True)
while a != b:
    a = b
    b = updated_map(a, 4, True)
print(str(b).count('#'))


print('PART TWO')
a = data
b = updated_map(a, 5, False)
while a != b:
    a = b
    b = updated_map(a, 5, False)
print(str(b).count('#'))
