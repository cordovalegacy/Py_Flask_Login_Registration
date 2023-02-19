from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods = ['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    form_data = {
        'first_name': request.form['first_name'], 
        'last_name': request.form['last_name'], 
        'email': request.form['email'], 
        'password': bcrypt.generate_password_hash(request.form['password']) 
    }
    id = User.save_registration(form_data)
    session['user_id'] = id
    return redirect('/user_page')

@app.route('/user_page')
def user_page():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('user_page.html', user = User.get_one_user(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')