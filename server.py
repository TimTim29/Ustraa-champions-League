from flask import Flask, request, jsonify, render_template
import datetime as dt
from services.generateGroup import generateGroup
from random import randrange

app = Flask(__name__)

@app.route('/')
def home():
    data = generateGroup()
    return render_template('home.html.j2', data = data)

if __name__ == '__main__':
    app.run(host="localhost", debug=True)

