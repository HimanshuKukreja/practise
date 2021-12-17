# Check number i seven or odd
# take number from input
# num = input("Enter your number : ") #here number would be in sting type
# num = int(num) #cast it into num
# c= num%2
# if (c==0):
#     print("Number is even")
# else:
#     print("Number is odd")


# operators
# >,<,and,<=,>=,!=,or,+=,-+, not

# if else for dish program find out which dish is this
indian = ['daal','samosa','poha']
italian = ['pizza','pasta','garlic bread']
chinese = ['noodles','fried rice','manchurian']
dish = input("enter a dish : ")
if dish in indian:
    print("indian dish")
elif dish in chinese:
    print("chinese dish")
elif dish in italian:
    print("italian dish")
else:
    print("unknown dish :" , dish)
