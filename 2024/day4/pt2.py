input = []

with open("test_input.txt", "r") as file:
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
        if input[y][x] == 'A':
            n = 0
            if char_at_is(x - 1, y - 1, 'M') and char_at_is(x + 1, y + 1, 'S'):
                n += 1
            if char_at_is(x + 1, y - 1, 'M') and char_at_is(x - 1, y + 1, 'S'):
                n += 1
            if char_at_is(x - 1, y - 1, 'S') and char_at_is(x + 1, y + 1, 'M'):
                n += 1
            if char_at_is(x + 1, y - 1, 'S') and char_at_is(x - 1, y + 1, 'M'):
                n += 1
            if n == 2:
                count += 1

print(count)
