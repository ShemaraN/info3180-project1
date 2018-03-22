from . import db
from time import time 
from datetime import date 


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(255))
    location = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    biography = db.Column(db.String(255))
    photo = db.Column(db.String(80))
    #date_created = db.Column(db.String(30))
    
    def __init__(self, first_name,last_name,email,location,
    gender,biography,photo):
        self.id           = UserProfile.get_new_id()
        self.first_name   = first_name
        self.last_name    = last_name
        self.email        = email
        self.location     = location
        self.gender       = gender
        self.biography    = biography
        self.photo        = photo
        self.date_created = timeinfo()

    

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

def get_new_id(self):
    try:
        return unicode(self.id)
    except NameError:
        return str(self.id) 
        
def timeinfo():
    d = date.today();
    return "{0:%A}, {0:%B} {0:%d}, {0:%y}".format(d)
	   