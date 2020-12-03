def readCoords():
  coords = []

  with open('input') as f:
    coords = [list(line.rstrip()) for line in f.readlines()]

  return coords

def calcTrees(numRight, numDown, coords):
  
  numTrees = 0

  r = 0
  c = 0

  while r < len(coords) - 1:
    c = (c + numRight) % len(coords[0])
    r = r + numDown

    if coords[r][c] == '#': 
      numTrees += 1

  return numTrees

def main():
  
  coords = readCoords()

  numTrees = []

  # Right 1, down 1.
  # Right 3, down 1. (This is the slope you already checked.)
  # Right 5, down 1.
  # Right 7, down 1.
  # Right 1, down 2.

  numTrees.append(calcTrees(1,1,coords))
  numTrees.append(calcTrees(3,1,coords))
  numTrees.append(calcTrees(5,1,coords))
  numTrees.append(calcTrees(7,1,coords))
  numTrees.append(calcTrees(1,2,coords))

  import functools
  result = functools.reduce(lambda a, b: a * b, numTrees)
  
  import sys
  sys.stdout.write(str(result) + '\n')

if __name__ == '__main__':
  main()