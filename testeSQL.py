from sqlitedict import SqliteDict
mydict = SqliteDict('db/teste.sqlite', autocommit=True)
mydict['some_key2'] = "teste"
print(mydict['some_key'])  # prints the new value
for key, value in mydict.iteritems():
    print(key, value)
print(len(mydict)) # etc... all dict functions work
mydict.close()
