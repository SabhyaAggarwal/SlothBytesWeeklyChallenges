# `actualMemorySize` Function(mentioned)

This `README.md` explains the Python function `actualMemorySize`, which calculates the actual usable memory of a USB flash drive based on its advertised size.

---

## What it Does

The `actualMemorySize` function takes a string representing the advertised memory capacity of a USB flash drive (e.g., "32GB", "512MB"). It then calculates and prints the actual usable memory, accounting for a standard 7% storage loss.

---

## How it Works (Calculation Logic)

1.  **Input Parsing:** The function first extracts the numerical value and the unit (GB or MB) from the input string.
2.  **Conversion to MB:** All memory sizes are internally converted to Megabytes (MB) for consistent calculation. For this challenge, **1 Gigabyte (GB) is treated as 1000 Megabytes (MB)**.
3.  **Loss Calculation:** A **7% loss** is applied to the total memory. This means the actual usable memory is 93% of the advertised size.
4.  **Output Formatting:**
    * If the calculated actual memory size is **1 Gigabyte (1000 MB) or greater**, the result is converted back to Gigabytes and **rounded to two decimal places**.
    * If the calculated actual memory size is **less than 1 Gigabyte (1000 MB)**, the result is returned in **Megabytes (MB)**, rounded to the nearest whole number.

---

## Usage

To use the function, just call `actualMemorySize()` with a string representing the memory size.

**Example:**

```python
actualMemorySize("32GB")
```

## Output
The function prints its output directly to the console in the format `output = "..."`.

- For sizes 1GB or greater, the output will be like `output = "29.76GB"`.
- For sizes less than 1GB, the output will be like `output = "476MB"`.

## Examples
Here are the examples demonstrating the function's behavior:
```python
actualMemorySize("32GB")
# Expected Output: output = "29.76GB"

actualMemorySize("2GB")
# Expected Output: output = "1.86GB"

actualMemorySize("512MB")
# Expected Output: output = "476MB"
```
