import re
#with open("html_code.txt","r") as file:
html_file = open("html_code.txt","r")
html_content = html_file.read()
sep = html_content.split("<")


def count_digits(n):
    #n = int(input(" please enter a number"))
    if n < 10:
        return 1
    else:
        return 1+count_digits(n//10)

def find_max(numbers_list):
    # if the list contains 1 number then return it as max
    if len(numbers_list)==0:
        return 0
    if len(numbers_list) == 1:
        return numbers_list[0]
    # assign a temporary max value for the index 1 and compare it with the rest of the list recursively
    temp_max = find_max(numbers_list[1:])
    #compare max of list (temp_max) with index 0
    if numbers_list[0] > temp_max:
        #return number at index 0 if bigger than temp_max
        return numbers_list[0]
    # or else we return the temp_max if bigger
    return temp_max
def count_tags (html_content,tag):
    #we define counts as 0
    tag_counts=0
    # we access the content of the html file
    for i in html_content:
        #if we found tag openning and the tag
        if i == "<"+tag:
            #we increment the tag count
            tag_counts+=1
        #we define remaining content after the tag
        remaining_content = html_content[i+tag:]
    # we recursively call the function with the remaining content
    count_tags(remaining_content,tag)


#display the menu for the user
choice = int(input("1. Count Digits \n"
                       "2. Find Max\n"
                       "3. Count Tags\n"
                       "4. Exit\n"
                       "- - - - - - - - - - - - - - -\n"
                       "Enter a choice:"))
#check user choice
if choice == 1:
    #if choice is 1 then we ask user to input a number and we call the function count_digits
    n = int(input("please enter a number"))
    print("digits in number ",n,": ",count_digits(n),"digits")
    #if choice = 2 we call function find_max()
elif choice==2:
    #ask user to enter numbers
    numbers = input(" please enter a list of numbers:")
    #we create an empty list
    numbers_list = []
    #we split the numbers by the space and add them to the list as int
    for i in numbers.split():
        numbers_list.append(int(i))
    # print the maximum value
    print("the maximum number in the list is:",find_max(numbers_list))
    #if choice = 3 we ask the user to enter the tag he wanna count
elif choice==3:
    tag = input("please enter a tag")
    print("the count of ",tag, "is:",count_tags(html_content,tag))
    #if choice = 4 we exit the program
elif choice==4:
    exit()

