import math    

directions = { 'R': (0,1), 'L': (0,-1), 'U': (1,0), 'D': (-1,0) }

wires = open("input.in", "r").read().strip().split("\n")
wire0 = wires[0].split(",")
wire1 = wires[1].split(",")

coordinatesWire0 = {}
x,y = 0,0
steps = 0

for turn in wire0:
  dir = directions[turn[0]]
  value = int(turn[1:])
  for i in range(value):
    steps += 1
    x += dir[0] 
    y += dir[1]
    coordinatesWire0[(x,y)] = steps   

intersections = {}
x, y = 0,0
steps = 0

for turn in wire1:
  dir = directions[turn[0]]
  value = int(turn[1:])
  for i in range(value):
    steps += 1
    x += dir[0] 
    y += dir[1]
    if (x,y) in coordinatesWire0:
      intersections[(x,y)] = coordinatesWire0[(x,y)] + steps


part1 = min([abs(x[0]) + abs(x[1]) for x in intersections.keys()])
part2 = min(intersections.values())

print("Part1: ", part1)
print("Part2: ", part2)





