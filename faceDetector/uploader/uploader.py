from config import config
from uploader.validator import Validator
from werkzeug.utils import secure_filename
import os
class Uploader:
    def __init__(self):
        self.validator = Validator()
    def upload(self,file,fileName):
        if self.validator.validate(fileName):
            fileName = secure_filename(file.fileName)
            file.save(os.path.join(config.toTrainPath, fileName))
