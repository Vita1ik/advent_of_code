from functools import cache
from helpers import read_input, measure_time

STEPS = 75
stones = [list(map(int, line.split())) for line in read_input()][0]

ranges_list = []
def generate_ranges():
    global ranges_list
    for rang in range(0, 15):
        step = 100**rang
        first_edge = 10 * step
        ranges_list.append([range(first_edge, step*100), 10**(rang+1)])
generate_ranges()

@cache
def splited_numbers(stone):
    for range, value in ranges_list:
        if stone < range[0]: break
        if stone in range: return [stone // value, stone % value]


@cache
def count_stones(stone, deep = 0):
    if deep == STEPS: return 1
    if stone == 0: return count_stones(1, deep + 1)
    numbers = splited_numbers(stone)
    if numbers:
        stone1, stone2 = numbers
        return count_stones(stone1, deep + 1) + count_stones(stone2, deep + 1)
    return count_stones(stone * 2024, deep + 1)


with measure_time():
    stones_count = sum(count_stones(stone) for stone in stones)

print(stones_count)