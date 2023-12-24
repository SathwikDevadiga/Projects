This project demonstrates how to perform web scraping using Scrapy, a powerful and extensible web scraping framework in Python. The goal is to gather information from a books website and store the extracted data in MongoDB Atlas.

Prerequisites
-Python 3.x
-Scrapy
-MongoDB Atlas account and connection details

Install dependencies:
pip install -r requirements.txt
Configure MongoDB Atlas:
Replace <YOUR_MONGODB_URI> in mongo.py with your MongoDB Atlas connection URI


Run the Scrapy spider to start scraping:
scrapy crawl books_spider
