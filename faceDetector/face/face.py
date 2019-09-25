from bson.binary import Binary
import pickle
class Face:
    def __init__(self,name,encodings):
        self.id = name
        self.name = name
        #we need to convert that to array handled by mongodb
        self.encodings =  encodings
    def toMongo(self):
        self.encodings = Binary(pickle.dumps(self.encodings, protocol=2), subtype=128 )
        return self
    @staticmethod
    def fromMongo(dict):
        return Face(dict['name'],pickle.loads(dict['encodings']))
        