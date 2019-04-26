print("Importando arquivos necessários...")
import getData.functions as getData
import getEmails.functions as getEmails
from getEmails.config import *

def updateDB():
	print("Iniciando processo...")
	try:
		mails = getEmails.start(IMAP_SERVER, EMAIL_ACCOUNT, PASSWORD, EMAIL_FOLDER, SENDER)
		getData.makeObject(mails)
	except Exception as e:
		print("Erro ao executar mineração automática: "+str(e))

if __name__ == "__main__":
	updateDB()

