from functools import reduce
print('--------------- Calculate the product of all elements in a list using the reduce function --------------')
# normal way
numbers_list = [2, 3, 4, 5]
product_result = 1
for item in numbers_list:
    product_result = product_result * item
print(product_result)
print('------------------------------')
# using reduce function - No lambda
def multiply_data(num1, num2):
    return num1 * num2

numbers_list = [2, 3, 4, 5]
product_result = reduce(multiply_data, numbers_list)
print(product_result)

# using reduce - with lambda
numbers_list = [2, 3, 4, 5]
product_result = reduce(lambda num1, num2 : num1 * num2, numbers_list)
print(product_result)

print('------------------- Concatenate a list of strings into a single string using the reduce function------------------')
# normal way
words_list = ['Welcome', ' to ', ' Python ', '!']
words_string = ''
for word in words_list:
    words_string = words_string + word
print(words_string)

# using reduce with no lambda
def concat_string(word1, word2):
    return word1 + word2

words_list = ['Welcome', ' to ', ' Python ', '!']
words_string = reduce(concat_string , words_list)
print(words_string)


# using reduce with lambda
words_list = ['Welcome', ' to ', ' Python ', '!']
words_string = reduce(lambda word1, word2 : word1 + word2 , words_list)
print(words_string)

