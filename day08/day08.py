def move(line, fix=-1):
    instructions.add(line)
    action = data[line].split()[0]
    arg = int(data[line].split()[1])
    if action == 'acc':
        global accumulator
        accumulator += arg
        return line + 1
    elif line == fix and action == 'jmp':
        return line + 1
    elif line == fix and action == 'nop':
        return line + arg
    elif action == 'jmp':
        return line + arg
    else:
        return line + 1


def next_fix_line(line=0):
    while line < len(data):
        action = data[line].split()[0]
        if action == 'jmp' or action == 'nop':
            return line
        else:
            line += 1


with open("input.txt") as file:
    data = file.read().splitlines()

accumulator = 0
instructions = set()
position = 0

print('PART ONE')
while position not in instructions:
    position = move(position)
print(accumulator)

print('PART TWO')
fix_line = next_fix_line()
while position < len(data):
    accumulator = 0
    instructions = set()
    position = 0
    while position not in instructions and position < len(data):
        position = move(position, fix_line)
    fix_line = next_fix_line(fix_line+1)
print(accumulator)
