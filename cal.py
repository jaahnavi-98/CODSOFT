def calculate(j1, j2, oper):
    if oper == '+':
        result = j1 + j2
    elif oper == '-':
        result = j1 - j2
    elif oper == '*':
        result = j1 * j2
    elif oper == '/':
        result = j1 / j2
    elif oper == '^':
        result = j1 ** j2
    else:
        raise ValueError('Invalid operator')
    return result
j1 = float(input('Enter the first number: '))
j2 = float(input('Enter the second number: '))
oper = input('Enter the operator (+, -, *, /, ^): ')
result = calculate(j1, j2, oper)
print(f'Result: {result:.2f}')