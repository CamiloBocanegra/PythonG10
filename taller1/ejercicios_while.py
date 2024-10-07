import random

#2.1
numero_actual = 20
while numero_actual > 0:
   print(numero_actual, end=" ")
   numero_actual -= 1
print("")

#2.2
numero_actual = 0
while numero_actual <= 50:
   print(numero_actual, end=" ")
   numero_actual += 2
print("")


#2.3
cadena = input("Ingrese una frase: ")
vocales = "aeiouAEIOU"

vocales_count = 0
c = 0
while c in range(len(cadena)):
   if(cadena[c] in vocales):
      vocales_count += 1
   c += 1
print(f"La cantidad de vocales es: {vocales_count}")

#2.4
dado = 0
while dado != 6:
   dado = random.randint(1,6)
   print(f"se lanzo el dado y dio: {dado}")


#2.5
numero_ingresado = input("Ingrese un numero: ")
suma_digitos = 0
c = 0
while c in range(len(numero_ingresado)):
   digito_actual = int(numero_ingresado[c])
   suma_digitos += digito_actual
   c += 1

print(f"la suma de los digitos es: {suma_digitos}")