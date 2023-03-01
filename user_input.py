# to call each function here!
# to create a Operations Menu
#   ---> e.g. making diff cases and then when the user selects a particular option eg getting user - ask the number?
# Read : how to read input from command line
import pymongo

from basic_operations import add_user_to_db, get_users_from_db, get_user_from_db, update_user_in_db, \
    delete_users_from_db


def print_menu():
    print("============ Menu ============")
    print("1 - Add New User\n"
          "2 - Search User\n"
          "3 - Display All Users\n"
          "4 - Update User\n"
          "5 - Delete User\n"
          "6 - Exit")
    print("==============================")


def menu():
    print_menu()
    user_input = 0
    try:
        while user_input != 6:
            user_input = int(input("Enter a choice and press enter: "))

            """To Add New User(s)"""
            if user_input == 1:
                no_of_users = int(input("Enter number of users to be added : "))
                list_of_users = []
                for user in range(no_of_users):
                    data = {"id": int(input("ID: ")), "name": input("Name: "), "mobile_no": input("Mobile No: "),
                            "city": input("City: ")}
                    list_of_users.append(data)

                user_added = add_user_to_db(list_of_users)
                print('--------------\n' + user_added + '\n--------------')

            """ To Search a User"""
            if user_input == 2:
                user_to_find = int(input("Enter User ID: "))
                print(get_user_from_db(user_to_find))

            """To Retrieve the List of Users"""
            if user_input == 3:
                List_of_users = get_users_from_db()
                for my_dict in List_of_users:
                    for key, value in my_dict.items():
                        print(key, ':', value)
                    print()

            """To Update a User"""
            if user_input == 4:
                User_to_update = int(input("Enter User ID: "))
                User_details = {}
                while User_to_update:
                    key = input("Enter field to be updated: ")
                    value = input("Enter data: ")
                    User_details[key] = value
                    break
                print(update_user_in_db(User_to_update, User_details))

            """ To delete a User """
            if user_input == 5:
                user_to_delete = int(input("Enter User ID: "))
                print(delete_users_from_db(user_to_delete))

            """ To Exit the Application"""
            if user_input == 6:
                print("Exiting!")
                break
    except pymongo.errors.ConnectionFailure:
        print("Connection Error!")
    except pymongo.errors.OperationFailure as e:
        print(f"MongoDB operation failed with error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


menu()
