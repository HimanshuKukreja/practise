# Write a function called print_pattern that takes integer number as an argument
# and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
#
# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def print_pattern(input):
    for i in range(input):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)
    # return s

print(print_pattern(3))
