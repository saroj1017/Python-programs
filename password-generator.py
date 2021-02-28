#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

r1=[]
for i in range(1,nr_letters+1):
  r1.append(random.choice(letters))

# r2=''
for i in range(nr_symbols):
  r1.append(random.choice(symbols))

# r3=''
for i in range(nr_numbers):
  r1.append(random.choice(numbers))

# the above program will have a order of letter , symobols and numbers 
# to randomiize that order also we use the shuffle method
# a very handy method to randomize stuff
# print(r1)
random.shuffle(r1)
# print(r1)

r2=''
for i in r1:
  r2+=i
print(r2)


# example output
'''
Welcome to the Python Password Generator!
How many letters would you like in your password?
4
How many symbols would you like?
6
How many numbers would you like?
8
65P680$&m(+z09#V$8
'''
