def readLines(fileName):

  with open(fileName) as f:
    return [line.rstrip() for line in f.readlines()]

def isValidPassport(inputDict):
  requiredAttributes = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
  ]

  for attr in requiredAttributes:
    if attr not in inputDict:
      return False

  return True

def main():
  import re
  import sys

  count = 0
  currentPassportAttributes = set()

  lines = readLines('input')
  for l in lines:

    if l == '':
      if isValidPassport(currentPassportAttributes):
        count += 1

      currentPassportAttributes = set()
    
    else:
      match = re.findall('([a-z]{3})\:', l)

      for m in match:
        currentPassportAttributes.add(m)

  # For last object
  if isValidPassport(currentPassportAttributes):
    count += 1

  sys.stdout.write(str(count) + '\n')
  return count

if __name__ == '__main__':
  main()