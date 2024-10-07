import os
os.system("cls")

# 1.1
letra = input("introduzca una letra: ").upper()
if('A' <= letra) and (letra <= 'L'):
   print("la letra es de las primeras")
elif('L' < letra and letra <= 'Z'):
   print("la letra es de las ultimas")
else:
   print("no es una letra valida")

#1.2
angulo_grados = int(input("introduzca un angulo(en grados): "))
angulo_grados = angulo_grados %360
if(angulo_grados < 90):
   print("el angulo dado se encuentra en el primer cuadrante")
elif(angulo_grados < 180):
   print("el angulo dado se encuentra en el segundo cuadrante")
elif(angulo_grados < 270):
   print("el angulo dado se encuentra en el tercer cuadrante")
else:
   print("el angulo dado se encuentra en el cuarto cuadrante")


#1.3
nota = float(input("introduzca la nota del estudiante: "))
if(nota > 4.5):
   print("Rendimiento: Exelente")
elif(nota > 3.5):
   print("Rendimiento: Bueno")
elif(nota > 3):
   print("Rendimiento: Regular")
elif(nota > 0):
   print("Rendimiento: Insuficiente")
else:
   print("Nota invalida")


#1.4
temperatura = float(input("Introduzca la temperatura (En grados centigrados): "))
if(temperatura > 35):
   print("el clima es calido")
elif(temperatura > 20):
   print("el clima es templado")
else:
   print("el clima es frio")


#1.5
jengibre = input("Introduzca la palabra Jengibre: ")
if(jengibre == "Jengibre"):
   print("Si, ¡El Jengibre es la mejor planta de todos los tiempos!")
elif(jengibre == "jengibre"):
   print("No, ¡quiero un gran Jengibre!")
else:
   print("! Jengibre¡ No")