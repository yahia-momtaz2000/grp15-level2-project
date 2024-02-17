import math

print('------------ Make a number power to a value using lambda  -----------')
# normal way
def power_number(num, pow):
    return math.pow(num, pow)


# main program
result = power_number(2, 3)
print(result)


# Using Lambda function ( inline function ) ( Anonymous function )
function_reference = lambda num, pow : math.pow(num, pow)
result = function_reference(2, 3)
print(result)



print('----------- Make a string to upper case using lambda -------------')
# normal way
def make_upper(my_statement):
    return my_statement.upper()


# main program
my_statement = 'I Love using Python'
result = make_upper(my_statement)
print(result)


# using lambda
function_reference = lambda my_statement : my_statement.upper()
result = function_reference('I Love using Python')
print(result)



print('----- check and return even or odd value for a number -------')
# normal way
def check_even_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'


# main program
result = check_even_odd(16)
print(result)

# lambda :
function_reference = lambda num : 'even' if num % 2 == 0 else 'odd'
result = function_reference(16)
print(result)