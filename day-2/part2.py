def readAllLines(fileName):
    lines = []

    with open(fileName) as f:
        lines = [line.rstrip() for line in f.readlines()]

    return lines

def main():
    import re
    import sys

    lines = readAllLines('input')

    count = 0
    for l in lines:
        match = re.search('([0-9]+)-([0-9]+)\s([a-z])\:\s(\w+)', l)
        
        if match:
            pos1, pos2, targetChar, searchString = match.groups()
            # print(pos1, pos2, targetChar, searchString)

            if (searchString[int(pos1)-1] == targetChar) ^ (searchString[int(pos2)-1] == targetChar):
                count += 1

    sys.stdout.write(str(count) + '\n')

if __name__ == '__main__':
    main()