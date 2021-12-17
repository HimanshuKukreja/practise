# dictionary is mpre of key value pair

dict = {"A":123,"B":456,"C":789}
print("dictionary = ", dict)

# Add a key in dictionary
dict["D"] = 101
print("Dictionary with added key", dict)

# Dictionary with deleted key
del dict["C"]
print("Dictionary with deleted key =", dict)

# to fetch a value of particular key
print("Value of a particular key = ", dict["A"])

for key in dict:
    print("Key:", key," Value:", dict[key])

# second way for loop

for k,v in dict.items():
    print("key:", k, "value:", v)

# check partitcular key present in dictionary
if "A" in dict:
    print("true")

# to clear dictionary
dict.clear()
print("Empty dictionary =", dict)