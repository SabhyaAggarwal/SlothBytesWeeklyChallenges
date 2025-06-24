# Birthday Cake Candles

This project contains a Python function `birthdayCakeCandles` that solves the Birthday Cake Candles problem.

## Function: `birthdayCakeCandles(candles)`

The `birthdayCakeCandles` function is designed to count how many candles are the tallest given a list of candle heights.

### How it Works

1.  **Input**: The function accepts a single argument:
    *   `candles`: A list of integers representing the heights of the candles.

2.  **Process**:
    *   It first checks if the list of `candles` is empty. If it is, the function prints `0` and exits.
    *   If the list is not empty, it iterates through the `candles` list once to find the `max_height`.
    *   Then, it iterates through the `candles` list again to count how many candles have a height equal to `max_height`.
    *   Finally, it prints this `count`.

3.  **Output**:
    *   The function does not return a value. Instead, it directly prints the integer count of the tallest candles to the console.

### Examples

Here's how you can use the function and the expected output:

```python
# Example 1
birthdayCakeCandles([4, 4, 1, 3])
# Expected output: 2
# Explanation: The tallest candles are of height 4. There are 2 such candles.

# Example 2
birthdayCakeCandles([1, 1, 1, 1])
# Expected output: 4
# Explanation: All candles are of height 1, so all are the tallest.

# Example 3
birthdayCakeCandles([])
# Expected output: 0
# Explanation: There are no candles.
```

To run these examples, you would typically call the function with the desired list of candle heights. The result will be printed to your console.
