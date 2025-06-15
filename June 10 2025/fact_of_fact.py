import math

def fact_of_fact(n: int):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        print(f"output = 1")
        return

    result = 1
    for i in range(n, 0, -1):
        current_factorial = math.factorial(i)
        result *= current_factorial
    print(f"output = {result}")

#Some examples

#fact_of_fact(4)
#output = 288

#fact_of_fact(5)
#output = 34560

#fact_of_fact(6)
#output = 24883200
