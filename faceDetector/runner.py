from config import config
from init.init import app
import train.train_controller
import detect.detect_controller
@app.route("/")
def index():
    return "Train controller"

app.run(config.host,config.port)