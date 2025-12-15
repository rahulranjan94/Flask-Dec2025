from flask import Flask
app = Flask(__name__) #_name_ ->"hello.py"

@app.route("/") # endpoint. When user visits "/" , this function is automatically called.
def hello_world():
    return "Hello, there.!"

@app.route("/ping", methods = ["GET",["POST"]]) # only respond to GET and POST request
def ping():
    return {"message": "Why are you pinging me?"}

if _name_ == "__main__":
    app.run(debug=True) #debug = True -> auto reload server on code changes