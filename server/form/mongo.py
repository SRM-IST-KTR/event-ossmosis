import os
from pymongo import MongoClient
from dotenv import load_dotenv


def database_entry(data):
    try:
        load_dotenv()
        mongo_string = os.getenv('MONGODB_AUTH_URI')
        client = MongoClient(mongo_string)
        database = client[os.getenv('MONGODB_DB')]
        col = database['users']
        col.insert_one(data)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    pass
