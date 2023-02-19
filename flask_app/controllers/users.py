from flask_app import app
from flask import render_template, redirect

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return redirect('/')