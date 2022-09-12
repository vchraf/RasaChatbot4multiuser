from pymongo import MongoClient

def DataUpdate_mongo_par(FirstName,LastName,mail,adress,project,other): 
    CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0.4cjd18h.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    db = client['chatbot']
    coll1 = db['chatbot']
    coll1.insert_one({"firstname":FirstName,
                         "lastname":LastName, 
                         "mail":mail,
                         "adress":adress,
                         "project":project,
                         "other":other,
                         })



def DataUpdate_mongo_por(FirstName,LastName,mail,adress,project,other): 
    CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0.4cjd18h.mongodb.net/test"
    client = MongoClient(CONNECTION_STRING)
    db = client['chatbot']
    coll1 = db['chatbot']
    coll1.insert_one({"firstname":FirstName,
                         "lastname":LastName, 
                         "mail":mail,
                         "adress":adress,
                         })