def main():

    """Reading file steps.

    Step 1) Open the file in Read mode
    Step 2) Use the mode function in the code to check that the file is in open mode.
    If yes, we proceed ahead.
    Step 3) Use f.read to read file data and store it in variable content.
    Step 4) print contents.
    """

f= open("homework 3.txt","r")
if f.mode == 'r':
    contents = f.read()
    print(contents)

# Count numeric characters in a string

newstring1 = ""

# Iterating the string and checking for numeric characters
# Printing the character if a numeric
# And adding character to new string if not numeric and printing

for a in contents:
    if (a.isdigit()) == True:
        print(a)
    else:
        newstring1 += a

print(newstring1)

