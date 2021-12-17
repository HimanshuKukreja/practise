key_location = "rest room"
locations = ['garden','Living room','rest room','kitchen','upstairs']

for i in locations:
    if i == key_location:
        print("Keys found in : ", i)
        break
    else:
        print("keys not found in :", i)
