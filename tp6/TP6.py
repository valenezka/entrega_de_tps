# Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
# del rectángulo.
# class Rectangulo: 
#     def __init__(self,Base,Altura):
#         self.base=Base
#         self.altura=Altura 

#     def area(self):

#         return self.base*self.altura
    

# b=float(input("Por favor ingrese la base del rectangulo: "))
# h=float(input("Por davor ingrese la altura del rectangulo: "))
# rectangulo=Rectangulo(b,h)
# print(f"El area del rectangulo es {rectangulo.area()}")

# Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina.
#  La clase debe contener
# como miembros:
# o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
# o Un atributo para el estado (lleno o vacío).
# o Un atributo n, que indica la cantidad máxima de cebadas.
# o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
# excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
# o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
# debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
# o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
# de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
# “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.
# class Mate:
#     def __init__(self,N):
#         self.cebadasrest=N
#         self.estado=False
#         self.n=N
    
#     def cebar(self): 
#         if self.estado==True:
#             print("Cuidado, te quemaste!")
#         elif self.cebadasrest>0:
#             self.cebadasrest-=1
#             self.estado=True

#     def beber(self):
#         if self.estado==False:
#             print("El mate esta vacio")
#         else: 
#             if self.cebadasrest==0:
#                 self.estado=False
#                 print("El mate está lavado")
#             else:
#                 self.estado=False

# mate1=Mate(2)
# mate1.cebar()
# mate1.cebar()
# mate1.beber()
# mate1.cebar()
# mate1.beber()
# mate1.beber()

# Botella y Sacacorchos
#  Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
#  Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho
# que la tapa, o None si está destapada.
#  Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella,
# le saque el corcho y se guarde
# una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella 
#ya esté destapada, o si el
# sacacorchos ya contiene un corcho.
#  Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción 
#en el caso en el que no haya un corcho.
# class corcho:
#     def __init__ (self,bodega):
#         self.Bodega= bodega
# class Botella: 
#         def __init__(self,corcho=None):
#              self.corcho_botella=corcho
# class Sacacorcho:
#     def __init__(self):
#          self.corcho_sacado=None
#     def destapar(self,botella:Botella):
#         if botella.corcho_botella==None:
#               print("La botella no tiene corcho")
#         else:
#             if self.corcho_sacado!=None:
#                 print("El sacacorcho tiene un corcho, debes limpiarlo")
#             else:
#                 self.corcho_sacado=botella.corcho_botella
#                 botella.corcho_botella=None
#     def limpiar(self):
#         if self.corcho_sacado==None:
#               print("No hay un corcho en el sacacorcho")
#         else:
#              self.corcho_sacado=None
#              print("Sacacorcho limpio")
                       
# corcho1=corcho("Pampa")
# botella1=Botella(corcho1)
# sacarcorcho=Sacacorcho()
# sacarcorcho.destapar(botella1)
# print(botella1.corcho_botella)
# sacarcorcho.limpiar()
# sacarcorcho.limpiar()

# Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
# restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
# método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
# Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
# sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
# al método.
# class Restaurante:
#     def __init__(self,nombre,comida):
#         self.restaurante_nombre=nombre
#         self.tipo_comida=comida

#     def describir_restaurante(self):
#         print(f"Bienvenido al restaurante {self.restaurante_nombre}")
#         print(f"Pueden disfrutar de los diferentes {self.tipo_comida}")
    
#     def abrir_restaurante(self):
#         print("El restaurante esta abierto")

# class Heladeria(Restaurante):
#     def __init__(self,restaurante_nombre,tipo_comida,sabores):
#         super().__init__(restaurante_nombre,tipo_comida)
#         self.sabores_helado=sabores

#     def mostrar_sabores(self):
#         for i in self.sabores_helado:
#             print(i)


# sabor=["chocolate","Vainilla","Frutilla","Crema del cielo","Crema americana","Coockies and Cream"]
# heladeria1=Heladeria("Mi heladeria","Helados de crema",sabor)
# heladeria1.describir_restaurante()
# heladeria1.abrir_restaurante()
# heladeria1.mostrar_sabores()

# Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
# reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
# que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
#  Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
# personaje, al que le debe hacer el daño indicado por el atributo ataque.
#  Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
# devuelva la cantidad cosechada
# class Personaje:
#     def __init__(self,vida,posicion,velocidad):
#         self.vida_personaje=vida
#         self.posicion_personaje=posicion
#         self.velocidad=velocidad

#     def recibir_ataque(self,ataque):
#         self.vida_personaje-=ataque
#         if self.vida_personaje<=0:
#             print("Ya dejalo, ya esta muerto")
#         else:
#             print("Recibiste un ataque")

#     def mover(self,direccion):
#         if direccion==True:
#             self.posicion_personaje+=self.velocidad
#         else:
#             self.posicion_personaje-=self.velocidad

# class Soldado(Personaje):
#     def __init__(self,vida,posicion,velocidad,ataque):
#         super().__init__(vida,posicion,velocidad)
#         self.ataque_soldado=ataque
    
#     def atacar(self,persona:Personaje):
#         persona.recibir_ataque(self.ataque_soldado)

# class Campesino(Personaje):
#     def __init__(self,vida,posicion,velocidad,cosecha):
#         super().__init__(vida,posicion,velocidad)
#         self.cosecha_camp=cosecha

#     def cosechar(self):
#         print(f"cosechaste {self.cosecha_camp}")


# soldado1=Soldado(10,0,5,2)
# persona1=Personaje(4,0,2)
# campesino1=Campesino(15,4,2,8)
# print(persona1.vida_personaje)
# soldado1.atacar(persona1)
# print(persona1.vida_personaje)
# soldado1.atacar(campesino1)
# print(campesino1.vida_personaje)
# campesino1.cosechar()

# Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
# se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
# usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
# Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno
class Usuario:
    def __init__(self,nombre,apellido,edad):
        self.nombre_usuario=nombre
        self.apellido_usuario=apellido
        self.edad_usuario=edad

    def describir_usuario(self):
        print(f"Nombre= {self.nombre_usuario}\nApellido= {self.apellido_usuario}\nedad= {self.edad_usuario}")

    def saludar_usuario(self):
        print(f"Hola {self.nombre_usuario}, Esperamos que tengas un dia lleno de exitos")
              

# usuario1=Usuario("Sofia","Rodriguez",20)
# usuario2=Usuario("Miguel","Portell",25)
# usuario3=Usuario("Harvey","Specter",40)
# usuario4=Usuario("Levi","Ackerman",30)

# usuario1.describir_usuario()
# usuario1.saludar_usuario()
# usuario2.describir_usuario()
# usuario2.saludar_usuario()
# usuario3.describir_usuario()
# usuario3.saludar_usuario()
# usuario4.describir_usuario()
# usuario4.saludar_usuario()
             
# Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
# Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
# postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
# muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

# class Admin(Usuario):
#     def __init__(self,Nombre,apellido,edad,privilegios):
#         super().__init__(Nombre,apellido,edad)
#         self.privilegios_admin=privilegios
    
#     def mostrar_privilegios(self):
#         for i in self.privilegios_admin:
#             print(i)

# privilegios=["Puede postear en el foro","Puede borrar un post","Puede banear un usuario"]
# admin1=Admin("Roberto","Argenti",45,privilegios)
# admin1.describir_usuario()
# admin1.saludar_usuario()
# admin1.mostrar_privilegios()

# Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
# con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
# clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
# el método para mostrar privilegios.

# class Privilegios:
#     def __init__(self,privilegios):
#         self.privilegio=privilegios

#     def mostrar_privilegios(self):
#         for i in self.privilegio:
#             print(i)

# class Admin(Usuario):
#     def __init__(self,Nombre,apellido,edad,privilegios):
#         super().__init__(Nombre,apellido,edad)
#         self.privilegios_admin=privilegios
    
#     def mostrar_privilegios(self,privilegio:Privilegios):
#         privilegio.mostrar_privilegios()


# lista=["Publicar en el foro","Permiso para borrar post","Banear personas"]
# privilegio1=Privilegios(lista)
# admin11=Admin("Armando","Casas",45,privilegio1)
# admin11.mostrar_privilegios(privilegio1)

# Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
# al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
# funcionó.
# from Restaurante import Restaurante

# restaurante2=Restaurante("El Arabe","Arabe")
# restaurante2.describir_restaurante()
# restaurante2.abrir_restaurante()

# (Opcional): Repita el ejercicio anterior pero esta vez importando la clase Heladeria. 
# ¿Qué se necesita para que funcione la importación?
# from Restaurante import Heladeria

# sabores2=["Coockies and Cream","Mascarpone","Chocolate"]
# heladeria2=Heladeria("Oso Polar","Helados",sabores2)
# heladeria2.abrir_restaurante()
# heladeria2.describir_restaurante()
# heladeria2.mostrar_sabores()



