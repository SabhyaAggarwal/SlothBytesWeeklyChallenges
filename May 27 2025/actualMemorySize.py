def actualMemorySize(ms):
    if 'GB' in ms:
        value = float(ms.replace('GB', ''))
        total_mb = value * 1000
    elif 'MB' in ms:
        value = float(ms.replace('MB', ''))
        total_mb = value
    else:
        return f'output = "Invalid input format: {ms}"'

    actual_mb = total_mb * 0.93

    if actual_mb >= 1000:
        actual_gb = actual_mb / 1000
        result_string = f"{actual_gb:.2f}GB"
    else:
        result_string = f"{round(actual_mb)}MB"

    print(f'output = "{result_string}"')

# Example 1
#actualMemorySize("32GB") # Expected Output: output = "29.76GB"

# Example 2
#actualMemorySize("2GB")  # Expected Output: output = "1.86GB"

# Example 3
#actualMemorySize("512MB") # Expected Output: output = "476MB"
