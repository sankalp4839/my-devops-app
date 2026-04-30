# a) basic flask app -> b) containerize it ->c) automate the build (using git) ->d) deploy to cloud (AWS EC2)
#change for jenkins
from flask import Flask
app =Flask(__name__)

@app.route('/')
def home():
    return "<h1>Devops Successfull!</h1><p> Pythin + Docker + Git + AWS running.</p>"

if __name__== "__main__":
    app.run(host='0.0.0.0',port=5000)
