class Employee:
    # Initialization method
    def __init__(self, first, last):
        # Automatically intializing instance attributes 
        # Instance variables
        self.first = first
        self.last = last
        self.email = f"{self.first}.{self.last}@company.com"

    # regular method
    def fullname(self):
        return f"{self.first} {self.last}"


# emp_1 = Employee("Yahya", "Saleh")
# emp_2 = Employee("Test", "bot")

# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())

# print()
# emp_1.first = "Ahmed"

# # Notice how the email didn't get updated
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())
# print()


class Employee:
    # Initialization method
    def __init__(self, first, last):
        # Automatically intializing instance attributes 
        # Instance variables
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    # regular method
    def fullname(self):
        return f"{self.first} {self.last}"


# With the property decorator we can treat email as an attribute even though it's a method
# emp_2 = Employee("Test", "bot")

# print(emp_2.email)
# print(emp_2.first)
# print(emp_2.fullname())

# print()
# emp_2.first = "Ahmed"

# # Notice how the email didn't get updated
# print(emp_2.first)
# print(emp_2.email)
# print(emp_2.fullname())
# print()

class Employee:
    # Initialization method
    def __init__(self, first, last):
        # Automatically intializing instance attributes 
        # Instance variables
        self.first = first
        self.last = last

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleted name")
        self.first = None
        self.last = None


emp_2 = Employee("Test", "bot")

print(emp_2.email)
print(emp_2.first)
print(emp_2.fullname)

print()
# Using the setter decorator we can set our first and last name
emp_2.fullname = "yahya saleh"

print(emp_2.email)
print(emp_2.first)
print(emp_2.fullname)

# Delter is what gets run when del is called on fullname
del emp_2.fullname