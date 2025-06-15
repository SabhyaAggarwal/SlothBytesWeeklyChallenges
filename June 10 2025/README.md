# Factorial of Factorials

This Python script defines a single function, `fact_of_fact(n)`, that calculates the "factorial of factorials" for a given non-negative integer `n`.

## What is Factorial of Factorials?

The factorial of factorials for a number `n` is the product of the factorials of all integers from `n` down to 1.
Mathematically, it's represented as:

$n! \times (n-1)! \times \dots \times 2! \times 1!$

## How to Use

To run the function, simply call `fact_of_fact()` with an integer argument. The function will print the result directly to the console.

**Example Usage:**

```python
fact_of_fact(4)
fact_of_fact(5)
fact_of_fact(6)
```

## Examples
| **Input (n)** | **Calculation**                                                    | **Output (output = result)** |
|:--------------|:-------------------------------------------------------------------|:-----------------------------|
| `4`           | $4! \times 3! \times 2! \times 1! = 24 \times 6 \times 2 \times 1$ | `output = 288`               |
| `5`           | $5! \times 4! \times 3! \times 2! \times 1!$                       | `output = 34560`             |
| `6`           | $6! \times 5! \times 4! \times 3! \times 2! \times 1!$             | `output = 24883200`          |

## Requirements
This script requires Python 3 and uses the built-in `math` module, which is part of the standard Python library.
