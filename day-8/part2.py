def readLines(fileName):

  with open(fileName) as f:
    return [line.rstrip() for line in f.readlines()]

def parseLines(lines):
  import re

  ops = []
  
  for l in lines:
    match = re.search('(acc|jmp|nop)\s([+-])([\d]+)', l)
    op, sign, value = match.groups()

    value = int(value) * -1 if sign == '-' else int(value)

    ops.append((op, value))

  return ops


def main():
  import sys

  lines = readLines('input')
  ops = parseLines(lines)


  for i in range(len(ops)):
    accumulator = 0
    currentPC = 0
    seenPC = set()

    while currentPC not in seenPC and currentPC < len(ops):
      seenPC.add(currentPC)

      # print('-', i, currentPC, len(ops), seenPC)
      op, value = ops[currentPC]

      if currentPC == i:
        if op == 'nop': op = 'jmp'
        elif op == 'jmp': op = 'nop'

      if op == 'nop':
        currentPC += 1
      elif op == 'acc':
        accumulator += value
        currentPC += 1
      elif op == 'jmp':
        currentPC += value

    if currentPC >= len(ops):
      # print(i, accumulator)
      sys.stdout.write(str(accumulator) + '\n')
      return accumulator 

if __name__ == '__main__':
  main()