import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('email.html').read_text())
email = EmailMessage()
email['from'] = 'Cori Komiyama'
email['to'] = 'cori.komiyama@gmail.com'
email['subject'] = 'Response needed immediately!'

email.set_content(html.substitute(name='Molly'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: #as protocol, this port and syntax is standard
    smtp.ehlo()
    smtp.starttls() #encryption mechanism to connect securely to the server
    smtp.login('corikiyomi@gmail.com', 'joqi selx ocax grmk')
    smtp.send_message(email)
    print('All good, boss!')

