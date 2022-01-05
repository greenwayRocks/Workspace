import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# Check for cmd line args
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
