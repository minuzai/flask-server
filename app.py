from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO, WORLD'

app.run(port=5000)