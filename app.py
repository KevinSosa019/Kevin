import pymongo
from classes import DATA, Dataprocess
from classes import Careers, DbMongo,Courses,Students,Enrollments
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()

    pipeline = Dataprocess(DATA)
    
    pipeline.create_careers()
    pipeline.create_students()
    pipeline.create_enrollments()


    client.close()

if __name__ == "__main__":
    main()