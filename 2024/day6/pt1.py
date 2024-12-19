import sys

sys.setrecursionlimit(1_000_000_000)

input = []

with open("input.txt", "r") as file:
    for line in file:
        input.append(line.replace("\n", ""))

a_map = input
guard_x_y = None
direction = None
x_len = len(a_map[0])
y_len = len(a_map)
x_y_visited = set()
print(a_map)
for y, line in enumerate(a_map):
    for x, char in enumerate(line):
        if char == '^':
            guard_x_y = (x, y)
            direction = 'up'
        if char == '>':
            guard_x_y = (x, y)
            direction = 'right'
        if char == '<':
            guard_x_y = (x, y)
            direction = 'left'
        if char == 'v':
            guard_x_y = (x, y)
            direction = 'down'
print(guard_x_y)
print(direction)

def move(current_x_y, direction):
    # print(current_x_y)
    x_y_visited.add(current_x_y)
    x, y = current_x_y

    if direction == 'up':
        new_direction = 'right'
        y -= 1
    elif direction == 'right':
        new_direction = 'down'
        x += 1
    elif direction == 'left':
        new_direction = 'up'
        x -= 1
    elif direction == 'down':
        new_direction = 'left'
        y += 1

    if x >= 0 and y >= 0 and x < x_len and y < y_len:
        if a_map[y][x] == '#':
            direction = new_direction
            x, y = current_x_y


        move((x, y), direction)

move(guard_x_y, direction)
print(len(x_y_visited))
