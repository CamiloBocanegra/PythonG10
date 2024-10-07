
numero = int(input("introduzca que tabla quieres ver: "))
num_max = int(input("introduzca hasta que numero quieres ver la tabla: "))
for i in range(num_max+1):
   resultado = numero*i
   print(f"{numero} x {i} = {resultado}")