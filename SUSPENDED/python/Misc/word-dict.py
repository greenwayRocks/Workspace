# This is a word dictionary

dictionary = {
    'programming': 'Set of code for computers',
    'python': 'A powerful scripting language',
    'ai': 'idk'
}

search = input('[*] Search: ')

print('{} - {}'.format(search, dictionary[search.lower()]))
