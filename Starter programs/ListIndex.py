# Python Program to acess a certain list index

my_list = [100, 654, 2, 61]

# Option 1

for index, val in enumerate(my_list):
    print(index, val)

# Option 2

for index, val in enumerate(my_list, start=1):
    print(index, val)

# Option 3

for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)