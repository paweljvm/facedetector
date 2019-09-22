from init.init import app


@app.route("/detect")
def detecting():
    return "Detecting"