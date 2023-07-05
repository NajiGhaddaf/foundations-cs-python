####################################
####### Exercice 1 #################
####################################

def factorial():
    #assign an int to the final result
    result = 1
    #take input from user and change type to int
    n = int(input("please enter a positive number"))
    #check if input is negative
    if n < 0:
        #print and return if negative
        print(n , "is a negative number")
        return
    #loop from n till 1 in steps of -1 to get the final result
    for i in range(n,1,-1):
        result *= i
        #print the result
    print ("the factorial of ", n , "is:", result)


########################################
############ Exercice 2 ################
########################################
def divisors():
    #ask user to enter a number and cast it to int
    n = int(input("please enter a number:"))
    #create an empty list for divisors
    divisor = []
    #check if n if negative or 0, return as invalid
    if n <= 0:
        return "number invalid"
    #loop from i=1 as divisor till n
    for i in range(1,n):
        #check if n divided by i (remainder is 0)
        if n % i ==0:
            #add i to the list of divisors if its a divisor
            divisor.append(i)
    #return the list
    return divisor

########################################
############ Exercice 3 ################
########################################
def reverse():
    # We ask the user to enter a string
    phrase = input("please enter a phrase")
    #we create an empty string to return the reversed phrase
    reversed = ""
    #we iterate throught the string from last character till beginning in steps of -1
    for i in range(len(phrase)-1,-1,-1):
        #we add the characters to the reversed string
        reversed = reversed + phrase[i]
    # we return the reversed string
    return reversed


########################################
############ Exercice 4 ################
########################################

def even_numbers():
    # create 2 lists numbers[] to store input in it
    # and even_list to store even numbers
    numbers = []
    even_list = []
    # ask user to input a list of numbers
    n = input("enter a list of numbers")
    #add numbers to the list and split them by space
    for i in n.split():
        numbers.append(int(i))
    #loop through the list and check if number is even (%2 with 0 remainder)
    for i in numbers:
        if i % 2 == 0:
            #add even numbers to even_list
            even_list.append(i)
    #return even numbers list
    return even_list

########################################
############ Exercice 5 ################
########################################

def password():
    #first we create 4 counters to count digits char,upper char,lower and special character
    digits=0
    upper=0
    lower=0
    special=0
    #we define a special character list
    special_char = ["$","#","?","!"]
    # take input from user
    password = input("Please enter your password")
    # check if password length is less than 8 then Weak Password anyway
    if len(password) < 8:
        return "Weak Password"
    #loop through the password and check upper,lower,digits using functions like isupper() islower() isdigits()
    # we add the specified counter each time for the assigned character in password
    for i in password:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        elif i.isdigit():
            digits +=1
        #check if there's a special character from the list
        elif i in special_char:
            special+=1
    # we check if all requirements are met AKA at least 1 upper 1 lower 1 digit 1 special character (counter >0)
    if upper>0 and lower>0 and digits>0 and special>0:
        # if ALL counters are >0 then its a Strong Password
        return "Strong Password"
    #else we return Weak Password
    return "Weak Password"

########################################
############ Exercice 6 ################
########################################
def valid_ip():
    # we ask user to input an IP
    ip = input("please enter your IP")
    # we split the IP by the dots
    octet = ip.split(".")
    # we check if there's 4 dots(octets) as in valid IP ( no extra or missing dots guaranteed)
    if len(octet) != 4:
        #if not then invalid IP
        return "Invalid IP address"
    # we loop through the octets
    for i in octet:
        # we check if octet is negative or bigger than 255
        if int(i)>255 or int(i)<0:
            # invalid ip if so
            return "Invalid IP address"
        # we check if there's a leading 0 in any octet
        if len(i)>=1 and i[0]=="0":
            return "Invalid IP address"
    #finally we can safely return a valid IP !
    return "Valid IP address"
