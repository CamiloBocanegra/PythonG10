import random

while(True):
   print("*************************************************************")
   print("1. Decir en que cuadrante se encuentra un angulo")
   print("2. Tirar dado hasta que salga 6")
   print("3. Invertir una cadena de caracteres")
   print("4. Decir si un numero es par o no")
   print("0. Salir")
   seleccion = int(input("Introduzca una opcion: "))

   if(seleccion == 0):
      break
   elif(seleccion == 1):
      angulo_grados = int(input("introduzca un angulo(en grados): "))
      angulo_grados = angulo_grados %360
      if(angulo_grados < 90):
         print("el angulo dado se encuentra en el primer cuadrante")
      elif(angulo_grados < 180):
         print("el angulo dado se encuentra en el segundo cuadrante")
      elif(angulo_grados < 270):
         print("el angulo dado se encuentra en el tercer cuadrante")
      else:
         print("el angulo dado se encuentra en el cuarto cuadrante")

   elif(seleccion == 2):
      dado = 0
      while dado != 6:
         dado = random.randint(1,6)
         print(f"se lanzo el dado y dio: {dado}")
      
   elif(seleccion == 3):
      cadena = input("ingrese la cadena a invertir: ")
      for c in range(len(cadena)):
         print(cadena[(len(cadena)-1) - c], end="")
      print("")
   elif(seleccion == 4):
      numero = int(input("introduzca un numero para saber si es par: "))
      lambda_es_par = lambda num : (num%2)==0
      if(lambda_es_par(numero)):
         print(f"el numero {numero} es par")
      else:
         print(f"el numero {numero} no es par")
      