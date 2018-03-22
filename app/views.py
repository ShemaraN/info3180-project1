"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from datetime import date
from app import app, db, forms, models
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from forms import UserForm
from sqlalchemy.sql import exists
from models import UserProfile
from werkzeug import SharedDataMiddleware
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')
    
    
@app.route('/profile', methods=['POST', 'GET'])
def profile():
    form = UserForm()
    if request.method == 'POST' and form.validate_on_submit():
        first_name = form.firstname.data
        last_name  = form.lastname.data
        email     = form.email.data
        location  = form.location.data
        gender    = form.gender.data
        biography = form.biography.data
        photo     = form.photo.data
        filenames = secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filenames))
        photo=photo.filename
        #data_created = form.date_created.data
        
        user= UserProfile(first_name = first_name,
        last_name = last_name, email= email, location = location,
        gender=gender, biography=biography, photo =photo)
        
        db.session.add(user)
        db.session.commit()
        return redirect (url_for('profiles'))
    else:
        flash('This', 'danger')
        return render_template('profile.html', form=form)
        
    return render_template('profile.html', form= form)
        
@app.route('/profiles')
def profiles():
    users = UserProfile.query.all()
    print(users)
    return render_template('profiles.html', users = users)
    
@app.route('/profile/<userid>')
def profile_userid(userid= None):
    if (userid):
        user =UserProfile.query.filter_by(id=userid).first()
        photo= get_uploaded_images()
        return render_template('profile.html',user=user, photo=photo)
        
def get_uploaded_images():
    rootdir= os.getcwd()
    print rootdir
    ls =[]
    for subdir, dirs, files in os.walk(rootdir + 'app/static/uploads'):
        for file in files:
            ls.append(os.path.join(subdir,  file).split('/')[-1])
    return ls
            
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
