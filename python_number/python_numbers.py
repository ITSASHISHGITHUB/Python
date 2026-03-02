# NUMBERS IN PYTHON


# NUMBER TYPES

import random
import math
# int   — whole numbers, no decimal point (positive or negative)
a = 10
b = 3.14        # float — numbers with a decimal point
# complex — numbers with a real and imaginary part (rarely used in general programming)
c = 2 + 3j

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>


# ARITHMETIC OPERATORS

x = 10
y = 3

print(x + y)   # Output: 13   — addition
print(x - y)   # Output: 7    — subtraction
print(x * y)   # Output: 30   — multiplication
print(x / y)   # Output: 3.333... — division (always returns a float)
print(x // y)  # Output: 3    — floor division (rounds DOWN to nearest whole number)
print(x % y)   # Output: 1    — modulus (returns the remainder after division)
print(x ** y)  # Output: 1000 — exponentiation (10 to the power of 3)

# Note: / always returns a float even if the result is a whole number
print(10 / 2)  # Output: 5.0  ← float, not int
print(10 // 2)  # Output: 5    ← int, use // when you want a whole number result


# OPERATOR PRECEDENCE (BODMAS / PEMDAS)
# Python follows standard math order:
# 1. Brackets ()
# 2. Exponents **
# 3. Multiplication *, Division /, Floor //, Modulus %
# 4. Addition +, Subtraction -

print(2 + 3 * 4)      # Output: 14  — * runs before +
print((2 + 3) * 4)    # Output: 20  — () forces + to run first
print(2 ** 3 + 1)     # Output: 9   — ** runs before +
print(10 - 4 // 3)    # Output: 9   — // runs before -


# TYPE CONVERSION (CASTING)
# converting between int and float

print(int(3.9))    # Output: 3   — int() cuts off the decimal, does NOT round
print(int(3.1))    # Output: 3   — same behaviour regardless of decimal value
print(float(5))    # Output: 5.0 — float() adds a decimal point

# converting string to number — useful when working with input()
age = "25"
print(age + 5)          # ❌ TypeError — cannot add str and int
print(int(age) + 5)     # ✅ Output: 30 — convert to int first

height = "5.9"
print(float(height))    # Output: 5.9 — use float() for decimal strings, not int()
# print(int(height))    # ❌ ValueError — int() cannot convert a decimal string directly


# AUGMENTED ASSIGNMENT OPERATORS
# shorthand for updating a variable's value in place

score = 100
score += 10   # same as: score = score + 10 → 110
score -= 5    # same as: score = score - 5  → 105
score *= 2    # same as: score = score * 2  → 210
score /= 3    # same as: score = score / 3  → 70.0
score //= 2   # same as: score = score // 2 → 35.0
score %= 4    # same as: score = score % 4  → 3.0
score **= 3   # same as: score = score ** 3 → 27.0

print(score)  # Output: 27.0


# ROUNDING & PRECISION

print(round(3.14159))     # Output: 3      — rounds to nearest whole number
print(round(3.14159, 2))  # Output: 3.14   — rounds to 2 decimal places
print(round(3.14159, 4))  # Output: 3.1416 — rounds to 4 decimal places

# Output: 2 — Python uses "banker's rounding" (rounds to nearest even number)
print(round(2.5))
print(round(3.5))  # Output: 4 — 3.5 rounds up to 4 (nearest even)

# abs() returns the absolute value — removes any negative sign
print(abs(-45))    # Output: 45
print(abs(45))     # Output: 45


# THE MATH MODULE
# for more advanced mathematical operations, import the math module


print(math.sqrt(25))       # Output: 5.0    — square root (always returns float)
print(math.ceil(3.1))      # Output: 4      — rounds UP to nearest whole number
print(math.floor(3.9))     # Output: 3      — rounds DOWN to nearest whole number
print(math.pi)             # Output: 3.14159... — the value of π
# Output: 1024.0 — same as 2**10 but always returns float
print(math.pow(2, 10))
print(math.factorial(5))   # Output: 120    — 5! = 5 × 4 × 3 × 2 × 1
print(math.log(100, 10))   # Output: 2.0    — log base 10 of 100

# math.ceil vs math.floor vs round
# math.ceil  → always rounds UP   → ceil(3.1)  = 4
# math.floor → always rounds DOWN → floor(3.9) = 3
# round()    → rounds to nearest  → round(3.5) = 4


# COMPARISON OPERATORS
# these return True or False (bool)

a = 10
b = 20

print(a == b)   # Output: False — equal to
print(a != b)   # Output: True  — not equal to
print(a > b)    # Output: False — greater than
print(a < b)    # Output: True  — less than
print(a >= b)   # Output: False — greater than or equal to
print(a <= b)   # Output: True  — less than or equal to


# PRACTICAL: WORKING WITH input() AND NUMBERS
# input() always returns a string — always convert before doing math

price = float(input("Enter price: "))     # float for prices with decimals
quantity = int(input("Enter quantity: "))  # int for whole number quantities

total = price * quantity
tax = total * 0.18                         # 18% tax
grand_total = total + tax

print(f"Price     : ₹{price}")
print(f"Quantity  : {quantity}")
print(f"Total     : ₹{round(total, 2)}")
print(f"Tax (18%) : ₹{round(tax, 2)}")
print(f"Grand Total: ₹{round(grand_total, 2)}")


# COMMON MISTAKES

# 1. division always gives a float
print(type(10 / 2))   # <class 'float'> — use // if you need an int

# 2. int() truncates, it does NOT round
print(int(9.99))      # Output: 9, not 10 — use round() if you want rounding

# 3. floating point precision — floats are not always exact in memory
# Output: 0.30000000000000004 — a known quirk of floats in all programming languages
print(0.1 + 0.2)
# Output: 0.3 — use round() to clean up float results
print(round(0.1 + 0.2, 2))


# Random

print(random.random())
print(random.randint(1, 6))
