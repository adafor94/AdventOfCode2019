import math    

STEPS = 4
OUTPUT = 19690720

def runProgram(mem):
  pc = 0
  while(1):
    opcode = mem[pc]
    if opcode == 1:
      mem[mem[pc+3]] = mem[mem[pc+1]] + mem[mem[pc+2]]
    elif opcode == 2:
      mem[mem[pc+3]] = mem[mem[pc+1]] * mem[mem[pc+2]]
    elif opcode == 99:
      return
    pc += STEPS

def find(default_mem, output):
  for i in range(99):
    for j in range(99):  
      mem = default_mem.copy()
      mem[1] = i
      mem[2] = j
      runProgram(mem)
      if(mem[0] == output):
        print("Part2: ", 100 * i + j)
        return



default_mem = open("input.in", "r").read().strip().split(",")
default_mem = [int(x) for x in default_mem]
mem = default_mem.copy()

#PART 1
noun = 12
verb = 2
mem[1] = noun
mem[2] = verb

runProgram(mem)
print("Part1: ", mem[0])

#PART 2
find(default_mem, OUTPUT)





