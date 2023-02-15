# import json
# from pprint import pprint
# import bson
# from pymongo import MongoClient
# from pyramid.config import Configurator
# from pyramid.view import view_config
#
# conn = 'mongodb://127.0.0.1:27017/Users'
# client = MongoClient(conn)
# db_name = client['Users']
# collection_name = db_name["users"]
#
#
# @view_config(route_name='users', request_method='GET', renderer='json')
# def get_all_users():
#     users = list(collection_name.find({}))
#     return users
#     # for doc in collection_name.find():
#     #     return str(doc)
#
#
#
#
#
