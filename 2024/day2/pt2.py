
# 303
# 304
# 308
def import_data():
    reports = []
    with open("input.txt", "r") as file:
        for line in file:
            reports.append(list(map(int, line.split())))
    return reports


def count_safe_reports(reports):
    safe_reports = 0
    for line in reports:
        comparations = list(line[index - 1] < number for index, number in enumerate(line[1:], start=1))
        increasing = comparations.count(True) > comparations.count(False)
        safe = True
        bad_levels = 0
        index_sup = 1
        for index, number in enumerate(line[1:], start=1):
            prev_number = line[index - index_sup]
            next_number = None
            if index + 1 < len(line):
                next_number = line[index + 1]
            index_sup = 1
            diff = prev_number - number
            if abs(diff) > 3 or diff == 0 or (increasing and (diff > 0 or (next_number and next_number < number and next_number > prev_number))) or (increasing == False and (diff < 0 or (next_number and next_number > number and next_number < prev_number))):
                if bad_levels == 0:
                    next_diff = None
                    if index + 1 < len(line):
                        next_diff = prev_number - line[index + 1]
                    if (increasing and diff > 0) or (not increasing and diff < 0):
                        if (next_diff and abs(next_diff) <= 3) or index > 1:
                            index_sup = 2
                        else:
                            index_sup = 1
                    elif (not increasing and diff > 0) or (increasing and diff < 0):
                        if (next_diff and abs(next_diff) <= 3) or index > 1:
                            index_sup = 2
                        else:
                            index_sup = 1

                else:
                    safe = False
                bad_levels += 1
        if safe:
            safe_reports += 1

    return safe_reports

# print(count_safe_reports(import_data()))
