from getEmails.config import *
from getEmails.functions import *

def run():
	start(IMAP_SERVER,EMAIL_ACCOUNT,PASSWORD,EMAIL_FOLDER,SENDER)

if __name__ == "__main__":
	run()