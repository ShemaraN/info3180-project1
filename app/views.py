"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import datetime
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, send_from_directory
from models import UserProfile
from sqlalchemy.sql import exists
from forms import UserForm
from werkzeug import SharedDataMiddleware
from werkzeug.utils import secure_filename



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')
    
@app.route('/profile', methods=['POST','GET'])
def profile():
    form = UserForm()
    now = datetime.datetime.now()
    
    if request.method =='POST' and form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        location = form.location.data
        gender = form.gender.data
        biography=form.biography.data
        photo=form.photo.data
        date_created=now.strftime("%B %d, %Y")
        filename= secure_filename(photo.filename)
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        photo=photo.filename
        
        user = UserProfile.query.filter_by(first_name=first_name).first()
        if user is None :
            user = UserProfile(first_name = first_name, last_name = last_name, email = email, location = location, gender = gender, biography = biography, photo = filename, date_created=date_created)
            db.session.add(user)
            db.session.commit()
            flash('Profile was successfully added.', 'success')
            return redirect(url_for('profiles'))
        else:
            flash("already a member", 'danger')

    flash_errors(form)
    return render_template('profile.html',form=form)
    
@app.route('/profiles')
def profiles():
    Users = UserProfile.query.order_by(UserProfile.first_name).all()
    print(Users)
    return render_template('profiles.html', users = Users)
    
@app.route('/profiles/<userid>')  
def displayprofiles(userid):
    print(userid,1)
    User =UserProfile.query.filter_by(id=userid).first()
    return render_template('user.html',user=User)

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

###
# The functions below should be applicable to all Flask apps.
###

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
