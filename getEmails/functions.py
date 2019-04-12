import imaplib
import mailparser
import json
from datetime import datetime
import os

now = datetime.now()
def start(IMAP_SERVER, EMAIL_ACCOUNT, PASSWORD, EMAIL_FOLDER,SENDER):
    M = imaplib.IMAP4_SSL(IMAP_SERVER)
    M.login(EMAIL_ACCOUNT, PASSWORD)
    rv, data = M.select(EMAIL_FOLDER)
    if rv == 'OK':
        print ("Processing mailbox: ", EMAIL_FOLDER)
        process_mailbox(M,SENDER)
        M.close()
    else:
        print ("ERROR: Unable to open mailbox ", rv)
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

    while True:
        filePath = os.path.abspath(__file__)
        for i in range(2):
            filePath = os.path.dirname(filePath)


        date = now.strftime("%Y%m%d")
        retorno = dump_json(filePath+"/output/entradaJson_"+date+".txt",mails_dict)    
        if retorno == "ok":
            print("Mensagens salvas com sucesso")
            break
        else:
            print(retorno)
            break

def convert_mail_to_dict(mail_object):
    mail_dict = {}
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

def dump_json(filename,mails_dict):
    try:
        with open(filename, 'w') as outfile:
            json.dump(mails_dict, outfile)
        return "ok"
    except Exception as e:
        return "Error: "+str(e)

def processSingleMail(mail):
    pMail = mailparser.parse_from_bytes(mail)
    print("esse foi em")
    return convert_mail_to_dict(pMail)
