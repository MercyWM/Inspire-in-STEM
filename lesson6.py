
# learning about lists
motorcycle = ['honda','yamaha','suzuki']
print(motorcycle)

# accessing list items using the index
print(motorcycle[0])

# changing the value of an item in the list
motorcycle[0]= 'Bugatti'
print(motorcycle[0])
print("I think " + str(motorcycle[0]) + "s are cheap")

# adding elements in a list
motorcycle.append("Motorolla")
print(motorcycle)
# you can only append one argument to a list

plate_number = ['H1234','Y2345','S3456']
motorcycle = ['honda','yamaha','suzuki']
print(str(motorcycle[0]),str(plate_number[0]))
print(str(motorcycle[1]),str(plate_number[1]))
print(str(motorcycle[2]),str(plate_number[2]))
print(str(motorcycle[0]),str(plate_number[0]),str(motorcycle[1]),str(plate_number[1]),str(motorcycle[2]),str(plate_number[2]))
print(motorcycle[0] + plate_number[0] + motorcycle[1] + plate_number[1] + motorcycle[2] + plate_number[2])

# deleting an  item from a list
motorcycle = ['honda','yamaha','suzuki']
del motorcycle[2]
print(motorcycle)
print(motorcycle[-1])

# the pop method to delete an item
motorcycle = ['honda','yamaha','suzuki']
motorcycle_owner = "Mojo jojo"
popped_motorcycle = motorcycle.pop()
print(motorcycle) # this prints out the list but deletes the last item
print(popped_motorcycle) # this prints what it had deleted same as this next code
print(motorcycle.pop())
#print("My name is " + str(motorcycle_owner) + " and I own a " + str(motorcycle[2]) + " plate number " + str(plate_number[0])) this code won't run since the motorcyle[2] was popped out or deleted hapo juu
print("My name is " + str(motorcycle_owner) + " and I own a " + str(motorcycle[0]) + " plate number " + str(plate_number[0]))
print(f"My name is {motorcycle_owner} and i own a {motorcycle[0]} plate number {plate_number[0]}") # using the dot format
print(" My name is {} and i own a {} plate number {}".format(motorcycle_owner,motorcycle[0],plate_number[0])) # using the dot format

# using the remove function to remove an item from a list
motorcycle = ['honda','yamaha','suzuki']
motorcycle.remove("suzuki")
print(motorcycle)

school = ["Joy","Hope","Mercy","Peace"]
pupil = ["Furaha","Imani","Huruma","Amani"]
print(str(school[0]), str(pupil[0]))
print(str(school[1]), str(pupil[1]))
print(str(school[2]), str(pupil[2]))
print(str(school[3]), str(pupil[3]))
print(f"{school[0]} {pupil[0]} {school[1]} {pupil[1]} {school[2]} {pupil[2]} {school[3]} {pupil[3]} ")
for pupil in pupil:
    print(f" Hello I am {pupil}")
for school in school:
    print(f" I go to {school}")