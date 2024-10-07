import math
import random
import os

os.system("cls")

#ejercicio 1: funciones
# escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el indice de masa corporal
#IMC


def calcular_imc(peso, estatura):
   imc = peso / (estatura ** 2)
   return imc

def calcular_categoria_imc(imc):
   if imc < 18.5:
      return "bajo peso"
   elif imc < 25:
      return "peso normal"
   elif imc < 30:
      return "sobrepeso"
   elif imc < 35:
      return "obesidad tipo 1"
   elif imc < 40:
      return "obesidad tipo 2"
   else:
      return "obesidad tipo 3"
   

# imc = calcular_imc(85, 1.70)
# print(imc)
# print(calcular_categoria_imc(imc))

#calcular el area de un circulo y el volumen de un cilindro

def calcular_area_circulo(radio):
   return math.pi * (radio ** 2)

def calcular_volumen_cilindro(radio, altura):
   return calcular_area_circulo(radio)*altura

# radio = float(input("ingrese el radio del circulo: "))
# altura = float(input("ingrese la altura del cillindro: "))
# print(f"el volumen del cilindro es {calcular_volumen_cilindro(radio, altura):.3f} ")


#ejercicio 3: funciones
#escribir una funcion que reciba una muestra de numeros en una lista y devuelva su media
def media(lista):
   return sum(lista) / len(lista)

mi_lista = [1, 2, 3, 4, 5]

# print(f"Los elementos de la lista son: {mi_lista}")
# print(f"La suma de los elementos es: {sum(mi_lista)}")
# print(f"La cantidad de elementos es: {len(mi_lista)}")
# print(f"La media de la lista es: {media(mi_lista)}")


#ejercicio 4: funciones
#escribir una funcion que reciba una muestra de numeros en una lista y devuelve otra lista con sus cuadrados
# 1, 4, 9, 16, 25

def cuadrados(lista):
   return [i ** 2 for i in lista]

# lista = [1,2,3,4,5]
# print(f"los cuadrados de los elementos de la lista son: {cuadrados(lista)}")

#ejercicio 5: funciones
#escribir una funcion que muestre los numeros que piden por teclado, que muestre la suma de los pares y la suma de los impares.
# y cuente cuantos numeros hay en la lista

def analizarNumeros():
   numeros = [] #declaro mi lista vacia
   while True:
      entrada = input("ingrese un numero (o presione \"Enter\" para terminar el programa): ")
      if entrada == "":
         break
      else:
         numeros.append(int(entrada))
   
   pares = [num for num in numeros if num % 2 == 0]
   impares = [num for num in numeros if num % 2 == 0]

   print(f"La lista de numeros es: {numeros}")
   print(f"Pares: {pares}")
   print(f"La suma de los pares es: {sum(pares)}")
   print(f"Impares: {impares}")
   print(f"La suma de los impares es: {sum(impares)}")
   print(f"La cantidad de numeros es: {len(numeros)}")

# analizarNumeros()

#ejercicio 6: funciones
#Escribir una funcion que use todos los metodos de la lista, usando la funcion range para generar los numeros de la lista

def metodos_lista():
   lista = [random.randint(1,100) for _ in range(10)]
   print(f"lista original: {lista}")

   lista_desordenada = lista.copy()
   random.shuffle(lista_desordenada)
   print(f"lista desordenada: {lista_desordenada}")

   #agregar un elemento a la lista
   lista.append(11)
   print(f"valor agregado: {lista}")

   #concatenar listas
   lista2 = [12, 13, 14]
   lista.extend(lista2)
   print(f"lista2 es: {lista2}")
   print(f"listas concatenadas: {lista}")

   #insert posicion + valor
   lista.insert(5, 69)
   print(f"insertar 69 en posicion 5: {lista}")

   #eliminar un valor
   lista.remove(69)
   print(f"remove 69: {lista}")

   #pop
   eliminado = lista.pop(0)
   print(f"valor eliminado: {eliminado}")
   print(f"pop primer elemento: {lista}")

   #count
   print(f"La lista tiene {lista.count(12)} veces el valor 12")

   print(f"El valor 13 esta en la posicion {lista.index(13)}")

   #reverse
   lista.reverse()
   print(f"Reversa: {lista}")

   #Ordenar
   lista.sort()
   print(f"Ordenada: {lista}")

   #copy
   lista_copia = lista
   print(f"lista copiada: {lista_copia}")

   #clear
   lista_copia.clear()
   print(f"lista limpiada: {lista_copia}")


# metodos_lista()