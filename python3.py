#!/usr/bin/python

#1. Write a python script to encrypt the string using Caesar cipher.
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
		
#2. Write a Python script to Modify the above script to shift cipher based on user choice.
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
		
#3. Write a Python script to convert cipher text into uppercase characters and split the cipher into group of 5 of characters.
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

#4. Write a Python program to Find the histogram for each characters.

