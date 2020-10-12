from Learning_OOP import Employee


emp_1 = Employee("Yahya", "Saleh", 99999)
emp_2 = Employee("Test", "bot", 50000)

# prints <Learning_OOP.Employee object at 0x000002A87A1F7970> which we want to fix using repr and str methods
# print(emp_1)

print(emp_1)
print()

# What those functions are doing is calling the respective method in the class
# same as emp_1.__repr__()
print(repr(emp_1))
# same as emp_1.__str__()
print(str(emp_1))
print()


print(1+2)
# This is just calling the dunder add method within an int
print(int.__add__(1, 2))

print()

# We can tell our program how to add 2 instances of our class
# This would never work if we didn't define out dunder add method
print(emp_1 + emp_2)

print()

print(len(emp_1))
