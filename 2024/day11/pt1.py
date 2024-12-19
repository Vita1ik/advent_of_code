from helpers import read_input

stones = [line.split() for line in read_input()][0]

def apply_rules(stone):
    if stone == 0: return ['1']
    if len(stone) % 2 == 0:
        middle = len(stone) // 2
        return [str(int(stone[:middle])), str(int(stone[middle:]))]
    return [str(int(stone)) * 2024]

for step in range(15):
    new_stones = []
    for stone in stones:
        new_stones += apply_rules(stone)
    stones = new_stones

print(len(stones))