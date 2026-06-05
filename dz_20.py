import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

from config import MONGO_USERNAME, MONGO_PASSWORD


uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.qdihgbf.mongodb.net/?appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

# databases = client.list_databases()
# print(databases)
# for db in databases:
#     print(db)

db_book = client.book
collection_books = db_book['books']

book = {'title': 'Гра престолів', "price": 450, "year": 1996, "pages": 694}
collection_books.insert_one(book)

books = [
    {'title': 'Математика', "grade": 5, "pages": 320},
    {'title': 'Українська мова', "grade": 4, "pages": 288},
    {'title': 'Історія України', "grade": 8, "pages": 256},
    {'title': 'Географія', "grade": 6, "pages": 240},
    {'title': 'Біологія', "grade": 9, "pages": 272},
]
collection_books.insert_many(books)


query = {'grade': {"$gte": 5, "$lte": 8}}

all_books = collection_books.find(query)


query = {"year": 2022}

all_books = collection_books.find(query).sort("grade", -1).limit(3)


most_pages_books = collection_books.find().sort("pages", -1).limit(1)

for book in most_pages_books:
    print(book)







