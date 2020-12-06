def readLines(fileName):

  with open(fileName) as f:
    return [line.rstrip() for line in f.readlines()]

def main():
  import sys

  totalCount = 0
  currentGroupCount = 0
  currentGroupHist = {}

  lines = readLines('input')
  for l in lines:
    
    if l == '':
      for k in currentGroupHist:
        if currentGroupHist[k] == currentGroupCount:
          totalCount += 1
      currentGroupCount = 0
      currentGroupHist = {}
    else:
      currentGroupCount += 1
      for c in l:
        currentGroupHist[c] = currentGroupHist.get(c, 0) + 1

  for k in currentGroupHist:
    if currentGroupHist[k] == currentGroupCount:
      totalCount += 1

  sys.stdout.write(str(totalCount) + '\n')
  return totalCount

if __name__ == '__main__':
  main()