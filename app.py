from flask import Flask

app = Flask("meu app")

@app.route('/')
def hello():
    return "Hello Mundo !!"

@app.route('/novo')
def novo():
    return "Hello Mundo novo !!"    

