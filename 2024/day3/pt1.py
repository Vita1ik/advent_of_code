import re

with open("input.txt", "r") as file:
    text = file.read()

pattern = r"mul\((\d+),(\d+)\)"
numbers = sum(int(a) * int(b) for a, b in re.findall(pattern, text))

print(numbers)
