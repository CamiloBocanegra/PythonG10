pares = 0
impares = 0

numero = int(input("introduzca un numero: "))
while numero >= 0:
   if(numero%2 == 0):
      pares += 1
   else:
      impares += 1
   numero = int(input("introduzca un numero: "))

print(f"La cantidad de numeros pares es: {pares}")
print(f"La cantidad de numeros impares es: {impares}")