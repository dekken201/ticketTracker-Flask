import json
import os

def getConfigPath():
	filePath = os.path.abspath(__file__)
	for i in range(2):	
		filePath = os.path.dirname(filePath)
	return filePath


with open(getConfigPath()+"/config.json") as json_file:
    data = json.load(json_file)

IMAP_SERVER = data['imap']['host']
EMAIL_ACCOUNT = data['imap']['user']
EMAIL_FOLDER = data['imap']['box']
PASSWORD = data['imap']['password']
SENDER = data['imap']['senderMailModule']
