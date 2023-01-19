# Python Program to flattenNestedList

my_list = [[1], [2, 3], [4, 5, 6, 7]]

# Option 1

flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)

# Option 2

flat_list = []
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)

print(flat_list)

# Option 3

import itertools

flat_list = list(itertools.chain(*my_list))
print(flat_list)

# Option 4

flat_list = sum(my_list, [])
print(flat_list)