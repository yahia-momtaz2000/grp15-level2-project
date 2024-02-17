print('Set creation and printing')
my_set = {5, 6, 15, 12, 4, 6, 7, 3, 7}
print(my_set)
print(type(my_set))

print('---- add new elements ---')
my_set.add(20)
print(my_set)

print('----- Find elements ------')
print( 21 in my_set ) # False | True

print('------- Change element ------')
# cannot change element as there is no index : workaround ( Remove old > add new )
my_set.remove(20)
my_set.add(8)
print(my_set)

print('---- Count element -------')
print(len(my_set))

print('------ Loop over elements using foreach loop ---------')
for item in my_set:
    print(item)

print('------ Remove Element --- discard() remove() pop() --------')
print(my_set)
my_set.pop()
print(my_set)
my_set.remove(8)
print(my_set)
my_set.discard(15)
print(my_set)

print('-------- Sort set ----------')
my_list = sorted(my_set)
print(my_list)

print('---------- Convert from List to set and vice versa ------- ')
print(my_set)
items_list = list(my_set)   # int()         str()       float()
items_set = set(my_list)