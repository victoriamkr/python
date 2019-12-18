import os
path = "/Users/vikamkrtchyan/Desktop/python/homework 3"
start = "python/homework 3"
relative_path = os.path.relpath(path, start)

print(relative_path)