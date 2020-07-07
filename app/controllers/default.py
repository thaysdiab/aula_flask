from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Hello World!"


@app.route("/test/")
def test():
    return "Oi!"