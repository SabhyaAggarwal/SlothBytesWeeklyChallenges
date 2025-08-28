# Valid Hex Code

This Rust project contains a function `is_valid_hex_code` that determines whether a string is a valid hex color code.

## Problem Description

Create a function that determines whether a string is a valid hex code.

A hex code must:
- Begin with a pound key `#`
- Be exactly 6 characters in length (after the `#`)
- Each character must be a digit from 0-9 or an alphabetic character from A-F
- All alphabetic characters may be uppercase or lowercase

## What it Does

The `is_valid_hex_code` function takes a string slice (`&str`) as input and returns a boolean value indicating whether the input represents a valid hex color code.

## How it Works

The function validates a hex code through a series of checks:

1. **Prefix Check**: Verifies that the string starts with a `#` character
2. **Length Check**: Ensures the total length is exactly 7 characters (`#` + 6 hex digits)
3. **Character Validation**: Checks that each character after `#` is a valid hexadecimal digit (0-9, A-F, a-f)

The function uses Rust's built-in `is_ascii_hexdigit()` method for efficient character validation.

## Usage

To use the function, call `is_valid_hex_code()` with a string slice. The function returns `true` for valid hex codes and `false` for invalid ones.

**Example Usage:**

```rust
println!("{}", is_valid_hex_code("#CD5C5C")); // true
println!("{}", is_valid_hex_code("#EAECEE")); // true
println!("{}", is_valid_hex_code("#eaecee")); // true
println!("{}", is_valid_hex_code("#CD5C58C")); // false
```

**Running the Program:**

```bash
cargo run
```

**Running Tests:**

```bash
cargo test
```

## Examples

| **Input** | **Output** | **Explanation** |
|:----------|:-----------|:----------------|
| `"#CD5C5C"` | `true` | Valid hex code with uppercase letters |
| `"#EAECEE"` | `true` | Valid hex code with uppercase letters |
| `"#eaecee"` | `true` | Valid hex code with lowercase letters |
| `"#CD5C58C"` | `false` | Length exceeds 6 characters (7 characters) |
| `"#CD5C5Z"` | `false` | Contains invalid character 'Z' |
| `"#CD5C&C"` | `false` | Contains unacceptable character '&' |
| `"CD5C5C"` | `false` | Missing required '#' prefix |

## Performance

The algorithm runs in O(n) time complexity where n is the length of the input string (which is constant for valid hex codes). It uses constant space and performs only simple character checks without complex operations.

## Requirements

This project requires Rust (edition 2024) and uses only built-in Rust functionality (no external dependencies).