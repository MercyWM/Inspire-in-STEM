#!usr/bin/python

# write a program to withdraw Ksh 25000 if account balance is between Ksh 100000 to Ksh 200000 
# 30% if account balance between 500000 to 1000000
# above 1000000 deduct only 15000

acc_balance = input("Enter your account balance here")
if (int(acc_balance)>100000 and int(acc_balance)<200000) :
    acc_balance = int(acc_balance)- 25000
    print("Ksh 25000 has been withdrawn from your account. Your new account balance is " + str(acc_balance))

elif (int(acc_balance)>500000 and int(acc_balance)<1000000):
          acc_balance = float(acc_balance) - (0.3*float(acc_balance))
          print("We have deducted some of your account balance. Your new account balance is " + str(acc_balance))

elif (int(acc_balance)>1000000):
        acc_balance = int(acc_balance) - 15000
        print("We have removed 15000 from your account balance " + str(acc_balance))
