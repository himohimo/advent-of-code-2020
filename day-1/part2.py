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
    targetSum = 2020
    result = 0

    lines = readAllLines()
    lines = sorted(lines)
    N = len(lines)
    
    for i in range(N):

        l = i
        r = N - 1
        target = targetSum - lines[i]
        # print('target', target)

        while l <= r:

            # print(lines[mid])
            if lines[l] + lines[r] == target:
                result = lines[l] * lines[i] * lines[r]
                sys.stdout.write(str(result) + '\n')
                return result
            elif lines[l] + lines[r] > target:
                r -= 1
            else:
                l += 1

    return 0

if __name__ == '__main__':
    main()