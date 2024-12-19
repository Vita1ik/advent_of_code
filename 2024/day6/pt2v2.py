import sys

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
max_moves = x_len * y_len * 2
print(max_moves)
sys.setrecursionlimit(max_moves + 1)

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

def move(current_x_y, direction, o_barier_x_y = None, allowed_deep = None):
    global max_moves
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
        if a_map[y][x] == '#' or (x, y) == o_barier_x_y:
            direction = new_direction
            x, y = current_x_y

        if allowed_deep:
            allowed_deep -= 1
            if allowed_deep <= 0:
                return 'loop'

        return move((x, y), direction, o_barier_x_y, allowed_deep)


move(guard_x_y, direction)

path_x_y = list(x_y_visited)
path_x_y_len = len(path_x_y)
loops = 0

for index in range(path_x_y_len - 1):
    x, y = path_x_y[index + 1]
    if move(guard_x_y, direction, (x, y), max_moves) == 'loop':
        loops += 1

print(loops)
