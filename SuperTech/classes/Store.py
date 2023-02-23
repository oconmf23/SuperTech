from classes.DbMongo import DbMongo 

class Store:
    def __init__(self, nombre,id =""):
        self.__id = id
        self.nombre = nombre
    

   #""" def save(self,db):
    #    collection = db[self.__collection]
     #   result = collection.insert_one(self.__dict__)
      #  self.__id = result.inserted_id
        #client.close()

    #def update(self,db):
     #   collection = db[self.__collection]

      #  result = collection.insert_one(self.__dict__)
       # self.__id = result.inserted_id
        #client.close()

  #  """
