inicial = int(input("ingrese el inicio del conteo: "))
limite = int(input("ingrese el limite del conteo: "))

while inicial <= limite:
   print(f"{inicial}", end="-")
   inicial += 1
