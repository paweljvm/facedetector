from config import config
from init.init import app
import train.train_controller
import detect.detect_controller
import uploader.upload_controller
@app.route("/")
def index():
    return "<b>FACE DETECTOR</b>"

app.run(config.host,config.port)