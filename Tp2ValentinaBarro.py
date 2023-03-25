#Ejercicio N1
# 1) Pida un número al usuario y determine si es par o impar. 

# Numero=int(input("Por favor escriba un numero entero: "))

# if Numero%2==0:
#     print(f"el Numero {Numero} es par")
# else :
#     print(f"El Numero {Numero} es impar")
#Ejercicio N2
#2) Escriba una cadena if-elif-else que determine el estado de vida de una persona. 

# Edad=int(input("Por favor ingrese su edad: "))
# if Edad<2:
#     print("Es un bebé")
# elif Edad<4 and Edad >=2 :
#     print("Es un infante")
# elif Edad<12 and Edad>=4 :
#     print("Es un niño")
# elif Edad>=12 and Edad <20 :
#     print("Es un adolecente")
# elif Edad>=20 and Edad<65 :
#     print("Es un adulto")
# else :
#     print("Es un anciano")

# #Ejercicio N3

# # 3) Cree un ciclo que nunca termine y ejecútelo. Puede probarlo haciendo que muestre algo en
# # pantalla por cada pasada del ciclo. Para finalizarlo, presione Ctrl-C o el comando para detener
# # la ejecución correspondiente a su editor
# c=0
# while True:
#     c+=1 
#     print(c)

# #Ejercicio N4

# # scriba un programa que contenga dos ciclos while anidados que muestre los enteros del 1
# # al 100, diez números por línea, como se muestra abajo:

# c1=0
# c2=0
# while c2<100:
#     c2+=10
#     while c1<c2:
#         c1+=1
#         print(c1,end=" ")
#     print("\n")

# #Ejercicio N5 
# # 5) Resuelva el ejercicio anterior usando solo un ciclo while
# c1=0
# c2=10
# while c1<100:
#     c1+=1
#     print(c1,end=" ")
#     if c1==c2 :
#         c2+=10
#         print("\n")


