# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# scraped data -> item containers -> json/csv/xml
# scraped data -> item containers -> pipelines -> SQL/mongo database


'''
to use pipeline you first have to activate it 
Goto settings.py find ITEM_PIPELINES and uncomment it, and pipeline is activated
'''


 #store in sqlite3
'''import sqlite3
class Project1Pipeline:
    def __init__(self) -> None:
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        # self.curr = sqlite3.Cursor()
        self.curr = self.conn.cursor()

    def create_table(self):
        self.conn.execute(""" DROP TABLE IF EXISTS quotes_tb""")
        self.conn.execute("""
                create table quotes_tb(
                            quote text,
                            author text,
                            tags text
                )
        """)

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values(?,?,?)""", (
            item['quote'][0],
            item['author'][0],
            item['tags'][0]
        ))
        self.conn.commit()

#to store it in a database create a file named database.py
'''


# store in mongodb
import pymongo

class Project1Pipeline:
    def __init__(self) -> None:
        self.conn = pymongo.MongoClient('localhost', 27017) # creates a connection
        db = self.conn['myquotes'] #database name
        self.collection = db['quotes'] # collection name

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item)) # adds item to the database
        return item

