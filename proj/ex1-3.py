string1 = input('Enter a string: ')
string2 = input('Enter a another string: ')

if len(string1) < 2 or len(string2) < 2:
    raise Exception('The length of string should be longer than 2.')

s1 = string1[2:]
s2 = string2[2:]

print(s1+s2)
