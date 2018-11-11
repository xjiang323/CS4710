import numpy as np

def get_protein_to_index(fname):
    dic1 = {}
    fhand = open(fname,'r')
    count = 0
    for line in fhand:
        edge = line.split()
        if edge[0] in dic1.keys():pass
        else:
            count += 1
            dic1[edge[0]] = count-1
        if edge[2] in dic1.keys():pass
        else:
            count += 1
            dic1[edge[2]] = count-1
    return dic1

def get_new_dic(fname):
    dic2 = {}
    fhand = open(fname,'r')
    count = 0
    for line in fhand:
        edge = line.split()
        if edge[0] in dic2.values():pass
        else:
            count += 1
            dic2[count-1] = edge[0]
        if edge[2] in dic2.values():pass
        else:
            count += 1
            dic2[count-1] = edge[2]
    return dic2

def get_matrix(fname,dic):
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

def get_cliques(M,dic):
    for i in range(len(dic)):
        for j in range(i,len(dic)):
            for k in range(j,len(dic)):
                if M[i,j] == 1 and M[i,k] == 1 and M[j,k] == 1:
                    print(str(dic[i]) + "," + str(dic[j]) + "," +str(dic[k]))

def get_fw_al(Matrix,dic1,dic2):
    M = np.full((len(dic1),len(dic1)), np.inf)
    idx = (Matrix == 1)
    M[idx] = 1
    for k in range(len(dic1)):
        for i in range(len(dic1)):
            for j in range(len(dic1)):
                if M[i,j] > M[i,k] + M[k,j]:
                    M[i,j] = M[i,k] + M[k,j]
    X = np.sum((M == 2).astype(np.int), axis = 1)
    amax = np.amax(X)
    pmax = np.argmax(X)
    print("Node " + str(dic2[pmax]) + " has the largest neighborhood T2 and the size of T2 is " + str(amax))

def get_all(M,dic1,dic2):
    get_degree_dist(M)
    get_cliques(M,dic2)
    get_fw_al(M,dic1,dic2)

dic1 = get_protein_to_index("kshv.sif")
dic2 = get_new_dic("kshv.sif")
Matrix1 = get_matrix("kshv.sif",dic1)
get_all(Matrix1,dic1,dic2)

M = get_random_gragh(len(dic1),0.5)
get_all(M,dic1,dic2)

N = get_random_gragh(len(dic1),0.1)
get_all(N,dic1,dic2)

L = get_random_gragh(len(dic1),0.8)
get_all(L,dic1,dic2)
