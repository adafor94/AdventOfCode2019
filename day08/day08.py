import math    
import itertools
import threading

WIDE = 25
TALL = 6
PIXELS_PER_LAYER = WIDE*TALL
pixels = open("input.in", "r").read().strip()

unknownIndexes = set(range(PIXELS_PER_LAYER))
known = [0] * (WIDE*TALL)

zeros, ones, twos = PIXELS_PER_LAYER, PIXELS_PER_LAYER, PIXELS_PER_LAYER
index, current0, current1, current2 = 0,0,0,0

for pix in pixels:
  #For part1
  current0 += pix == '0'
  current1 += pix == '1'
  current2 += pix == '2'
  
  if index == WIDE*TALL - 1:                  #LAYER DONE
    if current0 < zeros:                      #if new low -> update
      zeros = current0
      ones = current1
      twos = current2

    current0, current1, current2 = 0,0,0    #Reset count

  #For part2
  if index in unknownIndexes:
    if pix == '0' or pix == '1':
      known[index] = pix
      unknownIndexes.remove(index)

  index = (index+1) % (PIXELS_PER_LAYER)           #Update index

print("Part1:", ones*twos)
s = ''.join(known).replace('1','x').replace('0',' ')      #replacing for clarity
print("Part2:")
for i in range(0, PIXELS_PER_LAYER, WIDE):
  print(s[i:i+WIDE])
  




