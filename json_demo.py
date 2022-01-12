# Write 2 programs
# 1. to create address book and write some records into it
# 2. Read this address book
# no object in python like json. pyhton native object s are dictionary,int,string ,etc

# create an object
book = {}
book['tom']={
    'name':'tom',
    'address': '1 red street , NY',
    'phone':12345
}
book['bob']={
    'name':'bob',
    'address':'1 green street, NJ',
    'phone':67890
}

import json
s = json.dumps(book) #json.dumps takes a dictionary object and converts into json string dataset
print("Json String = ", s)
# write this string i a file
with open("/home/h/PycharmProjects/book.txt",'w') as f:
    f.write(s)
x = open("/home/h/PycharmProjects/book.txt","r")
a = x.read()
print(type(a))
print("Dictionary = ", a)
b = json.loads(a)
print(b['tom']['phone'])
for person in book:
    print(book[person])


