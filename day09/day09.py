def is_valid(value, preamble):
    preamble = set(preamble)
    return any(value - i in preamble for i in preamble)


with open("input.txt") as file:
    data = list(map(int, file.read().splitlines()))

print('PART ONE')
preamble_len = 25
i = preamble_len
while is_valid(data[i], data[i-preamble_len:i]):
    i += 1
part1 = data[i]
print(part1)

print('PART TWO')
longest = []
for it in range(len(data)):
    values = []
    p = it
    while sum(values) < part1:
        values.append(data[p])
        p += 1
        if sum(values) == part1 and len(values) > len(longest):
            longest = values
print(min(longest) + max(longest))
