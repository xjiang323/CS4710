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

def get_fw_al(Matrix,dic1,dic2):
    M = np.full((len(dic1),len(dic1)), np.inf)
    idx = (Matrix == 1)
    M[idx] = 1
    for i in range(len(dic1)):
        M[i,i] = 0
    for k in range(len(dic1)):
        for i in range(len(dic1)):
            for j in range(len(dic1)):
                if M[i,j] > M[i,k] + M[k,j]:
                    M[i,j] = M[i,k] + M[k,j]
    print(M)

if __name__ == "__main__":
    dic1 = get_protein_to_index("kshv.sif")
    dic2 = get_new_dic("kshv.sif")
    Matrix = get_matrix("kshv.sif",dic1)
