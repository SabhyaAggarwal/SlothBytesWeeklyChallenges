def digits(n):
    if n <= 1:
        print("output = 0")
        return
    
    total_digits = 0
    current_power = 1
    digit_length = 1
    
    remaining = n - 1
    
    while remaining > 0:
        if digit_length == 1:
            range_start = 1
            range_end = 9
        else:
            range_start = current_power
            range_end = current_power * 10 - 1
        
        if remaining >= range_end:
            count = range_end - range_start + 1
            remaining -= count
        else:
            count = remaining
            remaining = 0
        
        total_digits += count * digit_length
        
        current_power *= 10
        digit_length += 1
    
    print(f"output = {total_digits}")
