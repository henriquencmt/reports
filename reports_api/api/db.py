import os

from bson.objectid import ObjectId
from pymongo import MongoClient


try:
    client = MongoClient(os.environ['MONGO_CONNECTION_STRING'])
except Exception as e:
    raise


def read_all_reports(collection):
    db = client.reports
    docs = db[collection].find()
    docs = list(docs)
    for doc in docs:
        doc['_id'] = str(doc['_id'])
    return docs


def read_report(collection, id):
    try:
        obj_id = ObjectId(id)
    except:
        return None
        
    db = client.reports
    doc = db[collection].find_one(obj_id)
    if doc:
        doc['_id'] = str(doc['_id'])
    return doc
