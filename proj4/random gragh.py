import numpy as np

p = 0.8

dic = {}
fhand = open("kshv.sif",'r')
count = 0
for line in fhand:
    edge = line.split()
    if edge[0] in dic.values():pass
    else:
        count += 1
        dic[count-1] = edge[0]
    if edge[2] in dic.values():pass
    else:
        count += 1
        dic[count-1] = edge[2]

n = len(dic)
M = np.random.rand(n,n)
M[M >= p] = 1
M[M < p] = 0
for i in range(n):
    if M[i,i] == 1:
        M[i,i] = 0
M = M.astype(np.int)

out = "random gragh 0.8.sif"
fout = open(out,'w')
for i in range(n):
    for j in range(i,n):
        if M[i,j] == 1:
            fout.write(str(dic[i]) + " 1.0 " + str(dic[j]) + "\n")
fout.close()
