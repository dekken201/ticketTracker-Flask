import imaplib
import mailparser
from pymongo import MongoClient
client = MongoClient()
from datetime import datetime

now = datetime.now()

def start(IMAP_SERVER, EMAIL_ACCOUNT, PASSWORD, EMAIL_FOLDER,SENDER):
    M = imaplib.IMAP4_SSL(IMAP_SERVER)
    M.login(EMAIL_ACCOUNT, PASSWORD)
    rv, data = M.select(EMAIL_FOLDER)
    if rv == 'OK':
        print ("Processing mailbox: ", EMAIL_FOLDER)
        return process_mailbox(M,SENDER)
    else:
        print ("ERROR: Unable to open mailbox ", rv)
    M.close()
    M.logout()

def process_mailbox(M,sender):
    mails_dict = {}
    rv, data = M.search(None, '(FROM "'+sender+'")')
    if rv != 'OK':
        print ("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print ("ERROR getting message", num)
            return        

        mail = mailparser.parse_from_bytes(data[0][1])
        print ("Writing message ", num)
        mails_dict.update(convert_mail_to_dict(mail))
    return mails_dict

def convert_mail_to_dict(mail_object):
    message_id = mail_object.message_id.split('@')
    date = mail_object.date
    date = date.strftime('%H:%M-%d/%m/%Y')
    mail_dict = {message_id[0][1:]:
    {'body':mail_object.body, 
    'date':date,
    'delivered_to':mail_object.delivered_to,
    'from':mail_object.from_,   
    'message_as_string':mail_object.message_as_string,
    'received':mail_object.received,
    'subject':mail_object.subject, 
    'text_plain':mail_object.text_plain,
    'text_html':mail_object.text_html,
    'to':mail_object.to,
    'to_domains':mail_object.to_domains,
    'timezone':mail_object.timezone}}
    return mail_dict
