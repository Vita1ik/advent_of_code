input = []

with open("input.txt", "r") as file:
    for line in file:
        input.append(line.replace("\n", ""))

def char_at_is(column, row, expected_value):
    if column < 0 or row < 0:
        return False
    try:
        return input[row][column] == expected_value
    except IndexError:
        return False

x_len = len(input[0])
y_len = len(input)
count = 0

for y in range(y_len):
    for x in range(x_len):
        if input[y][x] == 'X':
            if char_at_is(x - 1, y, 'M'):
                if char_at_is(x - 2, y, 'A'):
                    if char_at_is(x - 3, y, 'S'):
                        count += 1
            if char_at_is(x - 1, y - 1, 'M'):
                if char_at_is(x - 2, y - 2, 'A'):
                    if char_at_is(x - 3, y - 3, 'S'):
                        count += 1
            if char_at_is(x, y - 1, 'M'):
                if char_at_is(x, y - 2, 'A'):
                    if char_at_is(x, y - 3, 'S'):
                        count += 1
            if char_at_is(x + 1, y - 1, 'M'):
                if char_at_is(x + 2, y - 2, 'A'):
                    if char_at_is(x + 3, y - 3, 'S'):
                        count += 1
            if char_at_is(x + 1, y, 'M'):
                if char_at_is(x + 2, y, 'A'):
                    if char_at_is(x + 3, y, 'S'):
                        count += 1
            if char_at_is(x + 1, y + 1, 'M'):
                if char_at_is(x + 2, y + 2, 'A'):
                    if char_at_is(x + 3, y + 3, 'S'):
                        count += 1
            if char_at_is(x, y + 1, 'M'):
                if char_at_is(x, y + 2, 'A'):
                    if char_at_is(x, y + 3, 'S'):
                        count += 1
            if char_at_is(x - 1, y + 1, 'M'):
                if char_at_is(x - 2, y + 2, 'A'):
                    if char_at_is(x - 3, y + 3, 'S'):
                        count += 1

print(count)
