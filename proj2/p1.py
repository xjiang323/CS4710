p1 = input("Please enter the first permutation: ")
if len(p1) > 26 :
    exit(0)
if p1.isalpha() != True:
    exit(0)
hhh = []
for i in p1:
    if i in hhh:
        exit(0)
    else:
        hhh.append(i)

p2 = input("Please enter the second permutation: ")
if len(p2) > 26 :
    exit(0)
if p1.isalpha() != True:
     exit(0)
fff = []
for i in p2:
    if i in fff:
        exit(0)
    else:
        fff.append(i)

hhh.sort()
fff.sort()
if hhh != fff:
    exit(0)
else:
    pass

count = 0
for i in range(len(p1)):
    if p1[i] == p2[i]:
        pass
    else:
        count = count + 1
print("Hamming distance is " + str(count))

pl1 = list(p1)
pl2 = list(p2)

arr = []
for i in range(len(pl1)):
    for j in range(i,len(pl1)):
        if pl2.index(pl1[i]) > pl2.index(pl1[j]):
            tmp = []
            tmp.append(pl1[i])
            tmp.append(pl1[j])
            arr.append(tmp)
print("Kendall's diatance is " + str(len(arr)))

sum_num = 0
for item in pl1:
    dis = abs(pl1.index(item)-pl2.index(item))
    sum_num += dis
print("Spearman distance is " + str(sum_num))
