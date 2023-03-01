# to call each function here!
# to create a Operations Menu
#   ---> e.g. making diff cases and then when the user selects a particular option eg getting user - ask the number?
# Read : how to read input from command line

from basic_operations import add_user_to_db, get_users_from_db, get_user_from_db, update_user_in_db, \
    delete_users_from_db


def print_menu():
    print("============ Menu ============")
    print("1 - Add New User\n"
          "2 - Search User\n"
          "3 - Display All Users\n"
          "4 - Update User\n"
          "5 - Delete User")
    print("==============================")


def menu():
    print_menu()
    user_input = 0

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
            print(user_added)

        """ To Search a User"""
        if user_input == 2:
            user_to_find = input("Enter the Number to find User details: ")
            print(get_user_from_db(user_to_find))

        """To Retrieve the List of Users"""
        if user_input == 3:
            List_of_users = str(get_users_from_db()) + '\n'
            print(List_of_users)

        """To Update a User"""
        if user_input == 4:
            User_to_update = input("Enter User's Number to select the user: ")
            User_details = {}
            while User_to_update:
                key = input("Enter field to be updated: ")
                value = input("Enter data: ")
                User_details[key] = value
                break
            print(update_user_in_db(User_to_update, User_details))

        """ To delete a User """
        if user_input == 5:
            user_to_delete = input("Enter the User's Number to delete User Info: ")
            print(delete_users_from_db(user_to_delete))

        """ To Exit the Application"""
        if user_input == 6:
            print("Exiting!")
            break


menu()
