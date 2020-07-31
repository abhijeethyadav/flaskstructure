from app import app

@app.route("/")
def index():
    return "Hello world branch"

@app.route("/about")
def about():
    return "All about Flask"