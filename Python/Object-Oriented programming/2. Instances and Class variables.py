from Learning_OOP import Employee


# Instances of the Employee class
emp_1 = Employee("Yahya", "Saleh", 99999)
emp_2 = Employee("Test", "bot", 50000)

# Emp_1 doesn't have a raise amount attribute so it looks for it in the Employee class
print(Employee.__dict__)
print()
print(emp_1.__dict__)
print()

# Changes the raise_amount for every instance
Employee.raise_amount = 1.05

# Changes the raise_amount for specific instance
# Specifically it creates a raise_amount key for that specific instance that can be accessed through self
emp_1.raise_amount = 1.07
print(emp_1.__dict__)
print()

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)