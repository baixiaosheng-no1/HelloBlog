

from App.exts import db




class Admin(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20))
    userpwd = db.Column(db.String(20))

    
    
class Category(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    catename = db.Column(db.String(100),unique=True)
    as_name = db.Column(db.String(20),unique=True)
    key_word=db.Column(db.String(100))
    descri = db.Column(db.String(200))
    arts = db.relationship('ArtMoel',backref='my_category',lazy=True)


class ArtMoel(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    content = db.Column(db.Text)
    keywords = db.Column(db.String(100))
    describe = db.Column(db.String(100))
    tags = db.Column(db.String(100))
    date = db.Column(db.Date)
    category = db.Column(db.Integer, db.ForeignKey(Category.id))
    

    
    