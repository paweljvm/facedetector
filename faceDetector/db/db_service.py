import pymongo
from config import config
class DbService:
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://{}:{}".format(config.mongoHost,config.mongoPort))
        self.db = self.myclient[config.mongoDbName]
    def collectionPointer(self,name):
        return self.db[name]