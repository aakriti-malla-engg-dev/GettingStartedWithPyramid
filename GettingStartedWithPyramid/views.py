from pymongo import MongoClient
from pyramid.response import Response
from pyramid.view import view_config

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["Users"]
collection_name = db["users"]


@view_config(route_name='users', request_method='GET', renderer='json')
def get_all_users(request):
    users = list(collection_name.find({}))
    return users



