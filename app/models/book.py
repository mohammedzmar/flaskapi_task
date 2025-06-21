from app import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    price = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Integer)
    category = db.Column(db.String(100))
