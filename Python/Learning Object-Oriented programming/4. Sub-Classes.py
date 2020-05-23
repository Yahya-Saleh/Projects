from Learning_OOP import Employee, Developer, Manager

# This works because just like with classes and instances python looks in developer for an __init__ and if it doesn't find it it will look in Employee
# emp_1 = Developer("Yahya", "Saleh", 99999)

# Shows, among other things, the method resolution order
#print(help(Developer))

# Applying super().__int__()
dev_1 = Developer("Yahya", "Saleh", 99999, "python")
dev_2 = Developer("Test", "bot", 50000, "Java")

print(dev_1.prog_lang)
print()

mng_1 = Manager("sue", "smith", 90000, [dev_1])

mng_1.print_emp()
print()
mng_1.add_emp(dev_2)
mng_1.remove_emp(dev_1)

mng_1.print_emp()
print()

print(isinstance(mng_1, Manager))
print(isinstance(mng_1, Employee))
print(isinstance(mng_1, Developer))
print()
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))