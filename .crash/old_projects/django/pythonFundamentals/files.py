# Open a file (create)
myFile = open('myFile.txt', 'w')

# Get info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JS')

myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')

myFile.write(' I also like PHP')

myFile.close()
