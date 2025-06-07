# Next Letters Alphabetically

This repository contains a simple Python function, `next_letters`, designed to increment a given string of capital English letters alphabetically. It works similarly to how numbers increment, handling "carry-overs" when a 'Z' is encountered.

---

## Function: `next_letters(s: str) -> str`

This function takes a string `s` as input and returns a new string where the letters are incremented alphabetically.

### How it Works

The function treats the input string like a number in a base-26 system (where 'A' is 0, 'B' is 1, ..., 'Z' is 25). It starts from the rightmost character and attempts to increment it.

* If a character is not 'Z', it's simply changed to the next letter (e.g., 'A' becomes 'B', 'C' becomes 'D').

* If a character is 'Z', it "rolls over" to 'A', and a "carry" is propagated to the character on its left, which then attempts to increment. This process continues until no more carry is needed or the beginning of the string is reached.

* If a carry remains after processing the entire string (e.g., when incrementing "Z"), a new 'A' is prepended to the string.

### Examples

| Input (`s`) | Output        | Explanation                                                                                                                                                                                            |
| :---------- | :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"A"`       | `output="B"`  | 'A' becomes 'B' – a simple increment.                                                                                                                                                                |
| `"ABC"`     | `output="ABD"` | 'C' becomes 'D' – the last character changes without a carry.                                                                                                                                          |
| `"Z"`       | `output="AA"` | 'Z' rolls over to 'A', and since there's no previous letter, a new 'A' is added. Think of it like `9 + 1 = 10`, here `Z + 1 = AA`.                                                                |
| `"CAZ"`     | `output="CBA"` | 'Z' rolls over to 'A' (with a carry). The carry increments 'A' to 'B'. So, "CAZ" becomes "CBA". This is analogous to incrementing `129` to `130` in a decimal system.                                |
| `""`        | `output="A"`  | An empty input string is treated as the starting point (like 0 in numbers), so incrementing it results in 'A'.                                                                                          |

---

### Usage

To use the function, simply call it with your desired string. The function will print the result directly to the console in the format `output="result_string"`.

```python
# Example usage:
# next_letters("APPLE") # This will print: output="APPLF"
# next_letters("AZZ")   # This will print: output="BAA"
# next_letters("")      # This will print: output="A"
```
### Notes

- All test cases assume input strings will be in CAPITAL letters.
- An empty input string ("") will result in `output="A"`.

