# Launch sites randomly in browser
import webbrowser
import time
import random

while True:
    site = random.choice(['google.com', 'youtube.com',
                          'facebook.com', 'instagram.com'])
    visit = 'http://{}'.format(site)
    webbrowser.open(visit)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)
