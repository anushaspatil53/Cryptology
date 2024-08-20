#!usr/bin/python

#String Operations in Python 

Greeting='Welcome to Cryptology Lab'

print(Greeting)

#1. Find the length of the string 

print('Length of the string is:',len(Greeting))

#2. Slice the string as per your choice 

print('Slicing of string : ',Greeting[3:20])

#3. Concatenate two strings
Topic='Todays topic is python'
print('Concatenation of two strings')
print(Greeting+' '+Topic)

#4. Convert in to lower case in to uppercase character 
print('Converting to lower case',Greeting.lower())

#5. Convert upper case into lower case characters
print('Converting to upper case',Greeting.upper())


#6. convert the character into Unicode ( Ascii values)
a='D'
print('ASCII value of character D is:',ord(a))

#7. convert Unicode into character 
i=65
print('Converting a number to ascii character :',chr(i))

#8. Check whether the given "substring" exists in the string
if 'Lab' in Greeting:
    print("Yes,Substring 'Lab' is present in string")
else:
    print("No,Substring 'Lab' is not present in string")

#9. Replace the character 'k' with 'h'
b='kitkat, kite, king'
c=b.replace('k','h')
print(f"'k' in {b} is replaced with 'h': {c}")

#10. Pad the string with "x" at the end
c='hello'
print(c.ljust(20,'x'))

print(c.rjust(20,'x'))


#11. remove leading and trailing whitespace or specified characters from the string
d='            Hi                               '
print(d)
print(d.strip())

#12. split the given string in to group of five characters 
word='Hellowelcometocryptologylab'
group_size=5
print("Grouped string : ",[word[i:i+group_size] for i in range(0, len(word), group_size)])

#13. count total number of words 
word = 'Hello welcome to cryptology lab'
print("Total number of words:", len(word.split()))

#14. Find the frequency of each characters in the string 
from collections import Counter
word = 'Cryptology'
print(Counter(word))

#STDIN and File operators 
#15. get the file name from the user 
file1 = input('Enter the file name ')
print("File name is ",file1)

#16. check the file exist or not
import os 
if os.path.exists(file1):
	print('File exits')

#Looping and File handling 
#17. read the contents from the file 
file = open("file1.txt", "r")
contents = file.read()
print(contents)
file.close()

#18. reverse the contents from the file
filename="file1.txt"
with open(filename,'r') as file:
	contents=file.read()
print('reversed contents:',contents[::-1])

#19. Write into the file
filename = "file1.txt"
content = "Hi, This is LOS lab"
with open(filename, 'w') as file:
	file.write(content)
file = open("file1.txt", "r")
contents = file.read()
print("Write into file",contents)
file.close()
	
#Math operations 
#20. convert Frequency in to percentage
frequencies = {'a':6,'b':2,'c':5,'d':1,'e':8}
total = sum(frequencies.values())
percentages = {k: (v / total) * 100 for k, v in frequencies.items()}
print("Frequency in to percentages:", percentages)

#21. Perform modular arithmetic operation 
a,b = 200,7
print("Modular Addition = " ,(a + b) % b)
print("Modular Substraction = " ,(a - b) % b)
print("Modular Multiplication = " ,(a * b) % b)
print("Modular Division = " ,(a // b) % b)

#22. Find the prime numbers 
#check the given number is prime or not 
#print the prime numbers with the given range
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

# Example usage
print("Prime numbers between 1 and 50:")
print_primes(1, 100)

# Check if a number is prime
number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    
    
#23. Check the given two numbers are co prime or not
import math
def are_coprime(a, b):
    return math.gcd(a, b) == 1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if are_coprime(num1, num2):
    print(f"{num1} and {num2} are co-prime.")
else:
    print(f"{num1} and {num2} are not co-prime.")

#24. find the factors for the given number ( can use python library)
n = int(input("Enter a number to find factors: "))
factors = []
for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
print("Factors : ",sorted(factors))

#25. generate 10 random numbers 
import random
count = 10
random_numbers = [random.randint(1, 100) for _ in range(count)]
print("Random numbers:", random_numbers)


