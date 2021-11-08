import os

from pymongo import MongoClient


try:
    client = MongoClient(os.environ['MONGO_CONNECTION_STRING'])
except Exception as e:
    raise


def create_report(collection, data):
    db = client.reports
    result = db[collection].insert_one(data)
    return str(result.inserted_id) if result else None


def mailing_list_emails():
    db = client.users
    users = db.users
    docs = users.find(
        filter={'mailing_list': True},
        projection={'_id': False}
    )
    return [doc['email'] for doc in docs]