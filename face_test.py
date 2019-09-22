import face_recognition
import os
def main():
    knowns = load_knowns()
    classify(knowns)
  #  pitEncoding =load_encoding('pit1.jpg')
   # shouldBeTrue = load_encoding('pit2.jpg')
   # shouldBeFalse = load_encoding('tracz.jpg')
   # results = face_recognition.compare_faces([pitEncoding],shouldBeTrue)
   # print(results)
   # print(face_recognition.compare_faces([pitEncoding],shouldBeFalse))
def classify(knowns):
    knownsEncoding = list(knowns.values())
    knowsNames = list(knowns.keys())
    for r, d, f in os.walk("./unknown"):
        for file in f:
            find_name(knownsEncoding,knowsNames,"./unknown/{}".format(file))
def find_name(knowsEncodings,knownsNames,path):
    encoding = load_encoding(path)
    result = face_recognition.compare_faces(knowsEncodings,encoding)
    if True in result:
        index =  result.index(True)
        print('Found {} is {}'.format(path , knownsNames[index]))
    else:
        print('Face {} not found'.format(path))

def load_knowns():
    knowns = {}
    for r, d, f in os.walk("./known"):
       for file in f:
           knowns[file.split(".")[0]]=load_encoding("./known/{}".format(file))
    return knowns
       

def load_encoding(name):
    image = face_recognition.load_image_file(name)
    encodings = face_recognition.face_encodings(image)
    return encodings[0]

main()