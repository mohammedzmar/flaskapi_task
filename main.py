from app import create_app
from app import db
from app.models.book import Book


app = create_app()
with app.app_context():
    print("Total books in DB:", Book.query.count())
if __name__ == '__main__':
    app.run(debug=True)

