def readLines(fileName):

  with open(fileName) as f:
    return [line.rstrip() for line in f.readlines()]

def main():
  import sys

  totalCount = 0
  currentGroupCount = set()

  lines = readLines('input')
  for l in lines:
    
    if l == '':
      totalCount += len(currentGroupCount)
      currentGroupCount = set()
    else:
      for c in l:
        currentGroupCount.add(c)

  totalCount += len(currentGroupCount)

  sys.stdout.write(str(totalCount) + '\n')
  return totalCount

if __name__ == '__main__':
  main()