import hashlib

pass_hass = input('Enter md5 hash: ')
counter = 

wordlist = input('File name: ')

try:
    pass_file = open(wordlist, 'r')
except:
    print('No file found')
    quit()

for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    print(word)
    print(digest)
    print(pass_hass)

    if digest == pass_hash:
        print('Password found')
        print('password is ' + word)
        flag = 1
        break

if flag == 0:
    print('password/passphrase is not in the list')
