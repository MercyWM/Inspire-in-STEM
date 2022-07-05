#!usr/bin/python

#########################
#      Loops
#      Name: Mercy Muiruri
#      Date: 23/5/22 
###########################

for number in range(0,9):
    print(number)

print("number\tSquare")
print("______________________")
for number in range(0,9):
    print(number)
    print("\t")
    print(number**2)

print("number\tSquare")
print("______________________")
for number in range(0,9):
    print(number,"\t",number**2)

# assignment
colours = ["blue","red","yellow","green","indigo","violet"]
for colour in colours:
    if colour == "red":
        print(colour.upper())     

#the range function
for number in range(3): #here the code runs through number 0 to 2
    print("Attempt")  
for number in range(1,10,2):
    print("This will print out odd numbers"+str(number)+ number*".") #the last number multiplies he dot by the number 

#iterables
# an iterable is sometjhing that you can iterate over in a for loop
# iterables are like range,strings,and lists
count = 0
for number in range(1,10):
    if number%2==0:
        count += 1   # this is the same as count = count+1
        print(number)
print(f"We have {count} even numbers")
