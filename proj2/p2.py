
fname = input("Please enter file name: ")
fhand = open(fname)

arr = []
for line in fhand:
    line = line.rstrip()
    tmp = list(line)
    col = len(tmp)
    arr.append(tmp)
row = len(arr)

ref = ['A','T','G','C']
final_arr = []
for n in range(4): # Loop through ATGC
    freq_lst = []
    for i in range(col):
        count = 0
        for j in range(row):
            if arr[j][i] == ref[n]:
                count = count + 1
        if count == 0:
            string = '0'
        else:
            string = str(count) + '/' + str(row)
        freq_lst.append(string)
    print(ref[n], " : ", freq_lst)
