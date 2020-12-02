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
            minNum, maxNum, targetChar, searchString = match.groups()
            # print(minNum, maxNum, targetChar, searchString)

            if int(minNum) <= searchString.count(targetChar) <= int(maxNum):
                count += 1

    sys.stdout.write(str(count) + '\n')

if __name__ == '__main__':
    main()