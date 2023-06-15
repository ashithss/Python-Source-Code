from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>I have deployed given application by using ARGOCD at 3:57</h1>'
