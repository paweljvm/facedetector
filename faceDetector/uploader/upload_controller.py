from uploader.uploader import Uploader
from init.init import app
from flask import  request
uploader = Uploader()

@app.route("/upload/<fileName>",methods = ["POST"])
def upload(fileName):
    file = request.files['file']
    uploader.upload(file,fileName)
