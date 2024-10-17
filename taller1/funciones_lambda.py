#4.1
lambda_suma = lambda a, b : a+b
print(lambda_suma(6, 4))

#4.2
lambda_es_par = lambda num : (num%2)==0
print(lambda_es_par(6))

#4.3 Dada una lista de tuplas, usa una función lambda para ordenarlas según el segundo elemento de cada tupla.

lista_de_tuplas = [(9,5), (1,7), (10, 3), (156, 1), (4, 15)]
lista_ordenada_de_tuplas = sorted(lista_de_tuplas, key=lambda x: x[1])
print(lista_ordenada_de_tuplas)

#4.4
numeros= [1,515, 13, 4,3,2,5, 20, 52, 11, 10]

lista_mayores_que_10 = list(filter(lambda x: x>10, numeros))
print(lista_mayores_que_10)


#4.5
lista_cuadrados = list(map(lambda x: x*x, numeros))
print(lista_cuadrados)

def a_function():
   print("awaawawawwa")
