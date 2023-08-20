from pymongo import MongoClient

class AnimalShelter(object):
    """CRUD OPERATIONS for Animal Collection in MongoDB"""
    
    def __init__(self, user, password, host, port, db_name):
        self.client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}/{db_name}")
        self.database = self.client[db_name]
        self.collection = self.database["animals"]
        print("Connected to Database")

    def create(self, data):
        try:
            if data:
                insert_result = self.collection.insert_one(data)
                return insert_result.acknowledged
            else:
                raise Exception("Nothing to save, data is empty")
        except Exception as e:
            print("An exception has occurred: ", e)
            return False
            
    def read(self, target):
        try:
            if target:
                read_result = list(self.collection.find(target, {"_id": False}))
                return read_result
            else:
                raise Exception("Nothing to find. Target is empty.")
        except Exception as e:
            print("An exception has occurred: ", e)
            return []  # Return an empty list in case of an exception

    def update(self, fromTarget, toTarget, count):
        try:
            if fromTarget:
                update_result = self.collection.update_many(fromTarget, toTarget)
                print("Success!")
                print(update_result)
                return update_result.modified_count > 0
            else:
                raise Exception("Nothing to update, because at least one of the target parameters is empty")
        except Exception as e:
            print("An exception has occurred: ", e)
            return False

    def deleteData(self, target, count):
        try:
            if target:
                if count == 1:
                    delete_result = self.collection.delete_one(target)
                elif count == 2:
                    delete_result = self.collection.delete_many(target)
                else:
                    print("Count not recognized - try again.")
                    return False
                print("Success!")
                print(delete_result)
                return delete_result.deleted_count > 0
            else:
                raise Exception("Nothing to delete, because the target parameter is empty")
        except Exception as e:
            print("An exception has occurred: ", e)
            return False

# Example usage
user = "kelvin"
password = "matthew"
host = "nv-desktop-services.apporto.com"
port = 32477
db_name = "AAC"

shelter = AnimalShelter(user, password, host, port, db_name)


