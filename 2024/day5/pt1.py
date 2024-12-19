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

correct_updates = []

for update in input:
    if is_rule_valid(update):
        correct_updates.append(update)

sum = 0
for update in correct_updates:
    sum += int(update[int((len(update) / 2))])

print(sum)
