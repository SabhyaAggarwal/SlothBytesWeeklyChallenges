# September 9 2025 - Algebra Evaluator

## Challenge: evalAlgebra

Create a function that solves simple linear equations with one variable (x).

### Function Signature
```python
def evalAlgebra(expr):
```

### Description
The `evalAlgebra` function takes a string representing a simple linear equation and solves for the variable `x`. The function handles various formats of linear equations including addition, subtraction, and cases where `x` can be positive or negative.

### Supported Equation Formats
- `"number + x = result"` (e.g., "2 + x = 19")
- `"number - x = result"` (e.g., "4 - x = 1") 
- `"x + number = result"` (e.g., "x + 10 = 53")
- `"x - number = result"` (e.g., "x - 22 = -56")
- `"x = result"` (e.g., "x = 19")
- `"-x = result"` (e.g., "-x = 7")

### Examples
```python
evalAlgebra("2 + x = 19")      # x = 17
evalAlgebra("4 - x = 1")       # x = 3
evalAlgebra("x + 10 = 53")     # x = 43
evalAlgebra("-23 + x = -20")   # x = 3
evalAlgebra("10 + x = 5")      # x = -5
evalAlgebra("-49 - x = -180")  # x = 131
evalAlgebra("x - 22 = -56")    # x = -34
```

### Features
- ✅ Handles equations with spaces (automatically removes them)
- ✅ Supports positive and negative numbers
- ✅ Works when x appears on either side of the operator
- ✅ Returns correct results including negative values for x
- ✅ Prints both the cleaned expression and the solution

### Algorithm
1. Remove all spaces from the input equation
2. Split the equation by the equals sign to get left and right sides
3. Parse the left side to identify the pattern (x's position and operation)
4. Apply the appropriate mathematical operation to solve for x
5. Return the calculated value

### Implementation
The function uses pattern matching to identify different equation formats and applies the corresponding algebraic operations to isolate the variable x.