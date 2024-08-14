#!usr/bin/python
Greeting='Welcome to Cryptology Lab'

print(Greeting)

print('Length of the string is:',len(Greeting))

print('Slicing of string : ',Greeting[3:20])

Topic='Todays topic is python'
print('Concatenation of two strings')
print(Greeting+' '+Topic)

print('Converting to lower case',Greeting.lower())
print('Converting to upper case',Greeting.upper())


a='D'
print('ASCII value of character D is:',ord(a))

i=65
print('Converting a number to ascii character :',chr(i))

if 'Lab' in Greeting:
    print("Yes,Substring 'Lab' is present in string")
else:
    print("No,Substring 'Lab' is not present in string")

b='kitkat, kite, king'
c=b.replace('k','h')
print(f"'k' in {b} is replaced with 'h': {c}")

c='hello'
print(c.ljust(20,'x'))

print(c.rjust(20,'x'))

d='            Hi                               '
print(d)
print(d.strip())

