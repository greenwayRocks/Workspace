thinkers = ['Plato', 'PlayDo', 'Gumby']
while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as err:
        print(f'We tried to pop too many thinkers! [{err}]')
        break
