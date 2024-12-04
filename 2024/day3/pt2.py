import re

CALC_PATTERN = r"mul\((\d+),(\d+)\)"

with open("input.txt", "r") as file:
    input = file.read()

def calculate_result(text):
    return sum(int(a) * int(b) for a, b in re.findall(CALC_PATTERN, text))

parts = input.split('do()')
enabled_parts = list(part.split("don't()")[0] for part in parts)
calculated_enabled_parts = sum(calculate_result(part) for part in enabled_parts)
print('calculated_enabled_parts = ', calculated_enabled_parts)
