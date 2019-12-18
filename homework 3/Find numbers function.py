
f= open("homework 3.txt","r")
if f.mode == 'r':
    contents = f.read()
    print(contents)


def findNumbers(contents):
    return [char for char in contents if (char.isdigit()) == True]
print(findNumbers(contents))



