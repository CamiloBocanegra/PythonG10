
while True:
      
   palabra = input("ingrese una palabra: ")

   letra_inicial = input("ingrese la letra inicial: ")

   if palabra[:3].lower() == letra_inicial.lower():
      print(f"la palabra {palabra} comienza con la letra {letra_inicial} ingresada")
   else:
      print(f"la palabra {palabra} NO comienza con la letra {letra_inicial} ingresada")
