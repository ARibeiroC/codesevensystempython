import os
from pymongo import errors, MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()
def collection():
    MONGO_URI = f"mongodb+srv://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASS')}@codesevenacademyerp.ovupv.mongodb.net/?retryWrites=true&w=majority&appName=codesevenacademyerp"
    client=MongoClient(MONGO_URI, serverSelectionTimeoutMS=os.getenv('MONGO_TIMEOUT'))
    database = client['codeseven']
    return database['codesevencfi']

def conn():
    try:
        for register in collection.find():
            print(register)
    except errors.ServerSelectionTimeoutError as errorTimeout:
        print(f'the time was exceeded: {errorTimeout}')
    except errors.ConnectionFailure as errorConnection:
        client.close()
        print('Failure in connection with mongodb')



def includeRegister():
    data = {
        "registerCandidate": "001234",
        "nameComplete": "Anderson F R Campos",
        "emailCandidate": "andersonspl@email.com",
        "telephoneCandidate": "11999998888",
        "nameResponsible": "",
        "cellphoneResponsible": "",
        "passwordCandidate": "123",
    }
    collection().insert_one(data)

def findRegisterAll():
    for register in collection().find():
        print(register)


findRegisterAll()