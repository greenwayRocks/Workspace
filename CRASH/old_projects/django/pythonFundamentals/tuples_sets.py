# Tuples - ordered and unchangeable! Allows duplicate members

fruit_tuple = ('Apple', 'Orange', 'Mango')

# Using constructor
# fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

# Get single value
# print(fruit_tuple[1])

# CAnnot change value
# fruit_tuple[1] = 'Grape'

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

del fruit_tuple_2

# Get length of tuple
# print(len(fruit_tuple_2))


# Sets - unordered, unindexed, no duplicates

# Create set
fruit_set = {'Apple', 'Orange', 'Mango'}

print('Apple' in fruit_set)

# add to set
fruit_set.add('Grape')

# remove from set
fruit_set.remove('Grape')

# Clear set
fruit_set.clear()

# Delete set
del fruit_set

print(fruit_set)
