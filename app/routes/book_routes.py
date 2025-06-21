from flask import Blueprint, request
from app.models.book import Book
from app.schemas.book_schema import book_schema, books_schema
from app import db
from app.utils.response_wrapper import success_response
from app.utils.custom_exceptions import NotFoundError
from app.services.book_service import update_book_by_id 
from app.utils.custom_exceptions import BadRequestError 
book_bp = Blueprint("books", __name__)

@book_bp.route("/")
def home():
    return {
        "message": "Welcome to the Book API"
    }

@book_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return success_response("Books retrieved", books_schema.dump(books))

@book_bp.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    book = Book(**data)
    db.session.add(book)
    db.session.commit()
    return success_response("Book added", book_schema.dump(book), 201)

@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        raise NotFoundError("Book not found")
    return success_response("Book found", book_schema.dump(book))

@book_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    try:
        json_data = request.get_json()
        if not json_data:
            raise BadRequestError("No input data provided")

        data = book_schema.load(json_data, session=db.session, partial=True)
        updated_book = update_book_by_id(book_id, data)
        return success_response("Book updated", book_schema.dump(updated_book))
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500

@book_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        raise NotFoundError("Book not found")
    db.session.delete(book)
    db.session.commit()
    return success_response("Book deleted")
