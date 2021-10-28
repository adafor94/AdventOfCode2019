import math    

def parseInstruction(instruction):
  opcode = ('0' + instruction[-2:])[-2:]    #Adding leading 0 if needed
  paramModes = instruction[0:-2][::-1]      #Fetching and reversing the modes
  return opcode, paramModes

def fetchValues(mem, modes, pc, number_params): #params):
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


def runProgram(mem):
  number_params = 0
  pc = 0                                      #program counter

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
      value = input("Enter input value: ")
      mem[int(mem[pc+1])] = value
    elif opcode == "04":  #PRINT src
      number_params = 1
      value = fetchValues(mem, paramModes, pc, number_params)[0] 
      print(value)
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
      return
    else:
      print("ERROR! Opcode:", opcode)

    pc += 1 + number_params

mem = open("input.in", "r").read().strip().split(",")
runProgram(mem)

## Enter input 1 to get answer to part 1
## Enter input 5 to get answer to part 2






