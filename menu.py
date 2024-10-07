import os

os.system("cls")


def sumar_lista_de_numeros(lista):
   sumatoria = 0
   for num in lista:
      sumatoria += num
   return sumatoria

def crear_lista_de_numeros():
   numeros = []
   while True:
      entrada = input("Ingrese numero (o deje vacio para terminar): ")
      if entrada == '':
         break
      else:
         try:
            numeros.append(int(entrada))
         except ValueError:
            print("Error: No es un numero valido")
   return numeros

def menu():
   print("\n ----Menu----")
   print("1. Suma los numeros de una lista")
   print("2. Cuenta las vocales y consonantes")
   print("3. imprima una matriz n*n y llenar sus diagonales")
   # print("4. Suma los numeros de una lista")
   # print("5. Suma los numeros de una lista")
   # print("6. Suma los numeros de una lista")
   # print("7. Suma los numeros de una lista")
   print("0. para salir")



while True:
   menu()
   opcion = int(input("Ingrese una opcion: "))

   if opcion == 1:
      lista_de_numeros = crear_lista_de_numeros()
      resultado_suma = sumar_lista_de_numeros(lista_de_numeros)
      print(f"El resultado de la suma es: {resultado_suma}")
   elif opcion == 2:
      frase = input("Ingrese una frase: ")
      vocales = "aeiouAEIOU"

      vocales_count = 0
      consonantes_count = 0
      especiales_count = 0
      for character in frase:
         if(character in vocales):
            vocales_count += 1
         elif character.isalpha():
            consonantes_count += 1
         else:
            especiales_count += 1

      print(f"La cantidad de vocales es: {vocales_count}")
      print(f"La cantidad de consonantes es: {consonantes_count}")
      print(f"La cantidad de caracteres especiales es: {especiales_count}")
   if opcion == 3:
      n = int(input("Ingrese el tamaño de la matriz: "))
      
   if opcion == 0:
      print("bai bai")
      break