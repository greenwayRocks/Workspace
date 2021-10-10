# Strings

name = 'Tom'
age = 20

# Concatenate
# print('Hello I am ' + name + ' and I am ' + str(age))

# String Formatting
# ------------------------

# Arguments by position
# print('{2}, {0}, {1}'.format('a', 'b', 'c'))

# Arguments by name
# print('My name is {name} and I am {age} years old.'.format(name=name, age=age))

# F-Strings
# print(f'My name is {name} and I am {age}')

# -------------------------------------------


# String Methods

s = 'hello there world'

# Capitalize first letter
print(s.capitalize())

# Capitalize all
print(s.upper())

# Lowercase all
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyoNe'))

# Count
print(s.count('e'))

# Checks
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())

# Find position
print(s.find('r'))

# Starts with
print(s.startswith('hel'))
# Ends with
print(s.endswith('rld'))

# Split to list(array)
print(s.split())
