'''
# TEXT Processing Tool
RegeX :: Allows us to search for text with specific PATTERNS.
  e.g.: -> What are all the four-letter words in a file?
        -> How many different error types are there in this error log?
  -- Usage while extracting only server names from a file that lists NFS mounts.
  (Strips each line of the excess data & returns only the info needed!)
>>> re.search(r'p.ng', 'Penguin', re.IGNORECASE)
>>> re.search(r'[Pp]ython', 'Python')
>>> print(re.search(r'[a-z]way', 'The end of the highway'))
>>> print(re.search('cloud[a-zA-Z0-9]', 'cloud9'))
>>> print(re.search(r'[^a-zA-Z]', 'This is a sentence with spaces.')) # returns first ' '
>>> print(re.search(r'[^a-zA-Z ]', 'This is a sentence with spaces.')) # returns '.' 
>>> print(re.search(r'cat|dog', 'I like dogs.'))
>>> print(re.findall(r'cat|dog', 'I like both dogs and cats.'))
The '.*' has GREEDY behavior, takes as much as it can get!
>>> print(re.search(r'Py.*n', 'Python Programming'))
>>> print(re.search(r'Py[a-z]*n', 'Pyn'))
Wildcard: . (matches any character in the world!)
Character classes: [a-zA-Z0-9]
Repetition qualifiers: *, extended (+, ?)

Escaping special characters: .*+?^$[]
In a search pattern if we see backslash '\',
>> it could be escaping special regex character OR,
>> a special string character ('\n', '\t' etc.)

Python's special sequences with backslash:
-> \w (matches any alphanumeric character inc. letters, numbers & underscores)
-> \d (matches digits)
-> \s (matches whitespace characters [spaces, tabs, newlines])
-> \b (for word boundaries)
'''

# ADVANCED regeX
'''
# Capturing Groups
    - Get portion of pattern that are enclosed in parantheses.
>>> result = re.search(r'^(\w+), (\w+)$', 'Lovelace, Ada')
>>> print(result.groups())
>>> print(result[0])
>>> print(result[1]) => Lovelace
>>> print(result[2]) => Ada
>>> '{} {}'.format(result[2], result[1])
>>> r'^([\w \.-]+), ([\w \.-]+)$'
Repetition Qualifiers:
---------------------
>>> print(re.search(r'[a-zA-Z]{5}', 'a ghost'))
>>> print(re.findall(r'\b[a-zA-Z]{5}\b', 'a scary ghost appeared'))

# Extract PID
>>> def extract_pid(log):
        regex = r"\[(\d+)\]"
        result = re.search(regex, log)
        if not result:
          return ''
        return result[1]
'''
