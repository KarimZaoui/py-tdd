# py-tdd

## TDD Cycle


The TDD cycle is made by 5 steps:

1. Write a failing test
2. Run and fail the test
3. Write code to pass
4. Run and pass test
5. Refactor
Using baby steps you can go through this cycle every time you add or modify a new feature in your code.


## unittest

### Main methods

The **main methods** that we make use of in unit testing for Python are:

1. assert: base assert allowing you to write your own assertions
2. assertEqual(a, b): check a and b are equal
3. assertNotEqual(a, b): check a and b are not equal
4. assertIn(a, b): check that a is in the item b
5. assertNotIn(a, b): check that a is not in the item b
6. assertFalse(a): check that the value of a is False
7. assertTrue(a): check the value of a is True
8. assertIsInstance(a, TYPE): check that a is of type "TYPE"
9. assertRaises(ERROR, a, args): check that when a is called with args that it raises ERROR

### Mock