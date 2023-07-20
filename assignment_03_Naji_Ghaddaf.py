import json


def menu():
    #check user input and call function accordingly

    choice =int(input(("Please enter your choice:\n"
          "1. Sum Tuples\n"
          "2. Export JSON\n"
          "3. Import JSON\n"
          "4. Exit")))

    if choice == 1:
        print(sum_tuples(tup1,tup2))

    elif choice == 2:
        export_json(json_file,dict)

    elif choice == 3:
        print(import_json(data))
    else:
        exit()

def sum_tuples(tup1,tup2):
    #convert the two tuples to two lists & create a 3rd empty list
    list1= list(tup1)
    list2= list(tup2)
    list3 =[]

    #loop through the len of list1 or list2 (same length) and add the value to 3rd list
    for i in range(len(list2)):
        list3.append(list1[i]+list2[i])
    #convert list3 to tuple3 and print it
    tup3 = tuple(list3)
    print("the sum of the two tuples is: ",tup3)
    return  menu()

def export_json(json_file,dict):
    # initiate starting string of json file
    json_string = "{\n"
    # loop through the dictionary and concatenate the keys and values with appropriate json documentation
    for key, value in dict.items():
        json_string += '  "' + str(key) + '": "' + str(value) + '",\n'

    json_string = json_string[:-2]  # Remove the last two characters (comma and newline)
    json_string += "\n}"
    json_file.write(json_string)
    return menu()

def import_json(data):
    list= []
    #eliminate whitespace and new lines
    data = data.replace(" ","").replace("\n","")
    #initiate start index and loop through the file while true
    start_index = 0
    while True:
        # find the opening bracket
        start_object_index = data.find("{",start_index)
        # if no more opening brackets => break
        if start_object_index == -1:
            break
        # find closing brackets
        end_object_index = data.find("}",start_object_index)
        #error in file
        if end_object_index==-1:
            break
        #converting data found to a dictionary using .loads() and append dict to a list
        json_object = data[start_object_index:end_object_index + 1]
        dictionary = json.loads(json_object)

        list.append(dictionary)
        start_object_index = end_object_index+1

    print(list)
    return menu()





tup1= (1,2,3)
tup2 = (4,99,6)

json_file = open("json.json","w")
json_import = open ("json2.json","r")
data = json_import.read()
dict = {"name" : "Naji" , "age" : 27, "married" : True}


menu()



####################################
########### EXERCICE ###############
####################################
#a.     1/6N+8000N3+24 => O(N3) since its cubic and the worst case scenario we ignore 1/6N and the constant
#b.     1/6N3 => O(N3) we ignore the constant
#c.     1/6N! +200N4 => O(N!) since its factorial and the slowest we ignore N4
#d.     NlogN +1000 => O(NlogN) we ignore the constant
#e.     logN +N => O(N) since logN is faster and N is the worst case
#f.     1⁄2N(N-1) => O(N2) for nested N algorithm
#g.     N2+220NlogN2+3N+9000 => O(N2) is the biggest time complexity in the phrase
#h.     N!+3N+2N+N3+N2"""=> O(N!) factorial is the worst time complexity


