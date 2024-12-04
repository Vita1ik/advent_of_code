list1 = []
list2 = []
distances = []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

lists_len = len(list1)

def next_min_element(list):
    min_el = min(element for element in list if element is not None)
    index = list.index(min_el)
    list[index] = None
    return min_el

for _ in range(lists_len):
    element1 = next_min_element(list1)
    element2 = next_min_element(list2)
    distance = abs(element1 - element2)
    distances.append(distance)

print(sum(distances))
