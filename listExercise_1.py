# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

month_list=["Jan","Feb","March","April","May"]
print("Month list = ", month_list)
expense_list = [2000,2350,2600,2130,2190]
print("Expense list = ", expense_list)

# 1. In Feb, how many dollars you spent extra compare to January?
###### dictionary approach ############
# l = {"Jan": 2200,"Feb": 2350,"March":2600,"April":2130,"May":2190}
# print(type(l))
# print("l = ", l)
# print("In Feb, how many dollars you spent extra compare to January = ",l["Feb"]-l["Jan"], "dollars")
#####################################################
Diff = expense_list[month_list.index("Feb")]-expense_list[month_list.index("Jan")]
print("\n1. In Feb, how many dollars you spent extra compare to January = ", Diff)

# 2. Find out your total expense in first quarter (first three months) of the year.
total = 0
for i in range(3):
    total = total + expense_list[i]
print ("\n2. Total expense in first quarter (first three months) of the year = ", total)

# 3. Find out if you spent exactly 2000 dollars in any month
if 2000 in expense_list:
    a = expense_list.index(2000)
    print("\n3. Month = ", month_list[0],"==>","Expense = ",expense_list[a])

else:
    print("\n3. No month with expense of exactly 2000")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
month_list.append("June")
expense_list.append(1980)
print("\n4.Updated Month list =", month_list,"\n  Updated Expense list =", expense_list)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
x = month_list.index("April")
expense_list[x] = expense_list[x] - 200
print("\n5.Month List =", month_list,"\n  Updated Expense list =", expense_list)