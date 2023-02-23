from classes.DbMongo import DbMongo 

class Product:
    def __init__(self,id,nombre,unidades):
        self.id = id
        self.nombre = nombre
        self.unidades = unidades
        self.__collection = "Tipo_producto"
