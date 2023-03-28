
#Ejercicio3
""""Parte declarativa"""
# import datetime
# ahora=datetime.datetime.now()
""""Cuerpo principal"""
# print(ahora)

# from datetime import date, time
# dia=date.today()
# print(dia)

#Ejercicio5
# """"Parte declarativa"""
# import random
# def numero_random():
#     return(random.randint(1,8))
# """"Cuerpo principal"""
# inicio=input("Quieres iniciar el juego?: ").lower()
# while inicio=="si":
#     pregunta=input("Por favor ingrese su duda: ")
#     numero=numero_random()
#     if numero==1:
#         print("Es seguro que sí")
#     elif numero==2:
#         print("Las chances son buenas")
#     elif numero==3:
#         print("Puedes contar con ello")
#     elif numero==4:
#         print("Pregúntame de nuevo más tarde")
#     elif numero==5:
#         print("Concéntrate y pregunta de nuevo")
#     elif numero==6:
#         print("No veo con claridad, intenta de nuevo")
#     elif numero==7:
#         print(" Mi respuesta es no")
#     elif numero==8:
#         print("Mis fuentes me dicen que no")

#     inicio=input("Quieres seguir en el juego?: ").lower()

#Ejercicio1
# def redondear(numero):
#     numero2=int(numero)
#     if numero-numero2>=0.5:
#         return numero2+1
#     else:
#         return numero2

# numero=float(input("Por favor ingrese su numero: "))
# print(f"el numero redondeado es {redondear(numero)}")

#Ejercicio2
# import redondeo
# def suma_decimales(num):
#     acumulador=0.0

#     while num!=0:
#         acumulador+=num
#         num=float(input("Por favor ingrese el numero a sumar, 0 para salir= "))

#     print(f"la suma entera es {redondeo.redondeo(acumulador)}")

# numero=float(input("Por favor ingrese el numero a sumar= "))
# suma_decimales(numero)
#Ejercicio4
# Escriba un programa que devuelva un número par al azar entre 2 y 10
# (pista: para comprobar si se pueden generar todos los números, pruebe
# ejecutar el programa dentro de un ciclo infinito)

# import random
# print(random.randint(1,5)*2)

#Ejercicio6
# Encuentre el tiempo de ejecución de los programas de los ejercicios
# anteriores (pista: use el módulo time)
# import time
# ini=time.time()
# import redondeo
# def suma_decimales(num):
#     acumulador=0.0

#     while num!=0:
#         acumulador+=num
#         num=float(input("Por favor ingrese el numero a sumar, 0 para salir= "))

#     print(f"la suma entera es {redondeo.redondeo(acumulador)}")

# numero=float(input("Por favor ingrese el numero a sumar= "))
# suma_decimales(numero)
# fin=time.time()
# dif=fin-ini
# print(f"El tiempo de ejecucion es {dif}")

#Ejercicio7
# Sorteo: Escriba un programa que simule un sorteo donde
# toman uno o más papeles al azar de un pozo para elegir los ganadores
# import random
# papeles=random.randint(1,50)
# print(f"Decidimos sacar {papeles} papeles del pozo")
# numeros_ganadores=[]
# for i in range (papeles+1):
#     ganador=random.randint(1,50)
#     if ganador not in numeros_ganadores:
#         numeros_ganadores.append(ganador)
#     else:
#         while True:
#             ganadornuevo=random.randint(1,50)
#             if ganadornuevo!=ganador and ganadornuevo not in numeros_ganadores:
#                 numeros_ganadores.append(ganadornuevo)
#                 break

# print(f"Los numeros ganadores son: {numeros_ganadores}")

#Ejercicio 8
#  Escriba una función que pida al usuario ingresar su fecha de
# nacimiento y sea capaz de devolver la cantidad de días desde su
# nacimiento hasta hoy
# import datetime

# dia_actual=datetime.date.today()
# fecha_de_nacimiento=input("Por favor ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
# fecha_nacimiento=datetime.datetime.strptime(fecha_de_nacimiento,"%d/%m/%Y").date()
# dias=(dia_actual-fecha_nacimiento).days
# print(dias)
#Ejercicio 9
# Implemente el programa del ejercicio 6 usando un diccionario
# import time
# def Ejercicio1():
#     ini=time.time()
#     def redondear(numero):
#         numero2=int(numero)
#         if numero-numero2>=0.5:
#             return numero2+1
#         else:
#             return numero2

#     numero=float(input("Por favor ingrese su numero: "))
#     print(f"el numero redondeado es {redondear(numero)}")
#     fin=time.time()
#     dif=fin-ini
#     return dif
# def Ejercicio2():
#     ini=time.time()
#     import redondeo
#     def suma_decimales(num):
#         acumulador=0.0

#         while num!=0:
#             acumulador+=num
#             num=float(input("Por favor ingrese el numero a sumar, 0 para salir= "))

#         print(f"la suma entera es {redondeo.redondeo(acumulador)}")

#     numero=float(input("Por favor ingrese el numero a sumar= "))
#     suma_decimales(numero)
#     fin=time.time()
#     dif=fin-ini
#     return dif
# def Ejercicio3():
#     ini=time.time()
    
#     import datetime
#     ahora=datetime.datetime.now()
    
#     print(ahora)
#     fin=time.time()
#     dif=fin-ini
#     return dif
# def Ejercicio4():
#     ini=time.time()
#     import random
#     print(random.randint(1,5)*2)
#     fin=time.time()
#     dif=fin-ini
#     return dif
# def Ejercicio5():
#     ini=time.time()
#     import random
#     def numero_random():
#         return(random.randint(1,8))
    
#     inicio=input("Quieres iniciar el juego?: ").lower()
#     while inicio=="si":
#         pregunta=input("Por favor ingrese su duda: ")
#         numero=numero_random()
#         if numero==1:
#             print("Es seguro que sí")
#         elif numero==2:
#             print("Las chances son buenas")
#         elif numero==3:
#             print("Puedes contar con ello")
#         elif numero==4:
#             print("Pregúntame de nuevo más tarde")
#         elif numero==5:
#             print("Concéntrate y pregunta de nuevo")
#         elif numero==6:
#             print("No veo con claridad, intenta de nuevo")
#         elif numero==7:
#             print(" Mi respuesta es no")
#         elif numero==8:
#             print("Mis fuentes me dicen que no")

#         inicio=input("Quieres seguir en el juego?: ").lower()
#     fin=time.time()
#     dif=fin-ini
#     return dif
# def Ejercicio7():
#     ini=time.time()
#     import random
#     papeles=random.randint(1,50)
#     print(f"Decidimos sacar {papeles} papeles del pozo")
#     numeros_ganadores=[]
#     for i in range (papeles+1):
#         ganador=random.randint(1,50)
#         if ganador not in numeros_ganadores:
#             numeros_ganadores.append(ganador)
#         else:
#             while True:
#                 ganadornuevo=random.randint(1,50)
#                 if ganadornuevo!=ganador and ganadornuevo not in numeros_ganadores:
#                     numeros_ganadores.append(ganadornuevo)
#                     break

#     print(f"Los numeros ganadores son: {numeros_ganadores}")
#     fin=time.time()
#     dif=fin-ini
#     return dif
# def Ejercicio8():
#     ini=time.time()
#     import datetime
#     dia_actual=datetime.date.today()
#     fecha_de_nacimiento=input("Por favor ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
#     fecha_nacimiento=datetime.datetime.strptime(fecha_de_nacimiento,"%d/%m/%Y").date()
#     dias=(dia_actual-fecha_nacimiento).days
#     print(dias)
#     fin=time.time()
#     dif=fin-ini
#     return dif


# dicc_ejer={}
# dicc_ejer["Ejercicio1"]=Ejercicio1()
# dicc_ejer["Ejercicio2"]=Ejercicio2()
# dicc_ejer["Ejercicio3"]=Ejercicio3()
# dicc_ejer["Ejercicio4"]=Ejercicio4()
# dicc_ejer["Ejercicio5"]=Ejercicio5()
# dicc_ejer["Ejercicio7"]=Ejercicio7()
# dicc_ejer["Ejercicio8"]=Ejercicio8()
# print(dicc_ejer)



