# Object-Oriented programming

class Employee:
    
    # Class variables
    raise_amount = 1.04
    emp_no = 0

    # Initialization method
    def __init__(self, first, last, pay):
        # Automatically intializing instance attributes 
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@company.com"

        # Since emp_no is constent regardless of the instances
        # Employee.emp_no is incremented instead of self.emp_no - instances and class variables
        Employee.emp_no += 1

    # regular method
    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_amount(self):
        # Since we used self.raise_amount instead of Employee.raise_amount
        # the instances will check if it has a raise_amount defined before accessing the class variable
        self.pay = int(self.pay * self.raise_amount)

    # Passes in the class instead of the instance
    @classmethod
    # Class method
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Alternate constructor
    # Usually starts with from
    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # Static method
    @staticmethod
    def is_workday(day):
        # Using the datetime module
        if day.weekday() == 5 or day.weekday() == 5:
            return False

        return True

    # Dunder methods
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname()}-{self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
# Sub-Class of Employee
class Developer(Employee):
    # Developers have their own raise_amount
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        # Runs __init__ of parent
        super().__init__(first, last, pay)

        # Does the same
        # Employee.__init__(self, first, last, pay)

        self.prog_lang = prog_lang

class Manager(Employee):
    # you never want to pass in mutable data types like lists or dicts as default data types
    # That's why employees is none
    def __init__(self, first, last, pay, employees=None):
        # Runs __init__ of parent
        super().__init__(first, last, pay)

        if employees:
            self.employees = employees
        else:
            employees = []

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(f"--->{emp.fullname()}")