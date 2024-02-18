print('----- The factorial of 6 is denoted as 6! = 1*2*3*4*5*6 = 720.  ------')

# normal way without function
number = 6
factorial_result = 1
for i in range(1, number + 1):
    factorial_result = factorial_result * i

print(factorial_result)

# normal way with function
def calc_factorial(number):
    factorial_result = 1
    for i in range(1, number + 1):
        factorial_result = factorial_result * i
    return factorial_result

print(calc_factorial(6))


# recursion function
def factorial_recursion(number):
    if number == 1:
        return number
    else:
        return number * factorial_recursion(number - 1)

print(factorial_recursion(6))

