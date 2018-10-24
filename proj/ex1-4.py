
row = input('Enter a string: ')
string = str(row)

dict = {}
for index,value in enumerate(string):
    dict[value]=index+1

items = dict.items()
items = sorted(items)
for key,value in items:
    print("pos(" + str(key) + ") =" + str(value))

