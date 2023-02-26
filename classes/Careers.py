from classes.DbMongo import DbMongo
class Careers:
    def __init__(self, carrera):
        self.carrera = carrera

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
        lista_e = Careers.get_list(db)
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
                    'carrera': 1
                  
                }  
            }
        ])

        for d in result:
            print(d)

    
    

