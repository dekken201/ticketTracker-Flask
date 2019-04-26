from sqlitedict import SqliteDict
import sqlite3

def criaTeste():
    mydict = SqliteDict('db/teste.sqlite',"mails", autocommit=True)
    mydict['1'] = "batata"
    mydict['2'] = "banana"
    mydict['3'] = "oi"
    mydict['4'] = "teste"
    for key, value in mydict.iteritems():
        print(key, value)
    print(len(mydict)) # etc... all dict functions work
    mydict.close()

#GERA UMA QUERY SQL QUE LISTA ORDENANDO POR CHAVES
def testeSelectSQLITE():
    db_filename = 'db/teste.sqlite'
    conn = sqlite3.connect(db_filename)
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    key = c.execute('SELECT key FROM mails').fetchall()
    value = c.execute('SELECT value FROM mails').fetchall()
    print(sorted(key,reverse=True))
    print(sorted(value,reverse=True))

#RETORNA UM DICIONÁRIO ORDENADO DE CIMA PARA BAIXO
def testeSelectSQLDICT():
    mails = SqliteDict('db/teste.sqlite', "mails", autocommit=True)
    for key,value in sorted(mails.iteritems(),reverse=True):
        print(key,value)

def testeFindSQL():
    mails = SqliteDict('db/mails_db.db', "mails", autocommit=True)
    if "20190426113618.6CC61AC073A" in mails:
        print("aqui!")


#criaTeste()
#testeSelectSQLITE()
#testeSelectSQLDICT()
print(testeFindSQL())
