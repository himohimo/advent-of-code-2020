import re

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

  def checkHeight():

    hgtMatch = re.match('^(\d+)(cm|in)$', inputDict['hgt'])

    if not hgtMatch: return False

    value, units = hgtMatch.groups()

    if units == 'cm':
      return 150 <= int(value) <= 193

    elif units == 'in':
      return 59 <= int(value) <= 76
    
    return False


  checks = [
    1920 <= int(inputDict['byr']) <= 2002,
    2010 <= int(inputDict['iyr']) <= 2020,
    2020 <= int(inputDict['eyr']) <= 2030,
    checkHeight(),
    inputDict['hcl'][0] == '#' and not re.match('([g-z])', inputDict['hcl']),
    re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', inputDict['ecl']),
    re.match('^([\d]{9})$', inputDict['pid'])
  ]

  return all(checks)

def main():
  import sys

  count = 0
  currentPassportAttributes = {}

  lines = readLines('input')
  for l in lines:

    if l == '':
      if isValidPassport(currentPassportAttributes):
        count += 1

      currentPassportAttributes = {}
    
    else:
      match = re.findall('([a-z]{3})\:([#\w]+)', l)

      for k,v in match:
        currentPassportAttributes[k] = v

  # For last object
  if isValidPassport(currentPassportAttributes):
    count += 1

  sys.stdout.write(str(count) + '\n')
  return count

if __name__ == '__main__':
  main()