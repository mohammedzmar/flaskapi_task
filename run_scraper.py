from scraper import scrape_books
from database import Book, Session

books = scrape_books()
session = Session()

for book_data in books:
    book = Book(**book_data)
    session.add(book)

session.commit()
session.close()
print(f"Inserted {len(books)} books into books.db")
