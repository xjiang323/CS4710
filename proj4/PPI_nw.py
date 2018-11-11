import numpy as np

def get_protein_to_index(fname):
    dic = {}
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
    return dic

def get_new_dic(fname):
    dic = {}
    fhand = open(fname,'r')
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
    return dic

def get_matrix(fname):
    dic = get_protein_to_index(fname)
    Matrix = np.zeros((len(dic),len(dic)), dtype=int)
    fhand = open(fname,'r')
    for line in fhand:
        edge = line.split()
        if edge[0] == edge[2]:
            continue
        else:
            Matrix[dic[edge[0]],dic[edge[2]]] += 1
            Matrix[dic[edge[2]],dic[edge[0]]] += 1
    return Matrix

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
    for i in range(len(u_M)):
        print("k=" + str(u_M[i]) + " p=" + str(degree_lst[i]))

def get_cliques(M):
    dic = get_new_dic("kshv.sif")
    n = len(M[:,1])
    for i in range(n):
        for j in range(i,n):
            for k in range(j,n):
                if M[i,j] == 1 and M[i,k] == 1 and M[j,k] == 1:
                    print(str(dic[i]) + "," + str(dic[j]) + "," +str(dic[k]))

def get_fw_al(fname):
    dic = get_protein_to_index(fname)
    M = np.full((len(dic),len(dic)), np.inf)
    fhand = open(fname,'r')
    for line in fhand:
        edge = line.split()
        if edge[0] == edge[2]:
            continue
        else:
            M[dic[edge[0]],dic[edge[2]]] = 1
            M[dic[edge[2]],dic[edge[0]]] = 1
    for i in range(len(dic)):
        M[i,i] = 0
    for k in range(len(dic)):
        for i in range(len(dic)):
            for j in range(len(dic)):
                if M[i,j] > M[i,k] + M[k,j]:
                    M[i,j] = M[i,k] + M[k,j]
    X = np.sum((M == 2).astype(np.int), axis = 1)
    amax = np.amax(X)
    pmax = np.argmax(X)
    dic = get_new_dic("kshv.sif")
    print("Node " + str(dic[pmax]) + " has the largest neighborhood T2 and the size of T2 is " + str(amax))

Matrix = get_matrix("kshv.sif")
get_degree_dist(Matrix)
get_cliques(Matrix)
get_fw_al("kshv.sif")
#M = get_random_gragh(59,0.5)
#get_degree_dist(M)
