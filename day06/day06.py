def answers_by_group(everyone):
    groups = []
    start_of_group = True
    for i, line in enumerate(data):
        if start_of_group:
            groups.append(set(line))
            start_of_group = False
        elif line != '' and not everyone:
            groups[-1] = groups[-1] | set(line)
        elif line != '' and everyone:
            groups[-1] = groups[-1].intersection(set(line))
        else:
            start_of_group = True
    return groups


with open("input.txt") as file:
    data = file.read().splitlines()

print("PART ONE")
part1 = sum([len(group) for group in answers_by_group(False)])
print(part1)

print("PART TWO")
part2 = sum([len(group) for group in answers_by_group(True)])
print(part2)
