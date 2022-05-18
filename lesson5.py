# methods
name = "Muiruri Mercy"
age = 17
person = "I am " + str(name) + " and my age is " + str(age)
print(person)

print("i am " + name)

# format method
print( " My name is {} and i am {} years old ".format( name,age ))
print(f"My name is {name} and i am {age} years old") 
print(f" My name is \t {name} \n and i am {age}")

user_name = " remove all spaces "
print(user_name)
print(user_name.strip())
user = " the space on the right will be removed "
print(user.rstrip())
usert= " the space on the left will be removed "
print(usert.lstrip())

msg = ''' QRSTLAK12 Mpesa confirmed 
          you have received 100000 from ANGELA MURIUKI
          Safaricom simple,transparent for you'''
print(msg)

multipleLineString = """ You can also print a string
                         multiple line string like this using
                        three single qoutation marks or
                        three double qoutation marks """
print(multipleLineString)

city = "Nairobi" 
print(city[:5])
print(city[2:])
print(city[-1])

# converting to uppercase or lowercase
f_name = "mercy muiruri"
print(f_name.upper())
s_name = "MERCY MUIRURI"
print(s_name.lower())
m_name = "Mercy Muiruri"
print(m_name.upper())
print(m_name.lower())

# concatenation converting one data to another
# integer to float
number = 7
print(float(number))
# floats are numbers with decimals

# integer to string
number = 14
print(str(number))
# here the number is printed as a string

#float to integer
number = 12.34
print(int(number))
# here it prints out the whole number or integer only

f_name = "Metro"
s_name = "Sacco"
full_name = f_name + s_name
print(full_name)

# The .replace method replaces a specific character with another
name = "Brett Cooper"
print(name.replace('t','g'))


msg = "Hello from Mercy Muiruri welcome"
print(msg.split())

print(len(msg))