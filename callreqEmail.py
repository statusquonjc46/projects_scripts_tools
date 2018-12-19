#! /usr/bin/env python

import imaplib
import email
import re

email_user = input('Email: ')
email_pass = input('Password: ')
print('Logging in...' + '\n')
pyCon = imaplib.IMAP4_SSL('imap.secureserver.net', 993)
pyCon.login(email_user, email_pass)
pyCon.select()
print('Connected to imap server for: ' + email_user + '\n')
emailType, messages = pyCon.search(None, 'ALL')

for num in messages[0].split():
    emailType, emailData = pyCon.fetch(num, '(RFC822)')

    print('--------------------------------------------------------' + '\n')
    print('RAW DATA: ', emailData)
    print('\n' + '--------------------------------------------------------' + '\n')

    formattedEmail = email.message_from_bytes(emailData[0][1])
    print('Formatted Email: ')
    print(formattedEmail)
    print('\n')
    print('--------------------------------------------------------' + '\n')

    print('Human-readable email: ' + '\n')
    msgFrom = formattedEmail['from']
    msgTo = formattedEmail['to']
    msgSub = formattedEmail['subject']

    print('From: ' + msgFrom + '\n')
    print('To: ' + msgTo + '\n')
    print('Subject: ' + msgSub + '\n')

    #if formattedEmail.is_multipart():
      #  for payload in formattedEmail.get_payload():
     #       print(payload.get_payload())
    #else:
     #   print(formattedEmail.get_payload(decode=True))
    #type(formattedEmail)

    if formattedEmail.is_multipart():
        for walker in formattedEmail.get_payload():
            conType = walker.get_content_type()
            dispo = str(walker.get('Content-Disposition'))

            if conType == 'text/plain' and 'attachment' not in dispo:
                body = walker.get_payload()
                print(body)
                break
            if conType == 'text/html' and 'attachment' not in dispo:
                body = walker.get_payload()
                TAG_RE = re.compile(r'<[^>]+>')
                cleantext = re.sub(TAG_RE, '', body)
                cleantext = cleantext.replace('&nbsp;', '')
                cleantext = cleantext.replace('&nbsp=', '')
                cleantext = cleantext.replace(';&n=', '')
                cleantext = cleantext.replace('bsp;', '')
                print(cleantext)
    else:
        body = walker.get_payload()
        print(body)
        print('3')
pyCon.close()
print('Closing connection...\n')
pyCon.logout()
print('Logged out. Goodbye.')