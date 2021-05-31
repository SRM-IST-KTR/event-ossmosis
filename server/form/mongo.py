import os
from pymongo import MongoClient
from dotenv import load_dotenv

def database_entry(data):
    load_dotenv()
    mongo_string = os.getenv('MONGODB_AUTH_URI')
    client = MongoClient(mongo_string)
    database = client['test']
    col=database['test']
    col.insert_one(data)


if __name__ == "__main__":
	pass
