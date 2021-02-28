# A sligtly differnt approach to check the user input is prime or not

def prime_checker(number):
  if number in range(1,4):
    print("It's a prime number")
  
  #count=0
  if number > 3:
     for i in range(2,number):
         if number % i == 0:
            print(f"the first number divisble by {number} is {i}")
            print('Its not a prime number ')
            break

         else:
           #print(number, i)
           # it checks for all the numbers are divisible or not and then if the number divides by itself then its clearly a prime number 
           if number==i+1:
             print('Its a prime number') 

n = int(input("Check this number: "))
prime_checker(number=n)
