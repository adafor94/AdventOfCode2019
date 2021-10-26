import math    

def calc_fuel(module):
  fuel = math.floor(int(module)/3) - 2
  return fuel + calc_fuel(fuel) if fuel > 0 else 0

modules = open("input.in", "r").read().strip().split("\n")
part1 = sum([math.floor(int(module)/3) - 2 for module in modules])
part2 = sum([calc_fuel(int(module)) for module in modules])
print("Part1: ", part1)
print("Part2: ", part2)