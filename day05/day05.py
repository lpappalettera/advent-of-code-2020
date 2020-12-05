import math


def middle(a, b):
    return int(math.ceil((b - a) / 2))


def calc_id(ticket):
    row = [0, 127]
    column = [0, 7]
    for c in ticket:
        if c == 'F':
            row[1] = row[1] - middle(row[0], row[1])
        elif c == 'B':
            row[0] = row[0] + middle(row[0], row[1])
        elif c == 'L':
            column[1] = column[1] - middle(column[0], column[1])
        elif c == 'R':
            column[0] = column[0] + middle(column[0], column[1])
    return row[0] * 8 + column[1]


def my_seat(taken, empty):
    for spot in empty:
        if spot - 1 in ids and spot + 1 in taken:
            return spot


def all_ids():
    spots = set()
    for r in range(127):
        for c in range(7):
            spots.add(r * 8 + c)
    return spots


with open("input.txt") as file:
    data = file.read().splitlines()

ids = list(map(calc_id, data))
empty_seats = list(set(all_ids()) - set(ids))

print("PART ONE")
part1 = max(ids)
print(part1)

print("PART TWO")
part2 = my_seat(ids, empty_seats)
print(part2)
