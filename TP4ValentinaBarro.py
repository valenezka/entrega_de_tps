# #Ejercicio1
# def numeros_primos(numero):
#     for i in range(1,numero+1):
#         contador=0
#         for j in range (1,i+1):
#             if i%j==0:
#                 contador+=1
#         if contador==2:
#             print(f"El numero {i} es primo")

# numero=int(input("Por favor ingrese hasta donde quiere ver los numeros primos: "))
# numeros_primos(numero)

# #Ejercicio2
# def condimento_sandwich(condimentos):
#     condimento=input("Por favor ingrese un condimento: ")
#     while condimento!="salir":
#         condimentos.append(condimento)
#         print(f"Ya se agrego el condimento {condimento} al sandwich")
#         condimento=input("Por favor ingrese el siguiente codimento: ")

#     return condimentos
    
# condimentos=[]
# condimento_sandwich(condimentos)
# print(f"los condimentos agregados a tu sandwich son {condimentos}")

#Ejercicio3A
# def hacer_remera(talle,mensaje):
#     print(f"La remera es talle {talle} y su mensaje es {mensaje}")



# T=input("Por favor ingrese el tamaño que desea su remera: ")
# M=input("Por favor ingrese el mensaje que desea imprimir en la remera: ")
# hacer_remera(T,M)
# hacer_remera(mensaje=M,talle=T)
#Ejercicio3B
# def hacer_remera(talle="L",mensaje="Me gusta Phyton"):
#     print(f"La remera es talle {talle} y su mensaje es {mensaje}")
    



# T=input("Por favor ingrese el tamaño que desea su remera: ")
# M=input("Por favor ingrese el mensaje que desea imprimir en la remera: ")
# hacer_remera()
# hacer_remera(T,M)
# hacer_remera(T)
#Ejercicio4
# def fibonacci(lista,numero):
    
#     for i in range (numero-2):
#         lista.append(lista[i]+lista[i+1])

#     return lista

# lista=[0,1]
# numero=int(input("Por favor ingrese cuantos numeros quiere ver de la serie fibonacci: "))
# print(fibonacci(lista,numero))
#Ejercicio5

# def suma(x,y):
#     return x+y
# def resta(x,y):
#     return x-y
# def multiplicacion(x,y):
#     return x*y
# def division(x,y):
#     return x/y
# def potenciacion(x,y):
#     return x**y
# def division_entera(x,y):
#     return x//y

# x=int(input("Por favor ingrese el primer numero: "))
# y=int(input("Por favor ingrese el segundo numero: "))
# operacion=int(input("Que operacion desea realizar,1.Suma-2.Resta-3.Mult-4.Div-5.Pot-6.DivEnt= "))
# while operacion!=0:
#     if operacion==1:
#         print(suma(x,y))
#     elif operacion==2:
#         print(resta(x,y))
#     elif operacion==3:
#         print(multiplicacion(x,y))
#     elif operacion==4:
#         print(division(x,y))
#     elif operacion==5:
#         print(potenciacion(x,y))
#     elif operacion==6:
#         print(division_entera(x,y))
#     operacion=int(input("Que operacion desea realizar,1.Suma-2.Resta-3.Mult-4.Div-5.Pot-6.DivEnt, 0 para terminar = "))
#     if operacion!=0:
#         x=int(input("Por favor ingrese el primer numero: "))
#         y=int(input("Por favor ingrese el segundo numero: "))
#Ejercicio6
# pueda convertir
# gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la
# conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462
# libras = 1 gramo 
# def conv_gramos_libra(gr):
#     return gr*0.00220462
# def conv_libra_gramo(lib):
#     return lib/0.00220462
# def conv_centim_pulgada(cent):
#     return cent*0.393701
# def conv_pulgada_centim(pulgada):
#     return pulgada/0.393701
# def conv_kilometro_milla(km):
#     return km/1.60934
# def conv_milla_km(mill):
#     return mill*1.60934
# operacion=int(input("Ingrese operación a realizar:\n1-.Gramos-->Libras\n2-.Libras-->Gramos\n3-.Cm-->Pulgada\n4-.Pulgada-->Cm\n5-.Km-->Millas\n6-.Millas-->Km: "))
# while operacion!=0:
#     if operacion==1:
#         gramos=int(input("Por favor ingrese los gramos a convertir: "))
#         print(f"{gramos} es igual a {conv_gramos_libra(gramos)} libras")
#     elif operacion==2:
#         Libras=int(input("Por favor ingrese las Libras a convertir: "))
#         print(f"{Libras} es igual a {conv_libra_gramo(Libras)} gramos")
#     elif operacion==3:
#         centimetro=int(input("Por favor ingrese los centimetros a convertir: "))
#         print(f"{centimetro} es igual a {conv_centim_pulgada(centimetro)} pulgada")
#     elif operacion==4:
#         pulgada=int(input("Por favor ingrese las pulgadas a convertir: "))
#         print(f"{pulgada} es igual a {conv_pulgada_centim(pulgada)} centimetro")
#     elif operacion==5:
#         kilometro=int(input("Por favor ingrese los kilometros a convertir: "))
#         print(f"{kilometro} es igual a {conv_kilometro_milla(kilometro)} milla")
#     elif operacion==6:
#         milla=int(input("Por favor ingrese las millas a convertir: "))
#         print(f"{milla} es igual a {conv_milla_km(milla)} km")

#     operacion=int(input("Ingrese operación a realizar:\n1-.Gramos-->Libras\n2-.Libras-->Gramos\n3-.Cm-->Pulgada\n4-.Pulgada-->Cm\n5-.Km-->Millas\n6-.Millas-->Km, 0 para terminar: "))

        


#Ejercicio7
# def año_bisiesto(año):
#     if año%4==0:
#         if año%100==0 and año%400==0:
#             return True 
#         elif año%100!=0:
#             return True
#     else: 
#         return False

# año=int(input("Por favor ingrese el año a evaluar: "))
# if año_bisiesto(año) == True: 
#     print(f"El año {año} es un año bisiesto")
# else:
#     print(f"El año {año} no es bisiesto")
#B
# def año_bisiesto(año):
#         if año%4==0:
#             if año%100==0 and año%400==0:
#                 return True 
#             elif año%100!=0:
#                 return True
#         else: 
#             return False

# año=int(input("Por favor ingrese el año a evaluar que sea posterior al actual: "))

# for i in range (año,2023+1):
#     if año_bisiesto(i) == True: 
#         print(f"El año {i} es un año bisiesto")
#     else:
#         print(f"El año {i} no es bisiesto")
#Ejercicio 8
# 8) (Opcional) Si listamos todos los números naturales menores a 10 que son múltiplos de 3 o 5,
# obtenemos 3,5,6 y 9. La suma de estos múltiplos es 23. Encuentre la suma de todos los
# múltiplos de 3 o 5 menores a 1000.

# def multiplos():
#     contador=0
#     for i in range (1000+1):
#         if i%3==0 or i%5==0:
#             contador+=i
#     return contador
            
# print(f"La suma de los multiplos menores a 1000 es {multiplos()}")

        
