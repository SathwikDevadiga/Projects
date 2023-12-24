from pymongo import MongoClient
client = MongoClient("<YOUR_MONGODB_URI>")
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
