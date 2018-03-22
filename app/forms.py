from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UserForm(FlaskForm):
    first_name = StringField('Firstname', validators=[InputRequired()])
    last_name  = StringField('Lastname', validators=[InputRequired()])
    email     = StringField('Email', validators=[InputRequired()])
    location  = StringField('Location', validators=[InputRequired()])
    gender    = SelectField('Gender', choices=[('1','FEMALE'), ('2','MALE')])
    biography = TextAreaField('Biography', validators=[InputRequired(),])
    photo = FileField('Profile Picture',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])

    
    
    
    
    
    
    

    

