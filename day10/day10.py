with open("input.txt") as file:
    data = list(map(int, file.read().splitlines()))

data.append(0)
data.sort()

print("PART ONE")
min_adapters = 0
max_adapters = 1
for i in range(1, len(data)):
    adapter = data[i] - data[i-1]
    if adapter == 1:
        min_adapters += 1
    elif adapter == 3:
        max_adapters += 1
print(min_adapters * max_adapters)

print("PART TWO")
routes = [0] * (max(data) + 1)
routes[0] = 1
for adapter in data:
    for option in range(1, 4):
        if adapter - option >= 0:
            routes[adapter] += routes[adapter - option]
print(routes[-1])

