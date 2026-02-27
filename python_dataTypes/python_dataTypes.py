# VARIABLES & DATA TYPES

a = 10
# 'a' is the variable (the label) and 10 is the value (the data stored inside it)

# .upper() is a string method — it converts all characters to uppercase
# methods are called using dot notation: variable.method()
name = "ashish".upper()
print(name)  # Output: ASHISH

# .upper() only works on strings — calling it on a number will throw a TypeError
# "ashish".upper() ✅  |  (2).upper() ❌
name = "ashish"
print(name.upper())  # calling .upper() via a variable — same result


# DATA TYPES & OPERATORS

# int + int = int (arithmetic addition)
# 2 + 5 = 7

# str + str = str (string concatenation — joins the two strings together)
# "2" + "3" = "23"


# DATA TYPES (BASICS)

a = 10          # int      — whole numbers, positive or negative (e.g. 10, -5, 0)
b = 12.3        # float    — decimal numbers (e.g. 12.3, 3.14, -0.5)
c = "ashish"    # str      — text, always wrapped in quotes (e.g. "hello", 'world')
d = True        # bool     — only two possible values: True or False (capital T and F)
e = None        # NoneType — represents the absence of a value (unknown or not set yet)
f = ""          # str      — empty string, it exists but holds no characters
g = " "         # str      — whitespace string, it looks empty but contains a space character

# Note: None, "" and " " are all different:
# None  → no value at all
# ""    → a string that exists but is empty
# " "   → a string that contains a space


# FUNCTIONS

# A function is an independent block of code that performs a specific task
# It is not attached to any value or object — it stands on its own

# Syntax:
# function_name(value)

# Examples:
print('hello')   # print() is a built-in function that displays output
type(40)         # type() is a built-in function that returns the data type of a value

text = "ashish"
number = 10

print(type(text))
print(len(text))


# METHODS

# A method is a function that belongs to an object or a data type (class)
# It is always called on a value using dot notation

# Syntax:
# value.method_name()

# Examples:
"hello".upper()    # .upper() belongs to str — converts text to uppercase
(50).bit_length()  # .bit_length() belongs to int — returns the number of bits needed to represent the number

print(text.upper())
print(number.bit_length())


# PYTHON CHALLENGE — 5 Variables with Different Data Types

age = int(input("Enter your age: "))        # int   — converting input from str to int using int()
height = float(input("Enter your height: ")) # float — converting input from str to float using float()
name = input("Enter your name: ")            # str   — input() always returns a string by default
student = True                               # bool  — True means yes, they are a student
rollNumber = None                            # NoneType — no value assigned yet

# Printing values, data types, and lengths of all variables
print(f"\nName       : {name}        | Type: {type(name)}  | Length: {len(name)}")
print(f"Age        : {age}          | Type: {type(age)}   | Bits: {age.bit_length()}")
print(f"Height     : {height}       | Type: {type(height)} | Length: {len(str(height))}")
print(f"Student    : {student}      | Type: {type(student)} | Length: {len(str(student))}")
print(f"Roll Number: {rollNumber}   | Type: {type(rollNumber)} | Length: N/A — None has no length")