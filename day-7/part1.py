def readLines(fileName):

  with open(fileName) as f:
    return [line.rstrip() for line in f.readlines()]

def parseBagColors(lines):
  import re

  myDict = {}

  for l in lines:
    match1 = re.search('(\w+\s\w+) bags contain (.*).', l)
    
    if match1:
      mainColor, strToParse = match1.groups()

      if strToParse == 'no other bags':
        myDict[mainColor] = []
      else:
        match2 = re.findall('[\d]*\s(\w+\s\w+) bag[s]?', strToParse)

        if match2:
          myDict[mainColor] = match2

  return myDict

def findGold(targetColor, colorDict, seen, lvl):

  if targetColor == 'shiny gold' and lvl > 0: return True
  if targetColor not in colorDict: return False
  if len(colorDict[targetColor]) == 0: return False
  if targetColor in seen: return False

  result = False

  for bag in colorDict[targetColor]:
    foundGold = findGold(bag, colorDict, seen, lvl + 1)

    if foundGold:
      result = True
    else:
      seen.add(targetColor)

  return result

def main():
  import sys

  lines = readLines('input')
  bagRules = parseBagColors(lines)

  numFound = 0

  for bag in bagRules:
    seen = set()
    foundGold = findGold(bag, bagRules, seen, 0)

    if foundGold: 
      numFound += 1

  # print(len(validColors))
  # print(numFound)
  
  sys.stdout.write(str(numFound) + '\n')

if __name__ == '__main__':
  main()