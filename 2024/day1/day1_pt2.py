list1 = []
list2 = []
counts = []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

for element1 in list1:
    counts.append(element1 * list2.count(element1))

print(sum(counts))
