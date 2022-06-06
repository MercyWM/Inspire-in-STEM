#!usr/bin/python

##########################
#      Tuples
#      Name: Mercy Muiruri
#      
###########################

# list. This is a normal list that can be edited.
fruits = ["mango","guava","banana","pineapple"]
fruits[2]= "apple" # here the value of banana is changed to apple
print(fruits)

# mutable(can be edited)   # immutable(cannot be edited)
# lists[]                  # tuples()
# dictionaries{}


# this is a list that is immutable. It can not be edited. It is called a tuple.
new_fruits = ("guava","apples","banana","peaches")
new_fruits[2] = "pineapple" # this won't work since a tuple cannot be changed
print(new_fruits)

cars = ("audi","bmw","nissan","toyota")
print(cars)
cars = ("nissan","bmw","nissan","toyota") #in order to change the value of a tuple you have to rewrite the tuple
print(cars)

favFoods = ("chips","ndengu","fish","avocado")
for favFood in favFoods:
    print(favFood)
