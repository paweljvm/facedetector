from db.db_service import DbService

class FaceDao:
    def __init__(self):
        self.facesRepo = DbService().collectionPointer("faces")
    def findByName(self,name):
        query = {"name":name}
        return self.facesRepo.find(query)
    def save(self,face):
        print("Saving face {}".format(face))
        self.facesRepo.insert_one(vars(face))
    