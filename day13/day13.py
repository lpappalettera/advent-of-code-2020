with open("input.txt") as file:
    data = file.read().splitlines()

timestamp = int(data[0])
busses = data[1].split(',')

print('PART ONE')
filtered_busses = list(map(int, filter(lambda x: x != 'x', busses)))
durations = [(bus, bus - timestamp % bus) for bus in filtered_busses]
earliest = durations[0]
for option in durations:
    if option[1] < earliest[1]:
        earliest = option
print(earliest[0] * earliest[1])
    