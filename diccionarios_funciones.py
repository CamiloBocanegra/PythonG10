import os
os.system("cls")

def diccionario_lista_de_valores(diccionario):
   return list(diccionario.values())
def diccionario_lista_de_tuplas(diccionario):
   return list(diccionario.items())

mi_diccionario = {
   "nombre": "milo",
   "email": "wawa@gmail.com",
   "edad":"null",
   "pesa":"69"
}

print(diccionario_lista_de_valores(mi_diccionario))
print(diccionario_lista_de_tuplas(mi_diccionario))
