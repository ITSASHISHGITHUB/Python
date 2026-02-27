# STRING METHODS & OPERATIONS

name = "ashish"
print(type(name))  # <class 'str'>

age = 25
print(type(age))   # <class 'int'>

print(age + 5)           # int + int = int → arithmetic addition → Output: 30
# str() converts int to string for concatenation
print("your age is: " + str(age))

age = age + 5  # age is now 30
age = str(age)  # converts the int 30 to the string "30"

print(type(age))  # <class 'str'>
# age = age + 5   # ❌ this would now crash — you cannot add a number to a string


# LENGTH

password = "   123ashish"
print(len(password))  # len() counts every character including spaces → Output: 12


# COUNT

text = """ashish
Ashish yadav
ashish is
frontend developer in company name ashish
"""

print(text.count("ashish"))  # Output: 3 — counts exact matches only
# Output: 1 — Python is case-sensitive, "Ashish" ≠ "ashish"
print(text.count("Ashish"))


# REPLACE
# .replace(old, new) — finds every occurrence of 'old' and swaps it with 'new'
# the original string is NOT changed — a new string is returned

price = "123,2323"
print(price.replace(",", "."))  # Output: 123.2323

phone = "29-23-23-23-32-32"
print(phone.replace("-", ""))   # removes all dashes → Output: 292323233232
# replaces dashes with spaces → Output: 29 23 23 23 32 32
print(phone.replace("-", " "))

# .replace() can be chained — each replacement runs on the result of the previous one
print(phone.replace("2", "3").replace("9", "0"))


# CONCATENATION
# joining strings together using the + operator

first_name = "ashish"
last_name = "yadav"
# " " adds a space between the two names
full_name = first_name + " " + last_name
print(full_name)  # Output: ashish yadav


# F-STRINGS
# f-strings let you embed variables and expressions directly inside a string using {}
# cleaner and more readable than using + and str() for concatenation

name = "ashish"
age = 32
isStudent = True

# old way — messy, requires manual str() conversion
print("My name is " + name + ", I am " + str(age) +
      " years old, and student status is " + str(isStudent))

# f-string way — clean and readable, no str() needed
print(
    f"My name is {name}, I am {age} years old and student status is {isStudent}")

# expressions inside {} are evaluated → Output: 2+4 = 6
print(f"2+4 = {2+4}")

# print(f{this is my name}) # ❌ f-string must have quotes around it

# {{ and }} print literal curly braces → Output: {ashish}
print(f"{{ashish}}")


# SPLIT
# .split(separator) — breaks a string into a list at every occurrence of the separator

stamp = "12-12-2002 12:32"
print(stamp.split("-"))       # Output: ['12', '12', '2002 12:32']

csv_file = "21213,ashish,asjs,232,32"
# Output: ['21213', 'ashish', 'asjs', '232', '32']
print(csv_file.split(","))


# STRING REPETITION
# str * number — repeats the string that many times

print("ha" * 3)  # Output: hahaha


# INDEXING
# each character in a string has a position called an index
# positive index starts from 0 (left to right)
# negative index starts from -1 (right to left)

string = "hello"
#          h  e  l  l  o
# pos:      0  1  2  3  4
# neg:     -5 -4 -3 -2 -1

print(string[0])   # Output: h  (first character)
print(string[-1])  # Output: o  (last character)


# SLICING
# string[start:end] — extracts a portion of the string
# start is INCLUDED, end is NOT included

print(string[1:4])   # Output: ell  (index 1, 2, 3 — stops before 4)
print(string[:3])    # Output: hel  (from beginning up to index 3)
print(string[2:])    # Output: llo  (from index 2 to the end)

# SLICING WITH STEP
# string[start:end:step] — step controls how many characters to jump each time
# default step is 1 (every character)

print(string[0:5:1])  # Output: hello  (every character)
print(string[0:5:2])  # Output: hlo    (every 2nd character — index 0, 2, 4)
print(string[0:4:3])  # Output: hl     (every 3rd character — index 0, 3)
print(string[::2])    # Output: hlo    (full string, every 2nd character)
print(string[::-1])   # Output: olleh  (step -1 reverses the entire string)


# WHITESPACE CLEANING

text = "  Engineering".lstrip()    # lstrip() removes spaces from the LEFT only
print(text)                         # Output: Engineering

text = "Engineering  ".rstrip()    # rstrip() removes spaces from the RIGHT only
print(text)                         # Output: Engineering

text = "     Engineering".strip()  # strip() removes spaces from BOTH sides
print(text)                         # Output: Engineering

text = "Data  Engineering".strip()  # strip() does NOT remove spaces in the middle
print(text)                         # Output: Data  Engineering

# you can pass a character to strip instead of spaces
text = "###Engineering###".strip("#")
print(text)                             # Output: Engineering

text = "  Engineering"
print(len(text))          # Output: 13 — includes the leading spaces
print(len(text.strip()))  # Output: 11 — spaces removed before counting

# Output: 2 — number of stripped characters
print(len(text) - len(text.strip()))


# CASE CONVERSIONS

text = "python PROGRAMMING"
print(text.upper())  # Output: PYTHON PROGRAMMING — every character uppercase
print(text.lower())  # Output: python programming — every character lowercase


# STRING COMPARISON

search = "Email"
data = "email"

# Output: False — "Email" ≠ "email", Python is case-sensitive
print(search == data)

# → "email"  (.lower() first, then .strip() removes the space)
search = "Email ".lower().strip()
data = "email".lower().strip()     # → "email"

print(search == data)  # Output: True — both are now "email"


# PRACTICAL PROBLEM — Extracting and cleaning data from a messy string

data = "960-Maria , (D@t@ Engineer) :: 27y  "

# slices "Maria" from index 4–8, then lowercases it
name = data[4:9].lower()
print(name)                            # Output: maria

# replaces @ with 'a' first, then slices and lowercases
role = data.replace("@", "a")[13:26].lower()
print(role)                                     # Output: data engineer

# removes "y" from "27y", slices from index 30, strips spaces
age = data.replace("y", "")[30:].strip()
print(age)                                  # Output: 27

print(f"name: {name} | role: {role} | age: {age}")


# SEARCH METHODS

# .startswith(value) — returns True if the string begins with the given value
# .endswith(value)   — returns True if the string ends with the given value
# in                 — returns True if the value exists anywhere inside the string

email = "support@gmail.com"

# Output: True  — string begins with "support"
print(email.startswith("support"))
# Output: False — string does NOT begin with "info"
print(email.startswith("info"))

print(email.endswith(".com"))       # Output: True  — string ends with ".com"
# Output: False — string does NOT end with ".org"
print(email.endswith(".org"))

# Output: True  — "gmail" exists somewhere in the string
print("gmail" in email)
# Output: False — "yahoo" does NOT exist in the string
print("yahoo" in email)

# practical use — these are commonly used in conditions (if statements)
# e.g. if email.endswith(".com"): → do something

text = "hello world"

print(text.find("o"))   # Output: 4
print(text.find("z"))   # Output: -1  (not found)

# index() throws error if not found
# print(text.index("z"))  # ❌ ValueError

phone1 = "+91-6360-431-631"
phone2 = "6360-431-631"

print(phone1[phone1.find("-")+1:]) 



print("123".isdigit())      # True
print("123a".isdigit())     # False

print("ashish".isalpha())   # True
print("ashish123".isalpha())# False

print("ashish123".isalnum())# True