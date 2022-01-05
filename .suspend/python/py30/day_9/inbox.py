# Check gmail inbox
import imaplib
import email

host = 'imap.gmail.com'
username = 'thisisnotmeofcourse@gmail.com'
password = 'hahahehehoHo71!'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select('inbox')

