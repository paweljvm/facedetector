import face_recognition

class ImageLoader:
    #load image and returns encodings
    def load(self,fileName):
        image = face_recognition.load_image_file(fileName)
        encodings = face_recognition.face_encodings(image)
        return encodings[0]