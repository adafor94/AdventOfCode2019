import math    

RANGE = range(382345,843167+1)    #pussle input

part1, part2 = 0, 0

def checkBack(number, pos):
    return pos < 2 or int(str(number)[pos-1]) != int(str(number)[pos-2])

def checkForward(number, pos):
    return pos > 4 or int(str(number)[pos]) != int(str(number)[pos+1])

for number in RANGE:
  adjacentPart1 = 0
  adjacentPart2 = 0
  for pos in range(1,6):
    current = int(str(number)[pos])
    prev = int(str(number)[pos-1])
    if current < prev:
      adjacentPart1 = 0
      adjacentPart2 = 0
      break
    else:
      if current == prev:
        adjacentPart1 = 1
        if checkBack(number,pos) and checkForward(number,pos):
          adjacentPart2 = 1

  part1 += adjacentPart1
  part2 += adjacentPart2

print("Part1:", part1)
print("Part2:", part2)






