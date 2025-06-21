# flaskapi_task
# BookStore Flask API
This is a simple RESTful API built with Flask to scrape book data from a website and manage it using a SQLite database. It demonstrates web scraping, database integration, and REST API development.

---

## Features

- **Web Scraping:** scrapes book information like title, price, rating, and category from [Books to Scrape](https://books.toscrape.com).
- **SQLite Database:** Stores scraped book data efficiently using SQLAlchemy ORM.
- **RESTful API:** Provides endpoints to list, get, create, update, and delete books.
- **Data Validation:** Uses Marshmallow to serialize and validate data.

