from datetime import datetime, timedelta
today = datetime.now()
formatted_today = today.strftime("%Y%m%d")
# date time retrieved from google link: https://www.programiz.com/python-programming/datetime/current-datetime

data = {}
with open("tickets.txt", 'r') as file:
    # read the file and store in a dictionary
    for line in file:
        parts = line.strip().split(",")
        id = parts[0].strip()
        event_id = parts[1].strip()
        username = parts[2].strip()
        date = parts[3].strip()
        priority = str(parts[4]).strip()
        data[id] = (event_id, username, date, priority)


def login():
    # let the user try 5 times and check user and password for login
    count = 5
    for i in range(count):
        user = input("please enter your username")
        password = input("please enter your password")
        if user == "admin" and password == "admin123123":
            return menu()
        elif password == "":
            return users_menu(user)
        elif password != "admin123123":
            count -= 1
            if count == 0:
                print("You have exceeded the limit")
                exit()
            print("Incorrect username and/or password\n", "please try again you have ", count, "attempts left")


def menu():
    # displaying admin menu after validating the login
    print("welcome aboard you are an Admin!")
    choice = int(input(("Choose a number from the menu below:\n"
                        "1. Display Statistics\n"
                        "2. Book a Ticket\n"
                        "3. Display all Tickets\n"
                        "4. Change Ticket’s Priority\n"
                        "5. Disable Ticket\n"
                        "6. Run Events\n"
                        "7. Exit")))

    # check user choice and call function accordingly
    if choice == 1:
        statistics()
    elif choice == 2:
        add_ticket(formatted_today)
    elif choice == 3:
        display(formatted_today)
    elif choice == 4:
        change_priority()
    elif choice == 5:
        disable_ticket()
    elif choice == 6:
        today_events(formatted_today)
    elif choice == 7:
        save()


def statistics():
    event_count = {}
    max = 0
    event_id = ""

    # we access dict value and access the events id at index 0 of values list
    for values in data.values():
        event_id = values[0]

        # we count the occurrence of the event id in the dict
        event_count[event_id] = event_count.get(event_id, 0) + 1

    # we search for the highest event id and store it in max
    for value, count in event_count.items():
        if count > max:
            event_id = value
            max = count
    print("the event with the most number of tickets is:", event_id)
    menu()


def add_ticket(formatted_today):
    key_list = []
    ticket_number = 0
    new_ticket = 0

    # add existing to a list to check last ticket number and increment it automatically
    for key in data.keys():
        key_list.append(key)

    # get last ticket number from the list (len)-1
    ticket_number = key_list[len(key_list) - 1][4:]
    ticket_number = int(ticket_number) + 1
    new_ticket = "tick" + str(ticket_number)

    # ask the admin to enter the details
    user = input("please enter username").strip()
    event = input("please enter event id starting with ev:").strip()
    time = input("please enter event date as YYYYMMDD").strip()
    while time < formatted_today:
        time=input("you cant add a ticket in the past! please add another date:").strip()
    prior = input("please enter the ticket priority")

    # create new key and values and update the dictionary
    new_key = new_ticket
    new_values = [event, user, time, prior]
    data[new_key] = new_values
    print("Ticket has been added successfully!")
    menu()


def display(formatted_today):
    #call merge sort function and specify key to sort it by date
    # we print events with recent date and ignore old tickets
    sorted_dict = merge_sort_dict(data, key=get_date_value)

    for key,values in sorted_dict.items():
        if formatted_today <= values[2]:
            print(f" {key}: {sorted_dict[key]}")
    menu()
def merge_sort_dict(input_dict, key):
    #check if dict has more than 1 enty and then call the function recursively after we divide it by half
    if len(input_dict) <= 1:
        return input_dict

    mid = len(input_dict) // 2
    left_half = dict(list(input_dict.items())[:mid])
    right_half = dict(list(input_dict.items())[mid:])

    left_half = merge_sort_dict(left_half, key)
    right_half = merge_sort_dict(right_half, key)

    return merge(left_half, right_half, key)


def merge(left_dict, right_dict, key):
    #we create an empty dict and convert the two half of the dict to lists
    merged = {}
    left_keys = list(left_dict.keys())
    right_keys = list(right_dict.keys())
    left_index, right_index = 0, 0

    # we loop through the two half and compare each index and sort them in ascending order
    while left_index < len(left_keys) and right_index < len(right_keys):
        left_value = left_dict[left_keys[left_index]]
        right_value = right_dict[right_keys[right_index]]

        if key(left_value) < key(right_value):
            merged[left_keys[left_index]] = left_value
            left_index += 1
        else:
            merged[right_keys[right_index]] = right_value
            right_index += 1
    # we check if there's any elements left in the right or left half and add them to final list
    while left_index < len(left_keys):
        merged[left_keys[left_index]] = left_dict[left_keys[left_index]]
        left_index += 1

    while right_index < len(right_keys):
        merged[right_keys[right_index]] = right_dict[right_keys[right_index]]
        right_index += 1

    return merged


def get_date_value(item):
    #specify key to sort dictionary by date
    return item[2]


def get_priority_value(item):
    #specify key to sort dictionary by priority
    return item[3]


def change_priority():
    #ask user to enter ticket Id then search for it in the dictionary
    id = input("please enter ticket ID")
    if id in data:
        #if found update the new priority by changing dict to list so we can update it
        new_priority = int(input("please enter the new priority"))
        ticket_info = list(data[id])
        ticket_info[3] = new_priority
        data[id] = tuple(ticket_info)
        print("priority of ticket", id, "has been changed successfully ")
    else:
        print("ID not found")
    menu()


def disable_ticket():
    # ask the user to enter ticket id and search for it in the dict , the we pop it from the dict
    ticket_id = input("please enter the ticket id you want to remove")
    if ticket_id in data:
        del data[ticket_id]
        print("ticket has been deleted!")
    else:
        # if not found we print not found message
        print("there's no such a ticket id")
    menu()


def today_events(formatted_today):
    # get today timestamp from computer and format it as YYYYMMDD

    events = {}
    keys_to_delete = []

    # check for today events in the dictionary and store them in a new dict
    # store today events key in a list to delete them from the file (we cannot delete while iterating the dict)

    for key, values in data.items():
        if formatted_today == values[2].strip():
            keys_to_delete.append(key)
            events[key] = values

    # sort the new dict using merge_sort by priority and print it in reverse and delete the tickets from today events

    sorted_events = merge_sort_dict(events, key=get_priority_value)
    print("Today events are:")
    for key in reversed(sorted_events):
        print(f"{key}: {sorted_events[key]}")
    for key in keys_to_delete:
        del data[key]

    menu()


def save():
    # ask the user if he wanna save the updates
    save_choice = input("Do you want to save?"
                        "type Y for YES"
                        "type N for NO")
    if save_choice == "Y":
        # read the dictionary as key,values and write to file with the same format
        with open("tickets.txt", "w") as output:
            for key, values in data.items():
                ticket_id = key
                event_id = values[0]
                username = values[1]
                date = values[2]
                priority = str(values[3])
                ticket_entry = f"{ticket_id}, {event_id}, {username}, {date}, {priority}\n"

                output.write(ticket_entry)
        print("all changes has been saved successfully")
        exit()
    elif save_choice == "N":
        exit()
    else:
        print("Invalid input")
        save()


def users_menu(user):
    # displaying user menu after validating the login
    print("welcome aboard ",user)
    choice = int(input(("Choose a number from the menu below\n"
                        "1. Book a ticket\n"
                        "2. Exit")))
    if choice == 1:
        user_ticket(user,formatted_today)
    elif choice == 2:
        save_user()

def user_ticket(username,formatted_today):
    key_list = []
    priority = 0
    ticket_number = 0
    new_ticket = 0
    event_id = input("please enter event id starting with ev:").strip()
    event_date = input("please enter event date").strip()
    while event_date < formatted_today:
        event_date=input("you cant add a ticket in the past! please add another date:").strip()
    # add existing to a list to check last ticket number and increment it automatically
    for key in data.keys():
        key_list.append(key)

    # get last ticket number from the list (len)-1
    ticket_number = key_list[len(key_list) - 1][4:]
    ticket_number = int(ticket_number) + 1
    new_ticket = "tick" + str(ticket_number)

    # create new key and values and update the dictionary
    new_key = new_ticket
    new_values = [event_id, username, event_date, priority]
    data[new_key] = new_values
    print("Ticket has been added successfully!")
    users_menu(username)

def save_user():
    # read the dictionary as key,values and write to file with the same format
    with open("tickets.txt", "w") as output:
        for key, values in data.items():
            ticket_id = key
            event_id = values[0]
            username = values[1]
            date = values[2]
            priority = str(values[3])
            ticket_entry = f"{ticket_id}, {event_id}, {username}, {date}, {priority}\n"

            output.write(ticket_entry)
    print("all changes has been saved successfully")
    exit()
login()
