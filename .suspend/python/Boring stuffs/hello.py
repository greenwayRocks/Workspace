# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name? ', end='')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:', end=' ')
print(len(myName))

print('Your Age? ', end='')
myAge = int(input())
print('You will be ' + str(myAge + 1) + ' in a year.')
