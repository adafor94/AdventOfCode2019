import math    
import itertools
import threading

mem = open("input.in", "r").read().strip().split(",")
inputs = [[],[],[],[],[]]     #input vectors for each thread
locks = []                    #locks for each thread
for i in range(5):
  locks.append(threading.Condition())
outputs = []                  #output list

def parseInstruction(instruction):
  opcode = ('0' + instruction[-2:])[-2:]    #Adding leading 0 if needed
  paramModes = instruction[0:-2][::-1]      #Fetching and reversing the modes
  return opcode, paramModes

def fetchValues(mem, modes, pc, number_params): 
  params = mem[pc+1 : pc+1+number_params]
  values = []
  for i in range(len(params)):
    if i >= len(modes):
      values.append(int(mem[int(params[i])]))
    elif modes[i] == '0':
      values.append(int(mem[int(params[i])]))
    else:
      values.append(int(params[i]))
  return values

def runProgram(mem, inputs, locks, index):
  my_input, my_lock = inputs[index], locks[index]
  lastOutput, number_params, pc = 0, 0, 0     #Default values

  while(1):
    opcode, paramModes = parseInstruction(mem[pc])

    if opcode == "01":    #ADD src src dst
      number_params = 3
      paramValues = fetchValues(mem, paramModes, pc, number_params) 
      mem[int(mem[pc+number_params])] = str(paramValues[0] + paramValues[1])

    elif opcode == "02":  #MUL src src dst
      number_params = 3
      paramValues = fetchValues(mem, paramModes, pc, number_params) 
      mem[int(mem[pc+number_params])] = str(paramValues[0] * paramValues[1])

    elif opcode == "03":  #INPUT dst
      number_params = 1
      my_lock.acquire()
      while not my_input:
        my_lock.wait()
        
      value = my_input.pop(0)
      my_lock.release()
      mem[int(mem[pc+1])] = value

    elif opcode == "04":  #PRINT src
      number_params = 1
      lastOutput = fetchValues(mem, paramModes, pc, number_params)[0]
      
      lock = locks[(index+1)%5]
      lock.acquire()
      inputs[(index+1)%5].append(lastOutput)
      lock.notifyAll()
      lock.release()

    elif opcode == "05":  #JUMP cond dst
      number_params = 2
      paramValues = fetchValues(mem, paramModes, pc, number_params) 
      if paramValues[0]:
        pc = paramValues[1]
        continue

    elif opcode == "06":  #JUMP !cond dst
        number_params = 2
        paramValues = fetchValues(mem, paramModes, pc, number_params) 
        if not paramValues[0]:
          pc = paramValues[1]
          continue

    elif opcode == "07":  #param2 = parm1 < param2
      number_params = 3
      paramValues = fetchValues(mem, paramModes, pc, number_params) 
      mem[int(mem[pc+number_params])] = paramValues[0] < paramValues[1]

    elif opcode == "08":  #param2 = param1 == param2
      number_params = 3
      paramValues = fetchValues(mem, paramModes, pc, number_params) 
      mem[int(mem[pc+number_params])] = paramValues[0] == paramValues[1]

    elif opcode == "99":  #HALT
      if index == 4:
        outputs.append(lastOutput)
      return 
    else:
      print("ERROR! Opcode:", opcode)

    pc += 1 + number_params


def calcHighestSignal(phaseSettings):
  combinations = list(itertools.permutations(phaseSettings))    #Calc all permutations

  for combination in combinations:          #try each combination
    inputs = [[],[],[],[],[]]               #Reset input vectors
    for i in range(len(combination)):       #Start values for each thread/"amplifier"
      inputs[i].append(combination[i])      
    inputs[0].append(0)                     #Start input value to first thread/amplifier
    t = 0
    for i in range(5):
      t = threading.Thread(target= runProgram, args= (mem.copy(), inputs, locks, i)) #Start one thread for each amplifier
      t.start()
    t.join()

calcHighestSignal([0,1,2,3,4])
print("Part1:", max(outputs))
outputs = []  #Reset output list

calcHighestSignal([5,6,7,8,9])
print("Part2:", max(outputs))






