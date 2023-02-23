import pymongo
from classes import Store, Product, Category, DbMongo
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()
    client.close()

if __name__ =="__main__":
    load_dotenv()
    main()

