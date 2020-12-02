import sys


def readAllLines():

    lines = []

    inputFile = open('input', 'r')
    line = inputFile.readline()

    while line:
        line = int(line)
        lines.append(line)
        line = inputFile.readline()       

    inputFile.close()

    return lines

def main():
    target = 2020
    result = 0

    lines = readAllLines()
    N = len(lines)
    
    partSum = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (lines[i] + lines[j] + lines[k] == target):
                    result = lines[i] * lines[j] * lines[k]
                    break

    sys.stdout.write(str(result) + '\n')
    return result

if __name__ == '__main__':
    main()