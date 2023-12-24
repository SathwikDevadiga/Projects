from pymongo import MongoClient
client = MongoClient("mongodb+srv://devadigasathwik81544:test1234@cluster0.82k5wbu.mongodb.net/")
db = client.scrapy
posts = db.test_collection

import datetime
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}
post_id = posts.insert_one(post).inserted_id