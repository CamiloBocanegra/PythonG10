filas = int(input("ingrese el numero de filas del triangulo de pascal: "))

for i in range(filas):
   #imprimir espacios
   for j in range(filas - i - 1):
      print(" ", end="")
   
   #calcular y mostrar coeficientes
   coeficiente = 1

   for j in range(i+1):
      print(coeficiente, end=" ") # imprimir coeficiente
      #Formula del coeficiente binomial
      # doble slash // para division entera
      coeficiente = coeficiente * (i - j) // (j + 1) 

   #salto de linea despues de cada fila
   print()