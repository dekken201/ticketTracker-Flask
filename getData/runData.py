from getData.functions import *
from getEmails.functions import *
from getEmails.config import *

mails = start(IMAP_SERVER,EMAIL_ACCOUNT,PASSWORD,EMAIL_FOLDER,SENDER)
print
makeObject(mails)