import math

msg = "Hello World"
print(msg)
# El programa ha de demanar la introducció d’una variable A 
# (ha de demanar-ho per pantalla) i també una variable B, que l’usuari ha d’introduir. 
A = input("Introdueix el valor A:")
B = input("Introdueix el valor B:")
print(f"El valor de A es: {A} i B es: {B}")

#A continuació es mostraran per pantalla els valors capturats indicant a quina variable
#  pertanyen, s’intercanviaran  els valors de les variables i es tornaran a 
# mostrar per pantalla.
C = A 
A = B
B = C
print(f"Ek valor de A es: {A} i B es: {B}")

#Programa que demani un nombre sencer i en mostri l'últim dígit.
try:
    num = int(input("Introdueix el numero sencer :"))
    txt = str(num)
    print(f"ultim digit: {txt[-1]}")
except:
    print("no es un numero l'introduit")

# Escriu un programa que en el que l’usuari introdueix els valors dels catets 
# d’un triangle, rectangle, i en calculi quina és la hipotenusa, l’àrea i el 
# perímetre del mateix mitjançant les següents expressions:
# Hipotenusa: c=r2(a2+b2)
#pow (x, y) == x:numero entero y: exponencial
print(f"")
print("calcula la hipotenusa")
numX = int(input("Introdueix un num: "))
numY = int(input("Introdueix un num: "))
C = math.sqrt(pow(numX, 2)+pow(numY, 2))

print(f"la hipotenusa es:{C}")

# Area: c=ba/2
print(f"")
print("calcula el area")
numX = int(input("Introdueix un num: "))
numY = int(input("Introdueix un num: "))
C = numX * numY / 2

print(f"el area es:{C}")


# Perímetre: p=a+b+c

print("calcula el perimetro")
numX = int(input("Introdueix un num: "))
numY = int(input("Introdueix un num: "))
numZ = int(input("Introdueix un num: "))
C = numX + numY + numZ

print(f"el perimetro es:{C}")




