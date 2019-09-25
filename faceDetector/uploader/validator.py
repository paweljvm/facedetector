from config import config
class Validator:
    def validate(self,fileName):
        if fileName and fileName.strip():
            index = fileName.fileName.rfind(".")
            extension =fileName[index+1:len(fileName)]).lower
            return extension in config.allowedExtensions
        return False

