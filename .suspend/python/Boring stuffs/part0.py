with open('SecretPasswordFile.txt', 'r') as f:
    secretPassword = f.read().strip('\n')
    print('Enter your password: ', end='')
    typedPassword = input()

    if typedPassword == secretPassword:
        print('Access granted')
        if typedPassword == '12345':
            print('That password is one that an idiot puts on their luggage.')
    else:
        print('Access denied')
        print(typedPassword + ' is not the same as ' + secretPassword)
