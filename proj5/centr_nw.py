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
    C = np.reciprocal(np.sum(M, axis = 1))
    O1 = np.argsort(C)
    print("The top three nodes with highest closeness centrality value are:")
    for i in [-1, -2, -3]:
        print(str(dic2[O1[i]]) + "'s closeness centrality value is " + str(C[O1[i]]))
    print("\n")

    E = np.amax(M, axis = 1).astype(np.int)
    E_min = np.amin(E)
    O2 = np.where(E == E_min)[0]
    for item in O2:
        print("The center of the gragh is " + str(dic2[item]))
    print("\n")
    high = O1[-1]
    low = O1[0]
    return high, low

def bfs_paths(Matrix, start, goal):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        lst = Matrix[node,]
        node_lst = np.where(lst == 1)[0]
        for next_node in node_lst:
            if next_node in path:
                continue
            elif next_node == goal:
                return path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

if __name__ == "__main__":
    f = "kshv.sif"
    high, low = get_fw_al(get_matrix(f, get_protein_to_index(f)), get_protein_to_index(f), get_new_dic(f))
    lt = bfs_paths(get_matrix(f, get_protein_to_index(f)), low, high)
    path = ""
    for i in lt:
        path += get_new_dic(f)[i] + ", "
    print("The shortest path between the node with lowest closeness centrality and the node with highest is: ")
    print(path[:-2])
