def readCoordinates(fileName):
    coords = []

    with open(fileName) as f:
        coords = [list(line.rstrip()) for line in f.readlines()]

    return coords

def main():
    import sys

    coords = readCoordinates('input')

    numTrees = 0

    xCoord = 0
    yCoord = 0

    while yCoord < len(coords) - 1:

      xCoord = (xCoord + 3) % len(coords[0])
      yCoord += 1

      if coords[yCoord][xCoord] == '#':
        numTrees += 1

    sys.stdout.write(str(numTrees) + '\n')

if __name__ == '__main__':
    main()