from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    if not User.validate(request.form):
        return redirect('/')
    form_data = {
        'first_name': request.form['first_name'], 
        'last_name': request.form['last_name'], 
        'email': request.form['email'], 
        'password': request.form['password'], 
    }
    User.save_registration(form_data)
    return redirect('/')