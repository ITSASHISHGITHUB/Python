# SPECIAL CHARACTERS

# Backslash \" is used to include double quotes inside a double-quoted string
print("Hi \"Python\"")
# Single quotes allow double quotes inside without any escape character
print('hi "python"')
# \\ is used to print a single backslash (\), since \ alone is an escape character
print("Path: C:\\USERS\\ASHISH")

print("ashish\n")  # \n is an escape sequence that moves the cursor to a new line

# \t is an escape sequence that inserts a horizontal tab (indentation)
print("ashish\t")

print("""Your Learning Path:
        \t-Python Basics
        \t-Data Engineering
        \t-AI""")  # Triple quotes """ allow multi-line strings; \t adds indentation before each item

# In Python, print() is used to display output to the console — commonly used for debugging and testing


# VARIABLES

# Static strings — the value is hardcoded directly into the print statement
print("My name is Ashish")
print("Ashish is learning Python")
print("Ashish wants to crack Google")

# Dynamic variable — the value is stored in a variable and can be reused or changed in one place
name = "Ashish"

print("My name is", name)  # the variable 'name' is passed as a dynamic value
print(name, "is learning Python")
print(name, "wants to crack Google")

# Using two variables — Python executes code line by line, top to bottom
first = "Ashish"
last = "Yadav"

print("My name is", first, last)  # prints full name using both variables
print(first, "is learning Python")
print(first, "wants to crack Google")


# F-STRINGS

mail = "ay677204.com"
# f-strings let you embed variables directly inside a string using {}
# \n breaks each email address onto a new line
print(f"info@{mail}\nsupport@{mail}\nwww.{mail}")


# INPUT

# input() alone reads the user's response but immediately discards it
# to keep the value, assign it to a variable
input("Enter your name: ")

# stores the user's response in a variable — dynamic
name = input("Enter your name: ")
country = "India"                  # hardcoded value — static
print("Your name is", name, "and you come from", country)
