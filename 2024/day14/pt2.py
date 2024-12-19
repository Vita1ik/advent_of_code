from helpers import read_input
import re
from functools import reduce
import copy
import os
import time

os.environ['TERM'] = 'xterm'
MOVES_COUNT = 5_000

class Map:
    WIDTH = 101
    HEIGHT = 103

    def __init__(self, robots):
        self.robots = robots

    def display(self):
        map_data = [['.'] * Map.WIDTH for _ in range(Map.HEIGHT)]
        for robot in self.robots:
            map_data[robot.position.y][robot.position.x] = '@'

        for row in map_data:
            print(''.join(row))

    def robots_on_map(self):
        vertical_divider = self.WIDTH // 2
        horizontal_divider = self.HEIGHT // 2
        robots_counts = [0, 0, 0, 0]
        for robot in self.robots:
            x, y = robot.position.x, robot.position.y
            if 0 <= x < vertical_divider and 0 <= y < horizontal_divider:
                robots_counts[0] += 1
            if vertical_divider < x < self.WIDTH and 0 <= y < horizontal_divider:
                robots_counts[1] += 1
            if 0 <= x < vertical_divider and horizontal_divider < y < self.HEIGHT:
                robots_counts[2] += 1
            if vertical_divider < x < self.WIDTH and horizontal_divider < y < self.HEIGHT:
                robots_counts[3] += 1

        return robots_counts



class Dot:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        if x >= Map.WIDTH: x -= Map.WIDTH
        if y >= Map.HEIGHT: y -= Map.HEIGHT
        if x < 0: x += Map.WIDTH
        if y < 0: y += Map.HEIGHT

        return Dot(x, y)

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Robot:
    def __init__(self, position, velocity):
        self._position = Dot(position[0], position[1])
        self._velocity = Dot(velocity[0], velocity[1])

    def move(self):
        self._position += self._velocity

    @property
    def position(self):
        return self._position


robots = []
pattern = r"[pv]=(-?\d+),(-?\d+)"
for line in read_input():
    matches = re.findall(pattern, line)
    result = [[int(x), int(y)] for x, y in matches]
    position, velocity = result
    robots.append(Robot(position, velocity))

min_result = 100000000000
seconds = 0
for step in range(MOVES_COUNT):
    a_map = Map(robots)
    for robot in robots:
        robot.move()
    robots_on_map = a_map.robots_on_map()
    result = reduce(lambda x, y: x * y, robots_on_map)
    if result < min_result:
        min_result = result
        seconds = step
    # if step == 7568:
    #     a_map.display()

print(seconds)
