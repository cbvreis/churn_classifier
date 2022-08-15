##Connect to mongoDB
from pymongo import MongoClient


class MongoDAO:
    def __init__(self, user, password, host, port):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.client = None
        self.db = None
        self._collection = None
        self.connect()

    def connect(self):
        client = MongoClient(self.host, self.port, username=self.user, password=self.password)
        self.client = client

    def set_db(self, db_name):
        self.db = self.client[db_name]

    def set_collection(self, collection_name):
        self._collection = self.db[collection_name]

    def get_collection(self):
        return self._collection
