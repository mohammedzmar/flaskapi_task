from app import ma
from app.models.book import Book
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True  
        include_fk = True     

book_schema = BookSchema()
books_schema = BookSchema(many=True)
