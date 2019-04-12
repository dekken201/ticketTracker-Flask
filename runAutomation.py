print("Importando arquivos necessários...")
import sys
import getData.functions as getData
import getEmails.functions as getEmails
from getEmails.config import * #MUDA EM GETEMAILS/CONFIG

#FAZ O BACKUP PARA /OUTPUT (DO DIA)
def getJSON():
	print("Iniciando processo...")
	try:
		getEmails.start(IMAP_SERVER,EMAIL_ACCOUNT,PASSWORD,EMAIL_FOLDER,SENDER)
		getData.makeObject(getData.open_json())
	except Exception as e:
		print("Erro ao executar mineração automática: "+str(e))

	print("Backup finalizado com sucesso!")

#PARA USO DO SITE
def processObject(mail):
	print("Iniciando processo...")
	try:
		mail = getEmails.processSingleMail(mail)
		print("Email processado.")
		return getData.makeObject(mail)
	except Exception as e:
		print("Erro ao executar mineração do email: "+str(e))

print(__name__)
if __name__ == "__main__":
	argv1 = (sys.argv[1])
	processObject(argv1)
