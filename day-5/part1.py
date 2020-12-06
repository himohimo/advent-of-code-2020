def readLines(fileName):

  with open(fileName) as f:
    return [line.rstrip() for line in f.readlines()]

def calcRow(inputStr):
  l = 0
  r = 127

  for c in inputStr:

    mid = (l + r) // 2

    if c == 'F':
      r = mid
    else:
      l = mid

  return l + 1 if inputStr[-1] == 'F' else r

def calcCol(inputStr):
  l = 0
  r = 7

  for c in inputStr:

    mid = (l + r) // 2

    if c == 'L':
      r = mid
    else:
      l = mid

  return l + 1 if inputStr[-1] == 'L' else r


def main():
  import re
  import sys

  maxSeatId = 0

  lines = readLines('input')
  for l in lines:
    row = calcRow(l[:7])
    col = calcCol(l[7:])

    maxSeatId = max(maxSeatId, row * 8 + col)

  sys.stdout.write(str(maxSeatId) + '\n')
  return maxSeatId

if __name__ == '__main__':
  main()