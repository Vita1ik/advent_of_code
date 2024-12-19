from helpers import read_input

garden_input = [list(line) for line in read_input()]

class Position:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    def x_y(self):
        return (self.x, self._y)

    def move_top(self, steps=1):
        return Position(self._x, self._y - steps)

    def move_bottom(self, steps=1):
        return Position(self._x, self._y + steps)

    def move_left(self, steps=1):
        return Position(self._x + steps, self._y)

    def move_right(self, steps=1):
        return Position(self._x - steps, self._y)

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Garden:
    def __init__(self, garden_input):
        self._garden = garden_input
        self.assigned_positions = []
        self.regions = []
        self.garden_width = len(garden_input[0])
        self.garden_height = len(garden_input)

    def get_region(self, tree_name):
        return Region(tree_name)

    def task_result(self):
        return sum(region.value() for region in self.regions)

    def inspect_regions(self):
        for y, line in enumerate(self._garden):
            for x, tree_name in enumerate(line):
                tree_position = Position(x, y)
                print(y)

                if tree_position in self.assigned_positions: continue
                region = self.get_region(tree_name)
                self.regions.append(region)
                self.inspect_region(tree_position, region)
        return self.regions


    def inspect_region(self, tree_position, region):
        if 0 <= tree_position.x < self.garden_width and 0 <= tree_position.y < self.garden_height:
            tree_name = self._garden[tree_position.y][tree_position.x]
            if tree_name == region.name and not (tree_position in self.assigned_positions):
                region.add_tree_position(tree_position)
                self.assigned_positions.append(tree_position)
                self.inspect_region(tree_position.move_top(), region)
                self.inspect_region(tree_position.move_bottom(), region)
                self.inspect_region(tree_position.move_right(), region)
                self.inspect_region(tree_position.move_left(), region)


class Region:
    def __init__(self, name):
        self._name = name
        self._trees_positions = []

    @property
    def name(self):
        return self._name

    def add_tree_position(self, position):
        self._trees_positions.append(position)

    def value(self):
        print(self.area() * self.perimeter())
        return self.area() * self.perimeter()

    def area(self):
        return len(self._trees_positions)

    def perimeter(self):
        perimeter_value = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for position in self._trees_positions:
            for dx, dy in directions:
                neighbor = Position(position.x + dx, position.y + dy)
                if neighbor not in self._trees_positions:
                    perimeter_value += 1
        return perimeter_value

    def __repr__(self):
        # return f"Region {self._name} ({[position for position in self._trees_positions]})"
        return f"Region {self._name}"


garden = Garden(garden_input)
garden.inspect_regions()
print(garden.task_result())
# for region in garden.inspect_regions():
#     print(region)
#     print('area =', region.area())
#     print('perimeter =', region.perimeter())