# Dunder __builtins__, __init__
message = "PYTHON: Everything is an object!"
print(message)

result = type(message)
print("result:", result)

''' In Python, there are builtin tools:
(1) TYPES > int float str list dict
(2) FUNCTIONS > print() len() input() type() str() int()
(3) CONSTANTS > True False None
'''

print(dir(__builtins__))

a = 100
print("a",   a)

message = "Hello World!" 
print(message)
