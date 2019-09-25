from image.image_loader import ImageLoader
from face.face_dao import FaceDao
from face.face import Face
from config import config
from file.move_file import MoveFile
import os
class TrainService:
   
    def __init__(self):
         self.imageLoader = ImageLoader()
         self.faceDao = FaceDao()
         self.moveFile = MoveFile()  
    def train(self,fileName):
        name = fileName.split(".")[0]
        encodings = self.imageLoader.load(os.path.join(config.toTrainPath,fileName))
        self.faceDao.save(Face(name,encodings).toMongo())
        self.moveFile.move(fileName,config.toTrainPath,config.trainedPath)
    
    def trainFromDirectory(self,directory):
        pass
