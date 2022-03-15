from . import db

class Property(db.Model):

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100))
    bedrooms = db.Column(db.String(10))
    bathrooms = db.Column(db.String(10))
    location = db.Column(db.String(100))
    price = db.Column(db.String(50))
    type = db.Column(db.String(20))
    desc = db.Column(db.String(1500))
    photo = db.Column(db.String(100))

    def __init__(self, title, bedrooms, bathrooms, location, price, type, desc, photo):
        
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location   
        self.price = price
        self.type = type
        self.desc = desc
        self.photo = photo


    def __repr__(self):
            return '<Property %r>' % (self.title)

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support