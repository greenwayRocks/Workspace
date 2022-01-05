# List of Dictionaries
user_1 = {'name': 'James Bond', 'addr': 'California'}
user_2 = {'name': 'Ned Stark', 'addr': 'New York'}

my_users = [user_1, user_2]
print('Keys | Values')
for user in my_users:
	keys = list(user.keys())
	values = list(user.values())
	print()
	for x in range(0, len(keys)):
		print('{:>4} | {:>11}'.format(keys[x], values[x]))
