reports = []
safe_reports = 0

with open("input.txt", "r") as file:
    for line in file:
        reports.append(list(map(int, line.split())))

for line in reports:
    increasing = line[0] < line[1]
    safe = True
    print(line)
    for index, number in enumerate(line[1:], start=1):
        prev_number = line[index - 1]
        diff = prev_number - number
        if abs(diff) > 3 or diff == 0 or (increasing and diff > 0) or (increasing == False and diff < 0):
            safe = False
    if safe:
        safe_reports += 1


print(safe_reports)
