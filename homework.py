name = 'Victoria'
surname = 'Mkrtchyan'
print(name +  surname)

# Split string 'name' into list of characters
def split(name):
    return list(name)

print(list(name))

# Iterating using for loop
for letter in list(name):
    print(letter)

# Split string 'surname' into list of characters
def split(surname):
    return list(surname)

print(list(surname))

# Getting length of list
length = len(list(surname))
i = 0

# Iterating using while loop
while i < length:
    print(list(surname)[i])
    i += 1

# or second usage of while loop

a = list(surname)
while a:
    print(a.pop())

