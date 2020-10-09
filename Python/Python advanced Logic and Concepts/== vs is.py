# "==" Checks for Equality
# "is" Checks for identity

# Two lists of the same values,but different memory locations
l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(l1 == l2)
print(l1 is l2)

print(id(l1), id(l2))


# Same memory location
l1 = [1, 2, 3]
l2 = l1

print(l1 == l2)
print(l1 is l2)

print(id(l1), id(l2))
# What "is" does
print(id(l1) == id(l2))