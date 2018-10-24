string = ''
for i in range(10):
    string = ''
    for j in range(10):
        value = i * j
        string = string + str(value) + ' '
    print(string)
