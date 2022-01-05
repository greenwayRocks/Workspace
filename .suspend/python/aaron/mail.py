import os
import sys
import smtplib

EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

def mail():
    if not EMAIL_USER or not EMAIL_PASS:
        print('Sender email or password is not provided. Use env variables:\nEMAIL_USER and EMAIL_PASS')
        sys.exit(1)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_USER, EMAIL_PASS)

        # Message
        subject = 'Your web server is down'
        body = 'The cloud servers are down and this script is restarting them, check it out!'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_USER, 'satishadhikari71@gmail.com', msg)

if __name__ == '__main__':
    mail()