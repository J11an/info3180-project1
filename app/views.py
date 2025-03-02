"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app,db
from flask import render_template, request, redirect, send_from_directory, url_for, flash
from werkzeug.utils import secure_filename
from app.forms import PropertyForm
from app.models import Property
import os 

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=["GET", "POST"])
def createProperty():    
    form = PropertyForm()

    if request.method == "POST":
        if form.validate_on_submit():

            title = form.title.data
            bedrooms = form.bedrooms.data
            bathrooms = form.bathrooms.data
            location = form.location.data
            price = form.price.data
            type = form.type.data
            desc = form.desc.data
            photo = form.photo.data

            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

            property = Property(title,bedrooms,bathrooms,location,price,type,desc,filename)
            db.session.add(property)
            db.session.commit()
            flash("Property Was Added!", "success")
            return redirect(url_for("viewProperties"))

    return render_template('pform.html', form=form)

@app.route('/properties')
def viewProperties():
    properties = Property.query.all()

    return render_template('propertiesView.html',properties=properties)

@app.route('/property/<property_id>')
def specific_property(property_id):
    property_id = int(property_id)

    my_property = Property.query.filter_by(id=property_id).first()

    return render_template('property.html', property=my_property)

@app.route('/uploads/<filename>')
def get_uploaded_images(filename):
    rootdir = os.getcwd()
    return  send_from_directory(os.path.join(rootdir,app.config['UPLOAD_FOLDER']), filename)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
