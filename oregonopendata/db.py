import json, os, pymysql
from pprint import pprint
from sqlalchemy import create_engine

class DatabaseManager:

    def __init__(self, db='yamhill'):
        self.db = db

        curdir = os.path.abspath(os.path.dirname(__file__))
        conf_path = os.path.join(curdir, '..', 'config', 'db.json')

        with open(conf_path, 'r') as fp:
            self.conf = json.loads(fp.read())

    def connect(self):
        return pymysql.connect(host=self.conf['host'], user=self.conf['username'], password=self.conf['password'], db=self.db)

    def create_engine(self):
        p = {
            'host': self.conf['host'],
            'user': self.conf['username'],
            'pass': self.conf['password'],
            'db':   self.db
        }
        return create_engine("mysql+pymysql://{user}:{pass}@{host}:3306/{db}".format(**p))

