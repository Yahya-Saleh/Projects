import copy

fi = ['12','t5','4']
spam = [fi,'24']
print(spam)

cheese = copy.deepcopy(spam)
print(cheese)
hi = copy.copy(spam)

print(hi)
