import bson
from pymongo import MongoClient
from pprint import pprint

conn = 'mongodb://127.0.0.1:27017/Users'
client = MongoClient(conn)
db = client['Users']
collection_name = db["users"]


def add_user_to_db(users):
    collection_name.insert_many(users)
    print("New User(s) inserted!")


users = [
    # {'name': "abc", "mobile_no": "6767676767", "city": "Delhi"},
    # {'name': "def", "mobile_no": "1234123467", "city": "Delhi"},
    {'name': "ghi", "mobile_no": "9898989898", "city": "Delhi"}
]


# add_user_to_db(users)


def get_user_from_db(mobile_no):
    print(f"user details for : {mobile_no}")
    pprint(collection_name.find_one({'mobile_no': mobile_no}))


# get_user_from_db('1234567890')


def get_users_from_db():
    print("Users are: ")
    for doc in collection_name.find():
        print(str(doc))


# get_users_from_db()


def update_user_in_db(mobile_no, updated_details):
    collection_name.update_one({"mobile_no": mobile_no}, {"$set": updated_details})
    print("User detail after update :")
    pprint(collection_name.find_one({'mobile_no': mobile_no}))


# update_user_in_db("2468013579", {'city': 'Bangalore'})


def delete_users_from_db(mobile_no):
    if db.collection_name.find({'mobile_no': {"$in": mobile_no}}):
        collection_name.delete_one({'mobile_no': mobile_no})
    else:
        return False


print()
delete_users_from_db('765766345435')

# Return every function with values or True/False

# 1. do not add users with the same mobile no
# 2. to update the user in a way that the mobile no should be same but the other details should change as mentioned
# 3. check if number exists for deleting the user otherwise dont make the func (delete) call

# 4. build unit test cases
#     - update unit test -> if number not available through exception user not available
#     - delete unit test -> Look for number, if not available through exception
#     - fetch user unit test -> if the user is not available through exception and return something
