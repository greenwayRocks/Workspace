# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip modules
import camelcase

# today = datetime.date.today()
today = date.today()

timestamp = time()

camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))
