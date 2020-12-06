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

  return mid if inputStr[-1] == 'F' else r

def calcCol(inputStr):
  l = 0
  r = 7

  for c in inputStr:

    mid = (l + r) // 2

    if c == 'L':
      r = mid
    else:
      l = mid

  return mid if inputStr[-1] == 'L' else r


def main():
  import sys

  seatList = []

  lines = readLines('input')
  for l in lines:
    row = calcRow(l[:7])
    col = calcCol(l[7:])

    seatList.append(row * 8 + col)

  minSeatId, maxSeatId = min(seatList), max(seatList)

  for val in range(minSeatId, maxSeatId):

    if val not in seatList and val + 1 in seatList and val - 1 in seatList:
      sys.stdout.write(str(val) + '\n')
      return val

if __name__ == '__main__':
  main()