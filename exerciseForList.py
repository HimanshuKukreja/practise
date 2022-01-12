# Exercise 1: Reverse a list in Python

list1 = [100,200,300,400,500]
list1.reverse()
print("Reversed List = {}".format(list1))

# Exercise 2: Concatenate two lists index-wise
# expected output --> ['My', 'name', 'is', 'Kelly']
a = ["M", "na", "i", "Ke"]
b = ["y", "me", "s", "lly"]
x = []
for i in range(len(a)):
    c = a[i] + b[i]
    x = x + c
    # print(c)
print("x = {}".format(x))



