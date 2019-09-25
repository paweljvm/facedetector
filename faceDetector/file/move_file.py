import os

class MoveFile:
    def move(self,fileName,oldDestination,newDestination):
        os.rename(os.path.join(oldDestination,fileName),os.path.join(newDestination,fileName))