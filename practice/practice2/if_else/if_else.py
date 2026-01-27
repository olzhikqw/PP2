# The else keyword catches anything which isn't caught by the preceding conditions.
# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

#1
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#2
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#3
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")

#4
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")

#5
password = "1234"
if password == "1234":
    print("Access")
else:
    print("Denied")