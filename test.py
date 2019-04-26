from sqlitedict import SqliteDict
def testeSelectSQLDICT():
    mails = SqliteDict('db/mails_db.db', "mails", autocommit=True)
    for key,value in sorted(mails.iteritems(),reverse=True):
        print(key,value)

def testeFindSQL():
    mails = SqliteDict('db/mails_db.db', "mails", autocommit=True)
    if "20190426113618.6CC61AC073A" in mails:
        print("aqui!")

print(testeFindSQL())
#print(testeSelectSQLDICT())