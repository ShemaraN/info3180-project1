from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name  = StringField('Last Name', validators=[InputRequired()])
    email     = StringField('Email', validators=[InputRequired()])
    location  = StringField('Location', validators=[InputRequired()])
    gender    = SelectField('Gender', choices=[('1','FEMALE'), ('2','MALE')])
    biography = TextAreaField('Biography', validators=[InputRequired(),Length(max=255)])
    photo = FileField('Profile Picture',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])
    

    
    
    
    
    
    
    

    

