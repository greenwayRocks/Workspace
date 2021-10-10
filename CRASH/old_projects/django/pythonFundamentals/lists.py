# Lists (array)

# Create list
# numbers = [1, 2, 3, 4, 5]

# Using constructor
numbers = list((1, 2, 3, 4, 5))
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

print(fruits[1])

# GEt length
print(len(fruits))

# Append to list
fruits.append('Mangoes')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberries')

# remove from position
fruits.pop(3)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# reverse sort
fruits.sort(reverse=True)

print(fruits)
