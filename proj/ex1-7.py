lst = []
while True:
    string = input('Enter a number.Input empty to quit.')
    if len(string) != 0:
        lst.append(string)
    else:
        break

if len(lst) % 2 == 1:
    tmp = lst[:-1:2]
    lst[:-1:2] = lst[1::2]
    lst[1::2] = tmp
else:
    tmp = lst[::2]
    lst[::2] = lst[1::2]
    lst[1::2] = tmp
print(lst)
