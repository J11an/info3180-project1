from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,IntegerField,DecimalField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField,FileAllowed,FileRequired

class PropertyForm(FlaskForm):

    title = StringField('Property Title',validators=[InputRequired()])
    bedrooms = StringField('Number of Bed Rooms',validators=[InputRequired()])
    bathrooms = StringField('Number of Bath Rooms',validators=[InputRequired()])
    location = StringField('Location',validators=[InputRequired()])
    price = StringField('Price',validators=[InputRequired()])
    type = SelectField('Property Type',choices=[('House','House'),('Apartment','Apartment')],validators=[InputRequired()])
    desc = TextAreaField('Description',validators=[InputRequired()])
    photo = FileField('Photo',validators=[FileRequired(),FileAllowed(['jpg','png'])])