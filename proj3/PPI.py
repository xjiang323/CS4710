from fractions import Fraction
import sys
import math

fname = sys.argv[1]
chain1 = input("Please enter the first chain: ")
chain2 = input("Please enter the second chain: ")
threshold = input("Please enter the threshold: ")
th = int(threshold)

dic1,dic2 = {},{}
helix1,helix2 = [],[]
sheet1,sheet2 = [],[]
fhand = open(fname,'r')
for line in fhand:
    if line[:4] == 'ATOM':
        if line[21:22] == chain1:
            if 'CA' in line:
                tmp = []
                tmp.append(line[17:20])
                tmp.append(line[30:38].strip())
                tmp.append(line[38:46].strip())
                tmp.append(line[46:54].strip())
                dic1[line[22:26].strip()] = tmp
        elif line[21:22] == chain2:
            if 'CA' in line:
                tmp = []
                tmp.append(line[17:20])
                tmp.append(line[30:38].strip())
                tmp.append(line[38:46].strip())
                tmp.append(line[46:54].strip())
                dic2[line[22:26].strip()] = tmp
    elif line[:5] == 'HELIX':
        if line[19:20] == chain1:
            start = line[21:25].strip()
            step = line[71:76].strip()
            for i in range(int(start),int(start)+int(step)):
                helix1.append(i)
        elif line[19:20] == chain2:
            start = line[21:25].strip()
            step = line[71:76].strip()
            for i in range(int(start),int(start)+int(step)):
                helix2.append(i)
    elif line[:5] == 'SHEET':
        if line[21:22] == chain1:
            start = line[22:26].strip()
            end = line[33:37].strip()
            for i in range(int(start),int(end)+1):
                sheet1.append(i)
        elif line[21:22] == chain2:
            start = line[22:26].strip()
            end = line[33:37].strip()
            for i in range(int(start),int(end)+1):
                sheet2.append(i)

intact1, intact2 = {},{}
intact1_keys,intact2_keys = [],[]
for key1 in dic1:
    for key2 in dic2:
        d = math.sqrt(math.pow(float(dic1[key1][1]) - float(dic2[key2][1]),2) + math.pow(float(dic1[key1][2]) - float(dic2[key2][2]),2) + math.pow(float(dic1[key1][3]) - float(dic2[key2][3]),2))
        if d < th:
            print(chain1 + ": " + dic1[key1][0] + "(" + str(key1) + ") interacts with " + chain2 + ": " + dic2[key2][0] + "(" + str(key2) + ")")
            intact1[key1] = dic1[key1][0]
            intact2[key2] = dic2[key2][0]

count1 = 0
count2 = 0
for key1 in intact1:
    k = int(key1)
    intact1_keys.append(k)
    if k in helix1:
        count1 += 1
    if k in sheet1:
        count2 += 1
print(chain1)
percent1 = Fraction(count1,len(intact1))
percent2 = Fraction(count2,len(intact1))
print(str(percent1) + " of the interface amino acids lying on alpha helices")
print(str(percent2) + " of the interface amino acids lying on belta sheets")
count1 = 0
count2 = 0
for key2 in intact2:
    k = int(key2)
    intact2_keys.append(k)
    if k in helix2:
        count1 += 1
    if k in sheet2:
        count2 += 1
print(chain2)
percent1 = Fraction(count1,len(intact2))
percent2 = Fraction(count2,len(intact2))
print(str(percent1) + " of the interface amino acids lying on alpha helices")
print(str(percent2) + " of the interface amino acids lying on belta sheets")

print(chain1)
n = len(intact1_keys)
for i in range(n):
    thisKey = intact1_keys[i]
    if i == 0:
        nextKey = intact1_keys[i+1]
        distance = abs(thisKey - nextKey)
        print(intact1[str(thisKey)] + ": closest " + intact1[str(nextKey)] + " at distance " + str(distance))
    elif i == n-1:
        previousKey = intact1_keys[i-1]
        distance = abs(thisKey - previousKey)
        print(intact1[str(thisKey)] + ": closest " + intact1[str(previousKey)] + " at distance " + str(distance))
    else:
        nextKey = intact1_keys[i+1]
        previousKey = intact1_keys[i-1]
        predistance = abs(thisKey - previousKey)
        suffdistance = abs(thisKey - nextKey)
        if predistance >= suffdistance:
            print(intact1[str(thisKey)] + ": closest " + intact1[str(nextKey)] + " at distance " + str(suffdistance))
        else:
            print(intact1[str(thisKey)] + ": closest " + intact1[str(previousKey)] + " at distance " + str(predistance))
print(chain2)
intact2_keys.sort()
n = len(intact2_keys)
for i in range(n):
    thisKey = intact2_keys[i]
    if i == 0:
        nextKey = intact2_keys[i+1]
        distance = abs(thisKey - nextKey)
        print(intact2[str(thisKey)] + ": closest " + intact2[str(nextKey)] + " at distance " + str(distance))
    elif i == n-1:
        previousKey = intact2_keys[i-1]
        distance = abs(thisKey - previousKey)
        print(intact2[str(thisKey)] + ": closest " + intact2[str(previousKey)] + " at distance " + str(distance))
    else:
        nextKey = intact2_keys[i+1]
        previousKey = intact2_keys[i-1]
        predistance = abs(thisKey - previousKey)
        suffdistance = abs(thisKey - nextKey)
        if predistance >= suffdistance:
            print(intact2[str(thisKey)] + ": closest " + intact2[str(nextKey)] + " at distance " + str(suffdistance))
        else:
            print(intact2[str(thisKey)] + ": closest " + intact2[str(previousKey)] + " at distance " + str(predistance))
    

