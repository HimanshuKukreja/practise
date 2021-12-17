
tom_expenses_monthly = [2500,2330,5080,6000]
sam_expenses_monthly = [3000,5050,4900,2880]

def calculate_total_expenses(expenses):
    # print("hello")
    total = 0
    for i in range(len(expenses)):
        print("Month : ", i+1,"Expenses:", expenses[i])
        total = total + expenses[i]
    return total

    # tom_expenses_monthly_total = calculate_total_expenses(tom_expenses_monthly)
print("Tom's total monthly expenses = ", calculate_total_expenses(tom_expenses_monthly))

sam_expenses_monthly_total = calculate_total_expenses(sam_expenses_monthly)
print("Sam's total monhtly expenses = ", sam_expenses_monthly_total)


