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
