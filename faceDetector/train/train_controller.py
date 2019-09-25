from init.init import app
from train.train_service import TrainService
from response.response import Response,OK
trainService = TrainService()

@app.route("/train/<fileName>")
def train(fileName):
    print("Training for {}".format(fileName))
    trainService.train(fileName)
    return str(OK)
