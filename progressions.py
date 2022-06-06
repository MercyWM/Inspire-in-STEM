#!usr/bin/python

#########################
#      ARITHMETIC AND GEOMETRIC PROGRESSIONS
#      Name: Mercy Muiruri
#      Date: 26/5/22 
###########################

# ARITHMETIC PROGRESSIONS
a = int(input("Enter the the first term"))
d = int(input("Enter the common difference"))
n = int(input("Enter the nth term"))
for i in range(1,n+1): # here i means each value of n
    nth_term = a + (i-1)*d    # the nth term is given by this formula
    print("The "+ str(i) + "th term is " + str(nth_term))      # remember that the i is each value of nth terms in that range 


sum_of_numbers_in_an_AP = (nth_term/2)*(2*a + (n-1)*d)
print(sum_of_numbers_in_an_AP)

# GEOMETRIC PROGRESSIONS
a = int(input("Enter the the first term"))
r = int(input("Enter the common ratio"))
n = int(input("Enter the nth term"))
for i in range(1,n):
    nth_term = a*(r** (i-1))
    print("The "+str(i) + "th term of a geometric sequence is "+ str(nth_term))

if r>1:
    sum_of_numbers_in_a_GP = (a*((r**n)-1))/(r-1)
else:
    sum_of_numbers_in_a_GP = (a*(1-(r**n)))/(1-r)
print(sum_of_numbers_in_a_GP)