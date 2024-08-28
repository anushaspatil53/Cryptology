#!/usr/bin/python

1. Write a python script to encrypt the string using Caesar cipher.
greet = 'heLlo worldz'
k=3
for i in greet:
	#temp=ord(i)+k
	if 97<=ord(i)<=122:
		temp = ord(i)+k
		if temp>122:
			temp = temp - 26
			print(i,temp,chr(temp))
		else:
			print(i,temp,chr(temp))
	else:
		print(i,ord(i),i)
		
2. Write a Python script to Modify the above script to shift cipher based on user choice.
greet = 'heLlo worldz'
k=int(input('Enter the value of key for shift cipher'))
for i in greet:
	#temp=ord(i)+k
	if 97<=ord(i)<=122:
		temp = ord(i)+k
		if temp>122:
			temp = temp - 26
			print(i,temp,chr(temp))
		else:
			print(i,temp,chr(temp))
	else:
		print(i,ord(i),i)
		
3. Write a Python script to convert cipher text into uppercase characters and split the cipher into group of 5 of characters.
greet = 'heLlo worldz'
k=int(input('Enter the value of key for shift cipher'))
res=''
for i in greet:
	#temp=ord(i)+k
	if 97<=ord(i)<=122:
		temp = ord(i)+k
		if temp>122:
			temp = temp - 26
			res+=chr(temp)
		else:
			res+=chr(temp)
	else:
		res+=i
cipher_upper=res.upper()
for i in range(0, len(cipher_upper), 5):
	print('Group of 5 ',cipher_upper[i:i+5])
#print('Group of 5 ',[cipher_upper[i:i+5] for i in range(0, len(cipher_upper), 5)])

4. Write a Python program to Find the histogram for each characters.

import matplotlib.pyplot as plt
from collections import Counter
string = input("Enter a string:")
char_counts=Counter(string)
characters = list(char_counts.keys())
counts = list(char_counts.values())
plt.bar(characters,counts,color='skyblue',edgecolor='black')

plt.title('Histogram of Characters in String')
plt.xlabel('Character')
plt.ylabel('Frequency')

plt.show()

5. Write a Python script to read the contents from the file. 
file = open("python3.py", "r")
contents = file.read()
print(contents)

6. Write a Python script to encrypt the contents from the file. 
greet = contents
k=int(input('Enter the value of key for shift cipher'))
res=''
for i in greet:
	#temp=ord(i)+k
	if 97<=ord(i)<=122:
		temp = ord(i)+k
		if temp>122:
			temp = temp - 26
			res+=chr(temp)
		else:
			res+=chr(temp)
	else:
		res+=i
		
print(res)
		
file.close()  

7. Do validation to the python program (2) 
   - not to accept special characters 
   - not to accept numeric values 
   - not to accept empty value 
   - accept only string
   - string should be lowercase if not convert the case
import re 

print("Validation of python program")
def validation(input):
	if not isinstance(input,str):
		return "Input must be string"
	if input.strip()=="":
		return "Input can't be empty"
	if not re.match("^[a-zA-Z\s]+$", input):
		return "input only contains alphabets and spaces"
	
	processed_string = input.lower()
	
	return processed_string
	
input = input("Enter a string:")
res = validation(input)
print(res)

8. Write a Python program to checks if two given strings are anagrams of each other.
example: mug, gum
         cork, rock
         note, tone

print("Anagram")         
string1 = input("Enter first string:")
string2 = input("Enter second string:")
if (sorted(string1)==sorted(string2)):
	print(string1," ",string2," ","are anagrams")
else: 
	print(string1,string2," ","are not anagrams")

9. Write a Python program to check the given string is palindrome or not
Do not use built in functions 

Example: MADAM 
         RACECAR
         LEVEL
         CIVIC
         
print("Palindrome")
string = input("Enter first string:")
reversed_string = string[::-1]
if (string == reversed_string):
	print("palindrome")
else:
	print("not a palindrome")

10. Write a Python program to check if a substring is present in a given string.
Example: Understand -- stand 

print("Program to check wheather substring present in string")
string = input("Enter a string:")
substring = input("Enter a substring:")
if substring in string:
	print("substring",substring,"present in string",string)
else:	
	print("substring",substring,"not present in string",string)

11. Explore string module 
   import the string module in your python script. 
   print all the lowercase characters
   print all the uppercase characters 
   print all the lowercase and uppercase characters
   print all the digits 
   print all the punctuation symbols  
   count the total number of punctuation symbols 


import string 

print("All lowercase characters:",string.ascii_lowercase)
print("All uppercase characters:",string.ascii_uppercase)
print("All lowercase and uppercase characters:",string.ascii_letters)
print("All digits:",string.digits)
print("All the punctuation symbols",string.punctuation)
count_punctuations = len(string.punctuation)
print("The total number of punctuation symbols:",count_punctuations)



