from flask import render_template
from core import app

@app.route('/')
def index():
    greeting = "hellow you found your way"
    return render_template('index.html', greet=greeting)
