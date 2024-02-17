
print('Create inner function used to print variable from outer function')

def outer_function(name):
    def inner_function():
        print(f'Hello {name}')
    print(f'Hi {name}')
    inner_function() # call the inner function

# main program
outer_function('Yahia')


print('--- Create inner function used to change variable from outer function-----')

def outer_function(name, salary):
    def inner_function():
        nonlocal salary
        salary = 5000
        print(name, salary) # 5000
    inner_function()
    print(name, salary) # 5000

# main program
outer_function('Yahia', 6000)


print('----- Create inner function used to change variable'
      '  from outer function and the change is still referenced from the outer function ---')
def outer_function(name, salary):
    def inner_function():
        nonlocal salary
        salary = salary + 5000
        print(name, salary) # Y 110000
    inner_function()
    print(name, salary) # Y 11000

# main program
outer_function('Yahia', 6000)
