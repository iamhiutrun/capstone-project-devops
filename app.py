from flask import Flask
 
app = Flask(__name__)
 
@app.route("/", methods=["GET"])
def helloWorld():
    return 'Hello World, my name is Cuong'
 
app.run(host="0.0.0.0", port=80, debug=True) 
