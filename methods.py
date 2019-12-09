# Capitalize first letter of the string

text = "hello, this is my homework"

print(text.capitalize())

# Print name string taking space of 20 characters, with name string in the center

name = "Victoria"

print(name.center(20))

# Return the number of letter "i" in the name string

name = "Victoria"

print(name.count('i'))


# Check if the position 3 to 6 ends with letter 'i'

name = "Victoria"

print(name.endswith('i', 3, 6))

# Expand tabs size to be replaced with the “\t” symbol

text = 'I\tam\tno\tordinary\tsoftware\ttester'

print(text.expandtabs(12))

# Find the first occurance of letter 'o' in the string

text = 'I am no ordinary software tester'

print(text.find('o'))

# Find the first occurance of letter 'o' in the string with index method.
# Difference should be the return value Velue Eror if not found

text = 'I am no ordinary software tester'

print(text.index('a', 3, 7))

# Find the last occurance of letter 'a' between position 3 and 7. Returns -1 if not found

text = 'I am no ordinary software tester'

print(text.rfind('a', 3, 7))

# Find last occurance of letter 'v' with rindex. Difference should be Value Error instead of -1 when not found

text = 'I am no ordinary software tester'

print(text.rindex('v'))

# Check if all the characters in the text are letters.

text = "this is text with one number 8"

x = text.isalpha()

print(x)

# Join all the characters in the list with empty separator

list = ['V','I', 'C', 'T', 'O', 'R', 'I', 'A']

print(''.join(list))

# Check if all characters are uppercase

text = "This is text with one upper case"

print(text.isupper())

