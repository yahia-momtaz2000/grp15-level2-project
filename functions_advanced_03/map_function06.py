import math

print('---- Loop over list of words and create another list with the words length ----')
words_list = ['ahmed','omar','hamada','ayman']

# normal way
words_len_list = []
for item in words_list:
    words_len_list.append(len(item))

print(words_len_list)
# using list comprehension
words_len_list = [len(item) for item in words_list]
print(words_len_list)

# using map - No lambda
def get_word_len(word):
    return len(word)

words_len_list = list( map(get_word_len, words_list))
print(words_len_list)

# using map - lambda
words_len_list = list( map(lambda word : len(word), words_list))
print(words_len_list)

print('----------------  Loop over the list and cube each element -----------------')
numbers_elements = [4, 5, 2, 10, 3]

# normal way
cubic_list = []
for item in numbers_elements:
    cubic_list.append( item ** 3 )
print(cubic_list)

# using list comprehension
cubic_list = [item ** 3 for item in numbers_elements]
print(cubic_list)

# map - no lambda
def calc_cubic(item):
    return item ** 3

cubic_list = list(map(calc_cubic, numbers_elements))
print(cubic_list)

# map - lambda
cubic_list = list(map(lambda item: item ** 3 , numbers_elements))
print(cubic_list)

print('-------------  : add each element in list 1 to their corresponding elements in list 2  ------------')
list1 = [7, 5, 3, 10, 22]
list2 = [8, 3, 7 ,6 , 9]

# normal way
list3 = []
for i in range(len(list1)):
    list3.append( list1[i] + list2[i]  )
print(list3)

# using map - no lambda
def add_elements(num1, num2):
    return num1 + num2

list3 = list(map(add_elements, list1, list2))
print(list3)

# using map - with lambda
list3 = list(map(lambda num1, num2 : num1 + num2, list1, list2))
print(list3)