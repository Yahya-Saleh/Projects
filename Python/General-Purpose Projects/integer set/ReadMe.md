# Integer set

A class definition for an integer set which contains unique integers.

## Methods

### init

Declares an empty list, `vals`, that will hold the integers.

### insert

Take in an `int` and adds it to `vals` if it was not already stored.

### member

Returns true if a given `int` is in the `int_set`.

### remove

Attempts to remove a given `int` and raises a `valueError` if the int is not in the list.

### getVals

A getter method to return the integers of teh set as a list.

### intersect

takes in another `int_set` and returns an `int_set` of the `int`s they have in common.

### str

represents the `int` between {} split by ,.

```python
{1, 7, 6, 9}
```

### len

the length of the class is the number of elements it holds.

## Acknowledgements

Most of the methods were pre-implemented, with the exception of the `__len__` and `intersect` methods.
