import numpy as np

dic = {}
fname = "kshv.sif"
fhand = open(fname,'r')
count = 0
for line in fhand:
    edge = line.split()
    if edge[0] in dic.keys():pass
    else:
        count += 1
        dic[edge[0]] = count-1
    if edge[2] in dic.keys():pass
    else:
        count += 1
        dic[edge[2]] = count-1
print(dic)

def get_random_gragh(n,p):
    M = np.random.rand(n,n)
    M[M >= p] = 1
    M[M < p] = 0
    M = M.astype(np.int)
    return M

def get_degree_dist(M):
    col_sum = np.sum(M, axis = 0)
    u_M = np.unique(col_sum)
    degree_lst = []
    for item in u_M:
        count = 0
        for element in col_sum:
            if element == item:
                count += 1
        degree_lst.append(count)
    print(degree_lst)

M = get_random_gragh(10,0.5)
get_degree_dist(M)
