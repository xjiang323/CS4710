from fractions import Fraction
import math

fname = "3hmg.pdb"
chain1 = input("Please enter the first chain: ")
chain2 = input("Please enter the second chain: ")
threshold = input("Please enter the threshold: ")
th = int(threshold)

def get_int(chain1,chain2):
    int1, int2 = get_interacting(chain1, chain2)
    key1 = get_fraction(chain1,int1)
    key2 = get_fraction(chain2,int2)
    get_closest_AA(chain1,key1,int1)
    get_closest_AA(chain2,key2,int2)
    
def get_fraction(chain, intact):
    helix, sheet = get_helix_and_sheet(chain)    
    intact_keys= []
    count1 = 0
    count2 = 0
    for key in intact:
        k = int(key)
        intact_keys.append(k)
        if k in helix:
            count1 += 1
        if k in sheet:
            count2 += 1
    percent1 = Fraction(count1,len(intact))
    percent2 = Fraction(count2,len(intact))
    print(chain)
    print(str(percent1) + " of the interface amino acids lying on alpha helices")
    print(str(percent2) + " of the interface amino acids lying on belta sheets")
    return intact_keys
    
def get_interacting(chain1, chain2):
    dic1 = get_dic(chain1)
    dic2 = get_dic(chain2)
    intact1, intact2 = {},{}
    for key1 in dic1:
        for key2 in dic2:
            d = math.sqrt(math.pow(float(dic1[key1][1]) - float(dic2[key2][1]),2) + math.pow(float(dic1[key1][2]) - float(dic2[key2][2]),2) + math.pow(float(dic1[key1][3]) - float(dic2[key2][3]),2))
            if d < th:
                print(chain1 + ": " + dic1[key1][0] + "(" + str(key1) + ") interacts with " + chain2 + ": " + dic2[key2][0] + "(" + str(key2) + ")")
                intact1[key1] = dic1[key1][0]
                intact2[key2] = dic2[key2][0]
    return (intact1, intact2)

def get_dic(chain):
    dic = {}
    fhand = open(fname,'r')
    for line in fhand:
        if line[:4] == 'ATOM':
            if line[21:22] == chain:
                if 'CA' in line:
                    tmp = []
                    tmp.append(line[17:20])
                    tmp.append(line[30:38].strip())
                    tmp.append(line[38:46].strip())
                    tmp.append(line[46:54].strip())
                    dic[line[22:26].strip()] = tmp
    return dic
def get_helix_and_sheet(chain):
    helix, sheet = [],[]
    fhand = open(fname,'r')
    for line in fhand:
        if line[:5] == 'HELIX':
            if line[19:20] == chain:
                start = line[21:25].strip()
                step = line[71:76].strip()
                for i in range(int(start),int(start)+int(step)):
                    helix.append(i)
        elif line[:5] == 'SHEET':
            if line[21:22] == chain:
                start = line[22:26].strip()
                end = line[33:37].strip()
                for i in range(int(start),int(end)+1):
                    sheet.append(i)
    return (helix, sheet)

def get_closest_AA(chain,intact_keys,intact):
    print(chain)
    intact_keys.sort()
    n = len(intact_keys)
    for i in range(n):
        thisKey = intact_keys[i]
        if i == 0:
            nextKey = intact_keys[i+1]
            distance = abs(thisKey - nextKey)
            print(intact[str(thisKey)] + ": closest " + intact[str(nextKey)] + " at distance " + str(distance))
        elif i == n-1:
            previousKey = intact_keys[i-1]
            distance = abs(thisKey - previousKey)
            print(intact[str(thisKey)] + ": closest " + intact[str(previousKey)] + " at distance " + str(distance))
        else:
            nextKey = intact_keys[i+1]
            previousKey = intact_keys[i-1]
            predistance = abs(thisKey - previousKey)
            suffdistance = abs(thisKey - nextKey)
            if predistance >= suffdistance:
                print(intact[str(thisKey)] + ": closest " + intact[str(nextKey)] + " at distance " + str(suffdistance))
            else:
                print(intact[str(thisKey)] + ": closest " + intact[str(previousKey)] + " at distance " + str(predistance))

get_int(chain1,chain2)
