import sys
import os

import getEmails.functions as getEmails
argv1 = (sys.argv[1])

print(argv1)
print(type(argv1))

filePath = os.path.abspath(__file__)
for i in range(2):
    filePath = os.path.dirname(filePath)


retorno = getEmails.dump_json("teste", argv1)
if retorno == "ok":
    print("Mensagens salvas com sucesso")
else:
    print(retorno)


