from classes.DbMongo import DbMongo

class Students:
    def __init__(self, numero_cuenta, nombre_completo,edad):
        self.numero_cuenta = numero_cuenta
        self.nombre_completo =nombre_completo 
        self.edad =edad 
        
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id


    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )

    @staticmethod
    def delete_all(db):
        lista_e = Students.get_list(db)
        for e in lista_e:
            e.delete(db)


    @staticmethod
    def print_full_report_short_path(db):
        collection = db["estudiante"]

        result = collection.aggregate([
            {
                '$lookup': {
                    'from': "estudiante"
                    , 'localField': "estudiante"
                    , "foreignField": "_id"
                    , "as": "te"
                }
            },{
                '$project': {
                    'nombre': 1
                    , 'telefono': 1
                    , 'edad': 1

                    ## , "tipo": Tipoestudiante.get_one(db, e["tipo_estudiante"] ).tipo

                }  
            }
        ])

        for d in result:
            print(d)





    