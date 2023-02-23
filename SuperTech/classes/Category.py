from classes.DbMongo import DbMongo 

class Category:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
        self.__collection = "categorias"
