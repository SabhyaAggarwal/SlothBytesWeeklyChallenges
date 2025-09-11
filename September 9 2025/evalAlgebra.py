def evalAlgebra(expr):
    remove_spaces = expr.replace(" ", "")
    
    left, right = remove_spaces.split('=')
    right_value = int(right)
    
    if '+x' in left:
        number = int(left.replace('+x', ''))
        x_value = right_value - number
        print(x_value)
    
    elif '-x' in left:
        number = int(left.replace('-x', ''))
        x_value = number - right_value
        print(x_value)
    
    elif left.startswith('x+'):
        number = int(left.replace('x+', ''))
        x_value = right_value - number
        print(x_value)
    
    elif left.startswith('x-'):
        number = int(left.replace('x-', ''))
        x_value = right_value + number
        print(x_value)
    
    elif left == 'x':
        x_value = right_value
        print(x_value)
    
    elif left == '-x':
        x_value = -right_value
        print(x_value)

evalAlgebra("2 + x = 19")
evalAlgebra("4 - x = 1")
evalAlgebra("x + 10 = 53")
evalAlgebra("-23 + x = -20")
evalAlgebra("10 + x = 5")
evalAlgebra("-49 - x = -180")
evalAlgebra("x - 22 = -56")