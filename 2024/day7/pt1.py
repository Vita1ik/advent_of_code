from math import prod
import itertools

input = []
# 7220004747874
# 7220004747874
# 12839443280319
with open("input.txt", "r") as file:
    for line in file:
        result, numbers = line.replace("\n", "").split(':')
        input.append([int(result), list(map(int, numbers.split()))])


def is_valid(result, numbers):
    # print(numbers)
    numbers_len = len(numbers)
    min = sum(numbers)
    max = prod(numbers)
    operands_list = [''.join(comb) for comb in itertools.product('+*|', repeat=numbers_len-1)]
    results = [min, max]
    if result in results:
        return True
    else:
        for operands in operands_list:
            # print(operands)
            numbers_copy = numbers[:]
            prev_value = numbers_copy[0]
            for index, operand in enumerate(operands):
                numbers_copy[index] = prev_value
                if operand == '+':
                    # print('+'.join(map(str, numbers_copy[index:index+2])))
                    prev_value = sum(numbers_copy[index:index+2])
                if operand == '*':
                    # print('*'.join(map(str, numbers_copy[index:index+2])))
                    prev_value = prod(numbers_copy[index:index+2])
            results.append(prev_value)

        return result in results

valid_results = []
for result, numbers in input:
    if is_valid(result, numbers):
        valid_results.append(result)


print(sum(valid_results))
