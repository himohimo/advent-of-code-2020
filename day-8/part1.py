def readLines(fileName):

  with open(fileName) as f:
    return [line.rstrip() for line in f.readlines()]

def main():
  import re
  import sys

  lines = readLines('input')

  accumulator = 0
  currentPC = 0
  seenPC = set()

  while currentPC not in seenPC:
    
    seenPC.add(currentPC)

    match = re.search('(acc|jmp|nop)\s([+-])([\d]+)', lines[currentPC])

    op, sign, value = match.groups()
    # print(op, sign, value)

    value = int(value) * -1 if sign == '-' else int(value)

    if op == 'nop':
      currentPC += 1
    elif op == 'acc':
      accumulator += value
      currentPC += 1
    elif op == 'jmp':
      currentPC += value
  # print(accumulator)
  
  sys.stdout.write(str(accumulator) + '\n')

if __name__ == '__main__':
  main()