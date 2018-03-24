from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/data/user/<string:id>")
def listUser(id):
	return "list user" + id	
