numero1 = input("escriba un numero")
numero2 = input("escriba otro numero")

if (numero1 > numero2):
   print(f"{numero1} es mayor que {numero2}")
else:
   if(numero2 > numero1):
      print(f"{numero2} es mayor que {numero1}")
   else:
      print(f"{numero1} es igual a {numero2}")