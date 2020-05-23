# Object-Oriented programming

Simple projects as well as notes that I made while learning Object-Oriented programming for python!

## Classes

Classes allow use to logically group our data and functions in away that's reusable and easy to build on.

data --> attributes
functions --> methods

## Instances

Classes are a blueprint and each unique variable holding that class is called an instance of the class.

## Attributes

When we try to access an instances the program will check if that instances has that attribute and if it doesn't it will see if the class has it.

### Instance variables

Unique to each instance of a class.

### Class variables

common to each instances of a class.

## Methods

Functions specific to a class.

### Regular methods

All the methods that we used thus far are regular methods: they take in the instances as the first argument.

#### __int__

The method that gets called when initializing an instance.

#### Self

Any regular method automatically takes in the instances as the first argument automatically, and by convention the instances is refereed to as self.

### Class methods

Methods that take in the class as input instead of the instance. Notice that class methods are almost always called by the class and not the instance:

```python
# Creating an instance using the alternate constructor
emp_3 = Employee.from_str("mark-mic-15200")
```

#### @classmethod

A decorator when written before a method allows it to take a class as a first argument instead of an instance.

#### cls

The convention for naming the parameter of passed class.

### Static methods

They don't take any input automatically. They are included because they have a logical connection to our other methods.

#### @staticmethod

The decorator that makes our method static.

## Sub-Classes

Are classes that inherit from other classes. Sub-classes have access to all the attributes and methods of the parent class.

### super().__init__()

Runs the parent `__init__` function.

### isinstance and issubclass

Good functions to use when experimenting with classes.

## Special methods

### Dunder

Methods who's name is between __: like `__init__` for example is called dunder Init. Also called magic methods.

#### __repr__

An unambiguous representation of the object that's used for debugging, and is meant to be seen by other developers. is displayed by `repr(object)`. a good repr definition is usually something that you can copy back into your code.

#### __str__

Readable representation that's meant to be seen by the end user. If the `__str__` method is not defined then the `__repr__` will be displayed when str(object) or print(object) is called otherwise `__str__` is displayed.

## Property Decorator

### @property

Lets us call methods as if they were attributes

### @property_name.setter

Used with @property to create a way to set or alter the instance.

### @property_name.deleter

Used with @property to create a method that's executed when del `instance.property` is called.
