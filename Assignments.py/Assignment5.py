#!usr/bin/python

#########################
#      LISTS 3
#      Name: Mercy Muiruri
#      Date: 25/5/22 
###########################

# write a list of vehicles and access jeep and convert it to uppercase
# using a for loop in a list
vehicles = ["mercedes","bmw","jeep","toyota","audi"]
for vehicle in vehicles:
    print(vehicle.title())
vehicles = ["mercedes","bmw","jeep","toyota","audi"]   
for vehicle in vehicles:
    if vehicle == "jeep":
        print(vehicle.upper())
vehicles = ["mercedes","bmw","jeep","toyota","audi"]
print(vehicles[2].upper())
 
### equals an is not equals to
age = 17
if age != 16: #if age is not sixteen
    print("You are not sixteen")
if age == 16: #if age is equal to sixteen
    print("you are sixteen")

# checking if something is in a list
banned_users = ["Matt","Andrew","Marie","Johnson","Nate"]
user = "Antony"
if user not in banned_users:
    print("Welcome to the site")


