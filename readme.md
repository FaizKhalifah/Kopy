# Installation
1. Install python
2. Create a virtual environment with -> python -m venv <environmentname>
3. Activate the virtual environment with .<environmentname>\Scripts\activate
4. Enter pip install flask

# Simple server 
To create a simple server that return a simple text to the browser enter this line of code : 

from flask import Flask

app = Flask(__name__)

@app.route('/') -> the url route

def index():
    return "hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True) -> change host, port and debug here
