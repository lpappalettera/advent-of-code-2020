with open("input.txt") as file:
    data = file.read().splitlines()

print('PART ONE')
x = 0
y = 0
d = 90

for it in data:
    action = it[0]
    value = int(it[1:])
    if action == 'N' or (action == 'F' and d % 360 == 0):
        y += value
    elif action == 'S' or (action == 'F' and d % 360 == 180):
        y -= value
    elif action == 'E' or (action == 'F' and d % 360 == 90):
        x += value
    elif action == 'W' or (action == 'F' and d % 360 == 270):
        x -= value
    elif action == 'L':
        d -= value
    elif action == 'R':
        d += value
print(abs(x) + abs(y))

print('PART TWO')
x = 0
y = 0
wp_x = 10
wp_y = 1

for it in data:
    action = it[0]
    value = int(it[1:])
    if action == 'N':
        wp_y += value
    elif action == 'S':
        wp_y -= value
    elif action == 'E':
        wp_x += value
    elif action == 'W':
        wp_x -= value
    elif (action == 'L' and 360 - value == 90) or (action == 'R' and value == 90):
        wp = (wp_x, wp_y)
        wp_x = wp[1]
        wp_y = -wp[0]
    elif (action == 'L' and 360 - value == 180) or (action == 'R' and value == 180):
        wp = (wp_x, wp_y)
        wp_x = -wp[0]
        wp_y = -wp[1]
    elif (action == 'L' and 360 - value == 270) or (action == 'R' and value == 270):
        wp = (wp_x, wp_y)
        wp_x = -wp[1]
        wp_y = wp[0]
    elif action == 'F':
        x += value * wp_x
        y += value * wp_y
print(abs(x) + abs(y))
