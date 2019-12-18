f= open("/Users/vikamkrtchyan/Desktop/python/homework 3/homework 3.txt","r")

# Opening the file in Read mode
if f.mode == 'r':
    contents = f.read()
    print(contents)

# splitting words from file to list
words = contents.split()
print(words)

# iterating over words in the list ans printing words and its length
for word in words:
    print(word, len(word))

# defining maximum length and finding it in the list
def longest_words(words):
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]
print(longest_words(words))
