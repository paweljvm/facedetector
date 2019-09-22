from init.init import app


@app.route("/train")
def train():
    return "Train"
