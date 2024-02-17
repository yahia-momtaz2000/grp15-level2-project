print('---- Create inner function used to change variable from outer function and the change is still referenced from the namespace ---')

def outer_function(name, salary):
    def inner_function(address):
        nonlocal salary
        salary = salary + 5000
        print(name, salary, address) # 11000
    return inner_function


# main program
function_reference = outer_function('Yahia', 6000)
function_reference('Cairo')
function_reference('Alex')
function_reference('Aswan')


print('---- Free variables references from namespace and still change them----')

def outer_function(name, salary):
    def inner_function(bonus):  # The Closure Function
        nonlocal salary
        salary = salary + bonus
        print(name, salary)
    return inner_function   # return closure function - without ( )


# main program
function_reference = outer_function('Yahia', 6000)
print('Call inner function : ')
function_reference(7000)     # print Yahia 13000 Cairo
function_reference(2000)     # print Yahia 15000 Cairo
