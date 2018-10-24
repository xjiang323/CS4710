input_string = input('Enter a string: ')

hhh=[]
for i in input_string:
    if i in hhh:
        print(i)
        exit(0)
    else:
        hhh.append(i)
