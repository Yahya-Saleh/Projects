from Learning_OOP import Employee


# Instances of the Employee class
emp_1 = Employee("Yahya", "Saleh", 99999)
emp_2 = Employee("Test", "bot", 50000)

# Manually intializing instance attributes 
# emp_1.first = "Yahya"

print(emp_1.email)

# This shows why the instance is always passed automatically
# This
emp_1.fullname()
# Gets transformmed into this
Employee.fullname(emp_1)