def calc_answer_part1(entries):
    for x in entries:
        for y in entries:
            if x + y == 2020:
                return x * y


def calc_answer_part2(entries):
    for x in entries:
        for y in entries:
            for z in entries:
                if x + y + z == 2020:
                    return x * y * z


with open("input.txt") as file:
    data = file.read().splitlines()

data = list(map(int, data))

print("PART ONE")
part1 = calc_answer_part1(data)
print(part1)

print("PART TWO")
part1 = calc_answer_part2(data)
print(part1)








