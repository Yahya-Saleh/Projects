from Learning_OOP import Employee


# Instances of the Employee class
emp_1 = Employee("Yahya", "Saleh", 99999)
emp_2 = Employee("Test", "bot", 50000)

# Class method
# Takes in class as first argument
Employee.set_raise_amount(1.16)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
print()

# Alternate constructor
# Creating an instance using the alternate constructor
emp_3 = Employee.from_str("mark-mic-15200")
print(emp_3.email)
# static methods
# Is it a work day?
import datetime
my_date = datetime.date(2016, 7, 11)
print()
print(Employee.is_workday(my_date))