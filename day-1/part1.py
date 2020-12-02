import sys

def main():
    target = 2020

    inputFile = open('input', 'r')
    line = inputFile.readline()

    neededNumber = {}
    result = 0

    while line:

        line = int(line)
        if line in neededNumber:
            result = line * neededNumber[line]
            break
        else:
            neededNumber[target - line] = line

        line = inputFile.readline()       

    inputFile.close()

    sys.stdout.write(str(result) + '\n')
    return result

if __name__ == '__main__':
    main()