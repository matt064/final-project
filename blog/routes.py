from flask import render_template
from blog import app


@app.route("/")
def homepage():
    return render_template('base.html')

