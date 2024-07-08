from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO, WORLD'

app.run(host='0.0.0.0', port=5000, debug=False)
