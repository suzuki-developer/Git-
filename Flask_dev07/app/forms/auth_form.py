from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email

class LoginForm(Form):
    email    = TextField('Email Adress', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Password', [Required(message='Must provide a password.')])
