from app.models.book import Book
from app import db
from app.utils.custom_exceptions import NotFoundError, BadRequestError

from app.utils.custom_exceptions import NotFoundError

def update_book_by_id(book_id, new_data):
    book = Book.query.get(book_id)
    if not book:
        raise NotFoundError("Book not found")

    if new_data.title:
        book.title = new_data.title
    if new_data.price:
        book.price = new_data.price
    if new_data.rating:
        book.rating = new_data.rating
    if new_data.category:
        book.category = new_data.category
    if new_data.stock is not None:
        book.stock = new_data.stock

    db.session.commit()
    return book


def delete_book_by_id(book_id):
    book = Book.query.get(book_id)
    if not book:
        raise NotFoundError("Book not found")

    db.session.delete(book)
    db.session.commit()
    return book
