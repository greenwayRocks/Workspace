# Coding a bot that reads the news
import requests
from bs4 import BeautifulSoup
import redis
# from secrets import password
from datetime import datetime

class Scraper:
  def __init__(self):
    self.markup = requests.get('https://kathmandupost.com/sports').text
    #self.keywords = keywords

  def parse(self):
    soup = BeautifulSoup(self.markup, 'html.parser')
    links = soup.findAll('h3')
    self.saved_links = links
    # for link in links:
    #   for keyword in self.keywords:
    #     if keyword in link.text:
    #       self.saved_links.append(link)

  def store(self):
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.flushdb()
    for link in self.saved_links:
      r.set(link.text, str(link))

  def email(self):
    r = redis.Redis(host='localhost', port=6379, db=0)
    links = [r.get(k) for k in r.keys()]
    new_links = []
    for link in links:
      new_links.append(link.decode(encoding='utf-8').replace('<h3>', '<h6>'))
    print(new_links)
    

    import smtplib

    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    me = "thisisnotmeofcourse@gmail.com"
    you = "satishadhikari71@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = 'Anonymous <' + me + '>'
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    html = """
      <h4> {} links you might find interesting today:</h4>

      {}
    """.format(len(new_links), '<br><br>'.join(new_links))

    # Record the MIME types of both parts - text/plain and text/html.
    mime = MIMEText(html, 'html')

    msg.attach(mime)

    try:
      mail = smtplib.SMTP('smtp.gmail.com', 587)

      mail.ehlo()

      mail.starttls()

      mail.login('thisisnotmeofcourse@gmail.com', 'hahahehehoHo71!')
      mail.sendmail(me, you, msg.as_string())
      mail.quit()
    except Exception as e:
      print('Something went wrong {}'.format(e))


if __name__ == '__main__':
  s = Scraper()
  s.parse()
  s.store()
  if datetime.now().hour == 12:
    s.email()