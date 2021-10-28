import math    
directOrbits = {}       # A : [B] if B orbits A
orbits = open("input.in", "r").read().strip().split("\n")

for orbit in orbits:  #Build directory of relations
  a,b = orbit.split(")")
  if a in directOrbits:
    directOrbits[a].append(b)
  else:
    directOrbits[a] = [b]

def calcOrbiting(): # from top of tree, traverse layer by layer and increase orbiting accordingly
  current = set(["COM"])
  depth = 0
  orbiting = 0

  while current:
    next = set()
    for c in current:
      if c in directOrbits.keys():
        next.update(directOrbits[c])

    orbiting += len(current) * depth
    depth += 1
    current = next
  
  return orbiting

print("Part1:", calcOrbiting())

neighbours = directOrbits.copy()      # Directory on Form A : [neighbour] (planet A orbits and planets orbiting A)

for k,v in directOrbits.items():
  for value in v:
    if value in neighbours.keys():
      neighbours[value].append(k)
    else:
      neighbours[value] = [k]

def findSanta():
  depth = 0
  current = neighbours["YOU"] # Start at planets closest to YOU
  visited = set(current)      #Set of visited planets

  while "SAN" not in current:   #Calc number of steps to find SAN
    depth += 1
    next = set()
    for c in current:
      for n in neighbours[c]:
        if n not in visited:
          visited.add(n)
          next.add(n)

    current = next
  return depth - 1

print("Part2:", findSanta())






