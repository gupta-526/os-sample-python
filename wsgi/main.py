from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Testing Hello World!"

# @application.route("/new_route"):
# def new_route():
# 	return "testing second route"

if __name__ == "__main__":
    application.run()