#You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
heros=['spider man','thor','hulk','iron man','captain america']
print("Marvel Heros list = ", heros)

# 1. Length of the list
print("\n1. Length of the list =", len(heros))

# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print("\n2. Updated Marvel Heros List =", heros)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove("black panther")
a = heros.index("hulk")
heros.insert(a+1,"black panther")
print("\n3. Updated Marvel Heros List =", heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=["doctor strange"]
print("\n4. Updated list = ", heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print("\n5. Updated Marvel Heros List =", heros)