import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail:
    def __init__(self, to_emails=[], text='Maybe this text is being sent to you!'):
        self.text = text
        self.html = ''
        self.subject = 'Hello World'
        self.to_emails = to_emails
        self.from_email = 'Hungry Py <thisisnotmeofcourse@gmail.com>'
        self.username = 'thisisnotmeofcourse@gmail.com'
        self.password = 'hahahehehoHo71!'
    
    def send_mail(self):
        assert isinstance(self.to_emails, list)
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = ','.join(self.to_emails)
        msg['Subject'] = self.subject

        txt_part = MIMEText(self.text, 'plain')
        msg.attach(txt_part)
        if self.html:
            html_part = MIMEText(self.html, 'html')
            msg.attach(html_part)

        # Message string
        msg_str = msg.as_string()

        # Login to smtp server
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login(self.username, self.password)
        server.sendmail(self.from_email, self.to_emails, msg_str)

        server.quit()

if __name__ == '__main__':
    m = Mail(['satishadhikari71@gmail.com', 'sandeshadhikari92@gmail.com'])
    m.send_mail()