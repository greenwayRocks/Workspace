# Comparision Operators

x = 11
y = 11

# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{x} is less than {y}')

# # elif
# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y:
#     print(f'{x} is equal to {y}')
# else:
#     print(f'{x} is less than {y}')


# # nested if
# if x > 2:
#     if x <= 10:
#         print(f'{x} is less than 11 and greater than 2 ')


# Logical operators

if x > 2 and x <= 10:
    print(f'{x} is less than 11 and greater than 2 ')

if not (x == y):
    print(f'{x} is not equal to {y}')


numbers = [1, 2, 3, 4, 5, 6]

# Membership operators
if x in numbers:
    print(x in numbers)

if y not in numbers:
    print(y not in numbers)

# Identity
if x is not y:
    print(x is not y)
