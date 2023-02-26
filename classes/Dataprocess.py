from classes import data
from classes.DbMongo import DbMongo
from classes.data import DATA
class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self):
        ## Do something to create careers on your mongodb collection using __data
        ##Haga algo para crear carreras en su colección mongodb usando __data
        
        data.DATA.append(data)
          
    
    def create_courses(self):
        ## Do something to create courses on your mongodb collection using __data
        ## Haga algo para crear cursos en su colección mongodb usando __data
        data.DATA.append(data)

    
    def create_students(self):
        ## Do something to create students on your mongodb collection using __data
        ## Haga algo para crear estudiantes en su colección mongodb usando __data
        data.DATA.append(data)
    
    
    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data
        ## Haga algo para crear inscripciones en su colección mongodb usando __data
        data.DATA.append(data)
