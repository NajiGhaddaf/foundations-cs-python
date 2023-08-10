graph = {}
def menu ():
    # we print menu and ask user to enter his choice
    choice = input(
        "1. Add a user to the platform.\n"
        "2. Remove a user from the platform.\n"
        "3. Send a friend request to another user.\n"
        "4. Remove a friend from your list.\n"
        "5. View your list of friends.\n"
        "6. View the list of users on the platform.\n"
        "7. Exit\n"
        "- - - - - - - - - - - - - - -\n"
        "Enter a choice:"
    )
    if choice == str(1):
        add_user()
    elif choice == str(2):
        remove_user()
    elif choice == str(3):
        add_friend()
    elif choice == str(4):
        remove_friend()
    elif choice == str(5):
        view_friends()
    elif choice == str(6):
        view_users()
    elif choice == str(7):
        exit()
    else:
        print("invalid choice!")
        menu()

def add_user():
    # we ask user to enter username with letters only
    user = input("please enter username to add:")
    while user in graph:
        user = input("user already exists! please enter a new one: ")
    while not user.isalpha():
        user = input("numbers/special characters are not allowed! please enter another user: ")
    graph[user]=[]
    menu()

def remove_user():
    # we check for username if exists and remove it from the graph , and neighbors accordingly
    user_to_remove = input("please enter the user to remove: ")
    while user_to_remove not in graph:
        user_to_remove = input("user not found! please enter a different user: ")
    del graph[user_to_remove]
    for neighbors in graph.values():
        if user_to_remove in neighbors:
            neighbors.remove(user_to_remove)
    menu()

def add_friend():
    # we ask user to enter both usernames and append both users to the graph vertices
    user1 = input("please enter first user")
    while user1 not in graph:
        user1 = input("user not found! please enter an existing user: ")
    user2 = input("please enter user to add: ")
    while user2 not in graph:
        user2 = input("user not found! please enter an existing user: ")
    graph[user1].append(user2)
    graph[user2].append(user1)
    print(graph)
    menu()
def remove_friend():
    # we check if user is valid and we remove it from both sides of the vertex
    user1 = input("please enter first user: ")
    while user1 not in graph:
        user1 = input("user not found! please enter an existing user: ")
    user2 = input("please enter user to remove: ")
    while user2 not in graph:
        user2 = input("user not found! please enter an existing user: ")
    graph[user1].remove(user2)
    graph[user2].remove(user1)
    print(graph)
    menu()

def view_friends():
    # we print the neighbors vertices of the user
    user = input("please enter username: ")
    while user not in graph:
        user = input("invalid user! please enter an existing user: ")
    #for neighbors in graph.values():
    print(graph[user])
    menu()
def view_users():
    # we print all users available in the graph
    print("Registered users are: ")
    for users in graph.keys():
        print(users)
    menu()


menu()
