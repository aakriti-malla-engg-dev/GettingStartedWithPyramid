import bson
import pymongo
from pymongo import MongoClient
from pprint import pprint

conn = 'mongodb://127.0.0.1:27017/Users'
client = MongoClient(conn)
db = client['Users']
collection_name = db["users"]


def add_user_to_db(users):
    inserted = []
    existing = []
    for user in users:
        if collection_name.find_one({"mobile_no": user['mobile_no']}):
            existing.append(user['mobile_no'])
        else:
            collection_name.insert_one(user)
            inserted.append(user['mobile_no'])
    result = f"Inserted users: {', '.join(inserted)}\nExisting users: {', '.join(existing)}"
    return result


def get_user_from_db(mobile_no):
    user = collection_name.find_one({'mobile_no': mobile_no})
    if user:
        return user
    else:
        print('user not found')


def get_users_from_db():
    users = []
    for doc in collection_name.find():
        users.append(doc)

    return users


def update_user_in_db(mobile_no, updated_details):
    user = collection_name.find_one({'mobile_no': mobile_no})
    if user:
        collection_name.update_one({"mobile_no": mobile_no}, {"$set": updated_details})
        return True
    else:
        return False


def delete_users_from_db(mobile_no):
    deleted = collection_name.delete_one({'mobile_no': mobile_no})
    if deleted.deleted_count == 1:
        return True
    else:
        return False


try:
    # to add users
    users = [
        {'name': "abc", "mobile_no": "6767676767", "city": "Delhi"},
        {'name': "def", "mobile_no": "1234123467", "city": "Delhi"},
        {'name': "ghi", "mobile_no": "9898989898", "city": "Delhi"}
    ]

    # user_added = add_user_to_db(users)
    # print(user_added)

    # to get user
    # print(get_user_from_db('1234567890'))

    # To get users
    # print(get_users_from_db())

    # To update the users
    # print(update_user_in_db("1234123467", {'city': 'Bangalore'}))

    # To delete the user
    # delete_user = delete_users_from_db('9898989898')
    # print(delete_user)

except pymongo.errors.ConnectionFailure:
    print("Connection Error!")
except pymongo.errors.OperationFailure as e:
    print(f"MongoDB operation failed with error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# -------------TO-DO ---------------

# ✅ 1. Add try/catch for internal server error or connection error
# ✅ 2. Return every function with values or True/False
# ✅ 3. Do not add users with the same mobile no (Giving messages if in the list of users added which one was added
# which one was not) using key/value
# ✅ 4. To update the user in a way that the mobile no should be same but the other details should
# change as mentioned
# ✅ 5. check if number exists for deleting the user otherwise dont make the func (delete) call

# 6. build unit test cases
#     - update unit test -> if number not available through exception user not available
#     - delete unit test -> Look for number, if not available through exception
#     - fetch user unit test -> if the user is not available through exception and return something
