def main():

    """Reading file steps.

    Step 1) Opening the file in Read mode
    Step 2) Using the mode function in the code to check that the file is in open mode.
    If yes, proceed ahead.
    Step 3) Using f.read to read file data and store it in variable content.
    Step 4) Print contents.
    """

f= open("homework 3.txt","r")
if f.mode == 'r':
    contents = f.read()
    print(contents)

# Print numeric characters from string

newstring1 = ""

# Iterating the string and checking for numeric characters
# Printing the character if a numeric
# And adding character to new string if not numeric and printing

for char in contents:
    if (char.isdigit()) == True:
        print(char)
    else:
        newstring1 += char

print(newstring1)

