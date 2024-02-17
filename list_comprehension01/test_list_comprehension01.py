
print('--- Adding items to new list Using List Comprehension ---')
my_list = [5, 10, 30]

# using normal way
new_list = []
for item in my_list:
    new_list.append(item)

print(new_list)

# using list comprehension
new_list = [item for item in my_list]
print(new_list)

print('--- Create new list with numbers from 1 to 10 Using List Comprehension ---')
numbers_list = [i for i in range(1, 11)]
print(numbers_list)

print('---- Double items * 2 to new list Using List Comprehension ----')
my_list = [4, 7, 2, 5, 19]
double_list = [item * 2 for item in my_list]
print(double_list)

print('---- create new list of letters from a string Using List  ------')
my_string = 'Egypt'
letters_list = [letter.upper() for letter in my_string]
print(letters_list)

print('---- # create new list add only even numbers Using List Comprehension----')
my_list = [4, 7, 2, 5, 18]
# normal way
even_list = []
for item in my_list:
    if item % 2 == 0:
        even_list.append(item)

print(even_list)

# By list comprehension
even_list = [item for item in my_list if item % 2 == 0]
print(even_list)

print('---- create new list return price or invalid price if    -ve Using List Comprehension ---')
prices_list = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# normal way
new_prices_list = []
for price in prices_list:
    if price > 0:
        new_prices_list.append(price)
    else:
        new_prices_list.append('Invalid')

print(new_prices_list)

# By List Comprehension --- if ternary operator
new_prices_list = [price if price > 0 else 'Invalid' for price in prices_list]


print('---- Recreate the last example using def function ----')
def check_price(price):
    return price if price > 0 else 'Invalid'

prices_list = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_prices_list = [check_price(price) for price in prices_list]
print(new_prices_list)