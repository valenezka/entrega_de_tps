class Restaurante:
    def __init__(self,nombre,comida):
        self.restaurante_nombre=nombre
        self.tipo_comida=comida

    def describir_restaurante(self):
        print(f"Bienvenido al restaurante {self.restaurante_nombre}")
        print(f"Pueden disfrutar de los diferentes {self.tipo_comida}")
    
    def abrir_restaurante(self):
        print("El restaurante esta abierto")
        
class Heladeria(Restaurante):
    def __init__(self,restaurante_nombre,tipo_comida,sabores):
        super().__init__(restaurante_nombre,tipo_comida)
        self.sabores_helado=sabores

    def mostrar_sabores(self):
        for i in self.sabores_helado:
            print(i)