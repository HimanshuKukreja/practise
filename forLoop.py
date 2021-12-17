# for loop to calculate sum of monthly expenses

expenses = [2450,2500,2550]
total = 0
# for i in expenses:
#     total = total + i
# print("total monthly expenses = ", total)

# for i in range(1,11):
#     print(i)

for i in range(len(expenses)):
    print("Month : ", i+1,"Expenses :", expenses[i])
    total = total + expenses[i]
print(" Total Monthly expenses = " , total)