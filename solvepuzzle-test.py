# This is a simple test or sanity check for output file syntax/formatting (FIT3080, assignment #1)
# Call this program as follows: 
# python solvepuzzle-test.py outputfile-name

import sys, re

def IsDigit(s):
  return re.search("[^1-3]", s) is None

def countChar(strr, ch):
  count = 0
  for i in range(0,len(strr)):
    if strr[i]==ch:
      count = count + 1
  return count

def swapCost(t):
  if t==1 or t==2:
    return 1
  if t==3:
    return 2 

def locateChar(string, char):
  loc = -1  
  for i in range(0, len(string)):
    if (string[i]==char):
      loc = i      
  return loc

def swap(myString, l1, l2):
  temp = list(myString)
  t = temp[l1]
  temp[l1] = temp[l2]
  temp[l2] = t
  return ''.join(temp)

outputfilename = sys.argv[1]


try:
    f = open(outputfilename, 'r')
except IOError:
    print('Error: The file you specified does not exist!')
    quit()

numlines = 0
splitflag = True

for line in f:
  numlines = numlines + 1
  splitline = line.split("\t")
  if len(splitline)!=3:
    splitflag = False

if not splitflag:
  print('Error: bad input format!')
  quit()

ops = ["" for x in range(numlines)]
strs = ["" for x in range(numlines)]
costs = ["" for x in range(numlines)]
f = open(outputfilename, 'r')
indx = 0
for line in f:
  splitline = line.split("\t")
  ops[indx] = splitline[0].upper()
  strs[indx] = splitline[1].upper()
  costs[indx] = splitline[2]
  indx = indx + 1

#################################################
# Check ops
if ops[0] =="START":
  opsflag = True
else:
  opsflag = False

opsflagMessage = ''
for i in range(1,numlines):
  opsflag = opsflag and IsDigit(ops[i][0]) and (ops[i][1]=='R' or ops[i][1]=='L')
  if opsflag==False:
    opsflagMessage = str(i+1)
    break

if not opsflag:
  print('Error: invalid operation in line ' + opsflagMessage + '!')
  quit()

#################################################
# Check strs
strsflag = True # solution invalid if false
strswarning = True # solution partial if false

strsflagMessage = ''
for i in range(0,numlines):
  strsflag = strsflag and (countChar(strs[i], 'W')==3) and (countChar(strs[i], 'B')==3) and (countChar(strs[i], 'E')==1)  
  if strsflag==False:
    strsflagMessage = str(i+1)
    break

strswarning = False
numW = 0
loc = 0
numChars = len(strs[numlines-1])
while (loc<numChars) and not (strs[numlines-1][loc]=='B'):
  if strs[numlines-1][loc]=='W':
    numW = numW + 1
  loc = loc + 1

if numW==3:
  strswarning = True

if not strsflag:
  print("Error: invalid tile configuration detected!")

#################################################
# Check costs

iflag = True # true for increasing sequences
for i in range(0, len(costs)-1):
  if int(costs[i+1])<=int(costs[i]):
    iflag = False

cflag = True # true for correct cost update(s)
cflagMessage = ''
temp_cost =  [0] * len(costs)
for i in range(1,len(costs)):
  temp_cost[i] = temp_cost[i-1] + swapCost(int(ops[i][0]))
  if temp_cost[i]!=int(costs[i]):
    cflagMessage = str(i+1)
    cflag = False

costsflag = int(costs[0])==0 and iflag and cflag

if not costsflag:
  print('Error: bad cost in line ' + cflagMessage + '! \nPlease check your cost calculations.')
  quit()

#################################################
# Check updates

uflag = True # true for correct updates
tmp_u =  ["" for x in range(len(costs))]
tmp_u[0] = strs[0]

for i in range(1,len(costs)):
  # swap
  l1 = locateChar(tmp_u[i-1],'E')  
  sc = int(ops[i][0])
  if ops[i][1]=='L':    
    l2 = l1 - sc
  if ops[i][1]=='R':
    l2 = l1 + sc
  if l2<len(strs[0]) and l2>=0:
    tmp_u[i] = swap(tmp_u[i-1], l1, l2)
  else:
    uflag = False  

uflagMessage = ''
 
for i in range(1,len(strs)):
  if strs[i]!=tmp_u[i]:
    uflagMessage = str(i+1)
    uflag = False

if not uflag:
  print('Error: bad update in line ' + uflagMessage + '! \nPlease check your operators.')
  quit()

#final solution most be acceptable as goal i.e. all white tiles to the left of black tiles
if not strswarning:
  print("Warning: final solution does not meet the goal requirement!")

print('Good job! Your output file passed the basic sanity checks! \nNow, you need to check if your costs are indeed optimal..')
