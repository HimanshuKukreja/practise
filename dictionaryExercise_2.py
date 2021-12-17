#You are given following list of stocks and their prices in last 3 days,

# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]

# Write a program that asks user for operation. Value of operations could be,
#a. print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33

# b. add: When user enters 'add', it asks for stock ticker and price.
# If stock already exist in your list (like info, ril etc) then it will append the price to the list.
# Otherwise it will create new entry in your dictionary.
# For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
dict = {"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
print("Dictonary = ", dict)
# A = dict["info"]
# avg_A = round((A[0]+A[1]+A[2])/len(A),2)
# B = dict["ril"]
# avg_B = B[0]+
operations_list=['print','add']
user_input = input("Enter operations:").lower()
if user_input in operations_list:
    if user_input=='print':
        for k,v in dict.items():
            print(k,"==>",v,"==>","avg: ", round(sum(v)/len(v),2))
    elif user_input == 'add':
        add_stock_ticker_key = input("Enter a stock ticker key:").lower()
        add_stock_ticker_value = int(input("Enter a stock ticker value:"))
        # d = {"add_stock_ticker_key":add_stock_ticker_value}
        # print(d)
        if  add_stock_ticker_key in dict:
            dict[add_stock_ticker_key].append(add_stock_ticker_value)
            print("Dictionary = ",dict)
        else:
            dict[add_stock_ticker_key]=[add_stock_ticker_value]
            print("New Dictionary after adding = ", dict)
else:
    print("Invalid operations")
