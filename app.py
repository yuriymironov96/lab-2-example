import os

from flask import Flask, request
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
    var = os.environ.get('MY_TEST', 'fallback')
    return f"<p>Today is {date.today().strftime('%d/%m/%Y')}</p><p>env var: {var}</p>"
