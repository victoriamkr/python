name = 'Victoria'
surname = 'Mkrtchyan'
print(name +  surname)

name = 'Victoria'
surname = 'Mkrtchyan'
print(name + surname)

# Split string 'name' into list of characters
def split(name):
    return list(name)

print(split(name))

# or just
list_name = name.split()

print(list_name)

# Iterating using for loop
for x in split(name):
    print(x)

# Split string 'surname' into list of characters
def split(surname):
    return list(surname)
print(split(surname))

# Getting length of list
length = len(split(surname))
i = 0

# Iterating using while loop
while i < length:
    print(list(surname)[i])
    i += 1

# or second usage of while loop

a = list(surname)
while a:
    print(a.pop(0))

