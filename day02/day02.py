def is_valid_part1(entry):
    parts = entry.split()
    min = int(parts[0].split('-')[0])
    max = int(parts[0].split('-')[1])
    count = parts[2].count(parts[1][0])
    return min <= count <= max


def is_valid_part2(entry):
    parts = entry.split()
    first = int(parts[0].split('-')[0]) - 1
    second = int(parts[0].split('-')[1]) - 1
    c = parts[1][0]
    return (parts[2][first] == c) is not (parts[2][second] == c)


with open("input.txt") as file:
    data = file.read().splitlines()

print("PART ONE")
part1 = sum(map(is_valid_part1, data))
print(part1)

print("PART TWO")
part1 = sum(map(is_valid_part2, data))
print(part1)






