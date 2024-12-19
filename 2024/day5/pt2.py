input = []
rules = []

with open("input.txt", "r") as file:
    for line in file:
        input.append(line.replace("\n", "").split(','))

with open("rules_input.txt", "r") as file:
    for line in file:
        rules.append(line.replace("\n", ""))

def is_rule_valid(update):
    for rule in rules:
        x, y = rule.split('|')

        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def correct_invaled_update(update):
    for rule in rules:
        x, y = rule.split('|')
        if x in update and y in update:
            x_index = update.index(x)
            y_index = update.index(y)
            if x_index > y_index:
                update[x_index] = y
                update[y_index] = x

# 5440

invalid_updates = []
for update in input:
    if not is_rule_valid(update):
        invalid_updates.append(update)

for _ in range(len(invalid_updates)):
    for update in invalid_updates:
        correct_invaled_update(update)

sum = 0
for update in invalid_updates:
    sum += int(update[int((len(update) / 2))])


print(sum)
