from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price = Column(String, nullable=False)
    rating = Column(Integer)
    category = Column(String)

engine = create_engine('sqlite:///books.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
