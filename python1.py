#!/usr/bin/python

# 1. The following line won't run because of a syntax error
# Fixed syntax error
print("hi")

# 2. Exercise 2
# The following lines won't run properly,
# even if the syntax error in the line above is corrected,
# because of a run-time error
# Fixed runtime error
print("hello")

# 3. Display a string (greeting message) directly
print("Hello, welcome to Python!")

# 4. Display the contents of a string variable
message = "This is a string variable"
print(message)

# 5. Display the string which contains single quotes
print("Indian's")

# 6. Display the string which contains Double Quotes
print('Students, "Welcome to SOIS".')

# 7. Read two numbers and perform calculations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculations
sum_value = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
power = num1 ** num2

print("Sum of a and b is : ",sum_value)
print("Difference of a and b is : ",difference)
print("Product of a and b is : ",product)
print("Quotient of a and b is : ",quotient)
print("Remainder of a and b is : ",remainder)
print("Power of a and b is : ",power)

# 8. Check if num1 is an integer
if (num1.is_integer()):
    print("num1 is an integer.")
else:
    print("num1 is not an integer.")

# 9. Convert num1 to an integer
num1 = int(num1)

# 10. Find datatype for variables
print(type(num1))
print(type(num2))

# 11. Read a float value and print the number rounded to 2 decimal places
float_value = float(input("Enter a float value: "))
print(f"Rounded value: {round(float_value, 2)}")

# 12. Read a float value and print the absolute value
print(f"Absolute value: {abs(float_value)}")

# 13. Store different types of values in variables
string_value = "Hello"
numeric_value = 42
complex_value = 1 + 2j
list_value = [1, 2, 3]
dict_value = {"key": "value"}
set_value = {1, 2, 3}
tuple_value = (1, 2, 3)

# 14. Find the data type for the above variables
print(type(string_value))
print(type(numeric_value))
print(type(complex_value))
print(type(list_value))
print(type(dict_value))
print(type(set_value))
print(type(tuple_value))

# 15. Display the number of letters in the string
greeting = "Welcome to Kali Linux"
print(len(greeting))

# 16. Read first name and last name from the user and combine them
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
greeting_message = "Hello, " + full_name + "!"
print(greeting_message)

# 17. Display the string with space
print(f"{first_name} {last_name}")

# 18. Display first two characters from the name
print(full_name[:2])

# 19. Display last three characters from the name
print(full_name[-3:])

# 20. Display 3rd character to last character
print(full_name[2:])

# 21. Display 3rd to 5th character
print(full_name[2:6])

# 22. Create a list of food with two elements
food = ["Roti", "Chapatti"]

# 23. Add one more to the food list
food.append("Rice")

# 24. Add two more food strings
food.extend(["Panipuri", "Idli"])

# 25. Count total number of items in the list
print(len(food))

# 26. Print the first two items in food using slicing notation
print(food[:2])

# 27. Print the last item in food using index notation
print(food[-1])

# 28. Debug: Check if the number is odd or even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# 29. Debug: Convert Centigrade to Fahrenheit
c = float(input("Enter temperature in Centigrade: "))
f = 9 * (c / 5) + 32
print("Temperature in Fahrenheit is:", f)

# 30. Debug: Calculate average of user inputs
count = int(input("Enter the count of numbers: "))
total_sum = 0
for _ in range(count):
    x = int(input("Enter an integer: "))
    total_sum += x
avg = total_sum / count
print("The average is:", avg)

# 31. Prove strings are immutable and lists are mutable
# Strings are immutable
str_value = "Hello"
try:
    str_value[0] = 'h'
except TypeError as e:
    print(f"Strings are immutable: {e}")

# Lists are mutable
list_value = [1, 2, 3]
list_value[0] = 100
print(f"Lists are mutable: {list_value}")
