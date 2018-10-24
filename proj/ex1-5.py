

string = input('Enter a list: ')
lst = list(string)

dict = {}
for index,value in enumerate(lst):
    dict[value]=index+1

items = dict.items()
items = sorted(items)
for key,value in items:
    print("pos(" + str(key) + ") =" + str(value))

