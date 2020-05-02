import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
print(cheese)

cheese[1] = 42
print(cheese)

print(spam)
