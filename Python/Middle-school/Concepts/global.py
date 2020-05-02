def spam():
    global eggs
    eggs = 'spam'

eggs  = 'global'
spam()
print(eggs)

def name():
    global hisname
    print('please input your name')
    hisname = input()

name()
print(hisname)

print('Note')
print()
print('If you ever want to modify the value stored in a global variable from in a function, you must use a global statement on that variable')
