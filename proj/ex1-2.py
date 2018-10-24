
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0

vowels = set('aeiou')
for line in fhand:
    line = line.rstrip()
    for i in line:
        if i in vowels:
            count = count + 1
            print(i)
        else:
            pass
print(count)

