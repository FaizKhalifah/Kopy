from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello<h1>", 200

@app.route('/name', methods=['GET'])
def name():
    return "my name is faiz"

#dynamic route
@app.route('/greet/<name>')
def greet(name):
    return f"halo {name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)