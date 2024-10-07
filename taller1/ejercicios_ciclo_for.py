
#3.1
suma_cubos = 0
for i in range(50):
   suma_cubos += i**3

print(f"la suma de los cubos del 1 al 50 es: {suma_cubos}")


#3.2
for i in range(6):
   for j in range(6-i):
      print(" ", end="")
   for j in range(i):
      print("*", end=" ")
   print("")

#3.3
for y in range(8):
   for x in range(8):
      if (x+y) % 2 == 0:
         print("■", end="")
      else:
         print("□", end="")
   print("")



#3.4 
cadena = input("ingrese la cadena a invertir: ")
for c in range(len(cadena)):
   print(cadena[(len(cadena)-1) - c], end="")
print("")



#3.5
#TODO: preguntar al profesor