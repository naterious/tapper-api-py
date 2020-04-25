from pymongo import MongoClient

# client = MongoClient('mongodb+srv://admin:KwXQ7p0dzQqBpd0A@cluster0-let3b.mongodb.net/test?retryWrites=true&w=majority')
client = MongoClient('mongodb+srv://test:test123@cluster0-4xd31.mongodb.net/test?retryWrites=true&w=majority')
db = client.TriviaTapper
Facts = db.Facts
Users = db.users
Quotes = db.Facts
