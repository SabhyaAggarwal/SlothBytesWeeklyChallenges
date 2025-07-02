# How Many Digits between 1 and N

This Python script defines a function `digits(n)` that calculates the total number of digits in all numbers between 0 and n (exclusive of both endpoints).

## Problem Description

Imagine you took all the numbers between 0 and n and concatenated them together into a long string. How many digits are there between 0 and n?

## What it Does

The `digits` function takes an integer `n` as input and calculates the total number of digits in all integers from 1 to n-1 (inclusive). It efficiently handles large inputs by using mathematical calculations rather than iterating through each number.

## How it Works

The function uses a mathematical approach to count digits efficiently:

1. **Edge Case**: If n ≤ 1, there are no numbers between 0 and n, so it returns 0.

2. **Digit Length Grouping**: Numbers are grouped by their digit length:
   - 1-digit numbers: 1, 2, 3, ..., 9 (9 numbers)
   - 2-digit numbers: 10, 11, 12, ..., 99 (90 numbers)
   - 3-digit numbers: 100, 101, 102, ..., 999 (900 numbers)
   - And so on...

3. **Calculation**: For each digit length group:
   - Determine how many numbers of that length fall within the range [1, n-1]
   - Multiply the count by the digit length to get total digits contributed
   - Sum up contributions from all groups

This approach ensures O(log n) time complexity, making it efficient for large inputs.

## Usage

To use the function, simply call `digits()` with an integer argument. The function will print the result directly to the console.

**Example Usage:**

```python
digits(1)
digits(10)
digits(100)
digits(2020)
```

## Examples

| **Input (n)** | **Range of Numbers** | **Calculation** | **Output** |
|:--------------|:---------------------|:----------------|:-----------|
| `1` | None (no numbers between 0 and 1) | 0 numbers = 0 digits | `output = 0` |
| `10` | 1, 2, 3, 4, 5, 6, 7, 8, 9 | 9 single-digit numbers = 9×1 = 9 digits | `output = 9` |
| `100` | 1 to 99 | 9 single-digit (9×1) + 90 double-digit (90×2) = 9 + 180 = 189 digits | `output = 189` |
| `2020` | 1 to 2019 | 9×1 + 90×2 + 900×3 + 1020×4 = 9 + 180 + 2700 + 4080 = 6969 digits | `output = 6969` |

## Performance

The algorithm runs in O(log n) time complexity, making it suitable for very large inputs. It uses constant space and performs only mathematical calculations without iterating through individual numbers.

## Requirements

This script requires Python 3 and uses only built-in Python functionality (no external dependencies).