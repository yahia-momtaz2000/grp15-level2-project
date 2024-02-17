print('-------  # Filter a list of numbers to include only even numbers using a lambda function and filter -------')
# normal way
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
for item in numbers_list:
    if item % 2 == 0:
        even_list.append(item)

print(even_list)

# using filter function without lambda
def get_even_num(item):
    if item % 2 == 0:
        return item

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(  filter( get_even_num, numbers_list)  )
print(even_list)

# using filter function with lambda
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter( lambda item : item % 2 == 0, numbers_list))
print(even_list)


print('---- Filter a list of strings to include only those with length greater than 5 using a lambda function and filter------')
# using normal way
words_list = ['apple', 'banana', 'kiwi', 'orange', 'grape']
new_words_list = []
for item in words_list:
    if len(item) > 5:
        new_words_list.append(item)
print(new_words_list)

# using filter function without lambda
def get_word_by_len(item):
    if len(item) > 5:
        return item

words_list = ['apple', 'banana', 'kiwi', 'orange', 'grape']
new_words_list = list( filter(get_word_by_len, words_list)  )
print(new_words_list)

# using filter function with lambda
words_list = ['apple', 'banana', 'kiwi', 'orange', 'grape']
new_words_list = list( filter( lambda item : len(item) > 5, words_list)  )
print(new_words_list)




