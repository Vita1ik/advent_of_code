from helpers import read_input

input = [line for line in read_input()]
trailheads = []
RIGHT = 'right'
LEFT = 'left'
TOP = 'top'
BOTTOM = 'bottom'
DIRECTIONS = [RIGHT, LEFT, TOP, BOTTOM]

max_y = len(input)
max_x = len(input[0])

for y, line in enumerate(input):
    for x, number in enumerate(line):
        if number == '0':
            trailheads.append((x, y))

trailheads_score = []

def move_to(direction, x, y):
    if direction == RIGHT: return (x + 1, y)
    if direction == LEFT: return (x - 1, y)
    if direction == TOP: return (x, y - 1)
    if direction == BOTTOM: return (x, y + 1)

def is_allowed_move(x, y, next_x, next_y):
    if 0 <= next_x < max_x and 0 <= next_y < max_y:
        return int(input[next_y][next_x]) - int(input[y][x]) == 1
    return False


def move_next(x, y):
    if input[y][x] == '9':
        reached_highes.add((x, y))

    for direction in DIRECTIONS:
        x_new, y_new = move_to(direction, x, y)
        if is_allowed_move(x, y, x_new, y_new):
            move_next(x_new, y_new)


highes_sum = 0
for x, y in trailheads:
    reached_highes = set()
    move_next(x, y)
    highes_sum += len(reached_highes)

print(highes_sum)
