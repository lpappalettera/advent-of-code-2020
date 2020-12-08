def parse(records):
    bags = dict()
    for r in records:
        r = r.split(' bags contain ')
        bags[r[0]] = dict()
        for b in r[1].split(', '):
            first_space = b.find(' ')
            last_space = b.rfind(' ')
            bags[r[0]][b[first_space + 1:last_space]] = 0 if b[:first_space] == 'no' else int(b[:first_space])
    return bags


def contains(bag, name):
    if bag in data:
        return name in data[bag] or any([contains(it, name) for it in data[bag]])
    else:
        return False


def count(bag):
    if bag in data:
        return sum([data[bag][it] + data[bag][it] * count(it) for it in data[bag]])
    else:
        return 0


with open("input.txt") as file:
    data = parse(file.read().splitlines())


print("PART ONE")
part1 = sum([contains(it, 'shiny gold') for it in data])
print(part1)

print("PART TWO")
part2 = count('shiny gold')
print(part2)

