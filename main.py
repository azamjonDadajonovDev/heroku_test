from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1><mark><i><b>Hello world</b></i></mark></h1>'

app.run(host='0.0.0.0', port=81)