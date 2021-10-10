import re
print(re.sub(r'[\w.%+-]+@[\w.-]+', '[REDACTED]',
             'Received an email for go_nuts75@gmail.com'))

print(re.sub(r"^([\w .-]+), ([\w. ]+)$", r"\2 \1", "Lovelace, Ada"))
