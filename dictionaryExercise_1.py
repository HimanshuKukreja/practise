# We have following information on countries and their population (population is in crores),
#
# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21

# Using above create a dictionary of countries and its population
dict = {"China":143,"India":136,"USA":32,"Pakistan":21}
print("Dictionary = ", dict)

# Write a program that asks user for three type of inputs,
# a. print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21

# add: if user input add then it should further ask for a country name to add.
# If country already exist in our dataset then it should print that it exist and do nothing.
# If it doesn't then it asks for population and add that new country/population in our dictionary
# and print it

operation_list = ["print","add","remove","query"]
user_input = input("Enter an operation :").lower()
if user_input in operation_list:
    if user_input == "print":
        for k,v in dict.items():
            print(k,"==>",v)

    elif user_input == "add":
        new_country = input("enter a new country :").lower()
        # print("new country = ", new_country)
        # print("Check whether country already exists...")
        if new_country in dict:
            print("Country already exists")
        else:
            print("Country doesn't exists in dataset so add in dictionary")
            dict[new_country] = 8
            print("Dictionary after adding country =", dict)

# remove: when user inputs remove it should ask for a country to remove.
# If country exist in our dictionary then remove it and print new dictionary using format shown above in (a).
# Else print that country doesn't exist!
    elif user_input == "remove":
        remove_country=input("Enter country to remove:").lower()
        if remove_country in dict:
            # print("Remove country from present dictionary")
            del dict[remove_country]
            print("Dictonary after removing country:", dict)
        else:
            print("Country doesn't exists in present dictionary")

    elif user_input == "query":
        print("Which country wants to be queried")
        query_country = input("Entry country to be queried:").lower()
        if query_country in dict:
            print("Country :",query_country,"==>", "population:",dict[query_country] , "Crores")
        else:
            print("Query country doesn't exists in dataset")
else:
    print("Invalid operations")


