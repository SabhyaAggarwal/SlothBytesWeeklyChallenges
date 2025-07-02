def digits(n):
    """
    Calculate the total number of digits in all numbers between 0 and n (exclusive).
    
    Args:
        n (int): The upper bound (exclusive)
    
    Returns:
        None: Prints the result in the format "output = <result>"
    """
    if n <= 1:
        print("output = 0")
        return
    
    total_digits = 0
    current_power = 1  # 10^0 = 1
    digit_length = 1
    
    # We count digits for numbers 1 to n-1
    remaining = n - 1
    
    while remaining > 0:
        # Calculate range for current digit length
        # For 1-digit: 1 to 9 (9 numbers)
        # For 2-digit: 10 to 99 (90 numbers)  
        # For k-digit: 10^(k-1) to 10^k - 1
        
        if digit_length == 1:
            range_start = 1
            range_end = 9
        else:
            range_start = current_power
            range_end = current_power * 10 - 1
        
        # Count how many numbers of this digit length are in our range
        if remaining >= range_end:
            # All numbers of this digit length are included
            count = range_end - range_start + 1
            remaining -= count
        else:
            # Only some numbers of this digit length are included
            count = remaining
            remaining = 0
        
        # Add digits from these numbers
        total_digits += count * digit_length
        
        # Move to next digit length
        current_power *= 10
        digit_length += 1
    
    print(f"output = {total_digits}")

# Test cases (commented out for now)
# digits(1)    # output = 0
# digits(10)   # output = 9  
# digits(100)  # output = 189
# digits(2020) # output = 6969