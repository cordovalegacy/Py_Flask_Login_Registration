from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM login_registration WHERE id=%(id)s"
        result = connectToMySQL('log_reg').query_db(query, data)
        return cls(result[0])

    @classmethod
    def save_registration(cls, form_data):
        query = """
                INSERT INTO login_registration (first_name, last_name, email, password, created_at, updated_at)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW())
                ;"""
        return connectToMySQL('log_reg').query_db(query, form_data)
    
    @staticmethod
    def validate(form_data):
        is_valid = True
        if len(form_data['first_name']) < 2:
            flash("First Name must be at least 2 characters")
            is_valid = False
        if len(form_data['last_name']) < 2:
            flash("Last Name must be at least 2 characters")
            is_valid = False
        if len(form_data['email']) < 12:
            flash("Email Address must be at least 12 characters")
            is_valid = False
        if len(form_data['password']) < 2:
            flash("Password must be at least 2 characters")
            is_valid = False


