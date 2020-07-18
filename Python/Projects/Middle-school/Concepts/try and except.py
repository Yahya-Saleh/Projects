def spam(no):
    try:
        return 42 / no
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam(no):
        return 42 / no

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
