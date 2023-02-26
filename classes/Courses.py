from classes.DbMongo import DbMongo

class Courses:
    def __init__(self, cursos_aprobados, cursos_reprobados):
        self.cursos_aprobados = cursos_aprobados
        self.cursos_reprobados=cursos_reprobados

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
        lista_e = Courses.get_list(db)
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
                    'cursos_aprobados': 1
                    , 'cursos_reprobados': 1

                }  
            }
        ])

        for d in result:
            print(d)