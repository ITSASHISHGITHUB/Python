# ----------------------------------------
# any() and all() functions
# ----------------------------------------

# any() → Returns True if AT LEAST ONE value is True / non-empty

name = ""
phone = "312237"
username = ""

print(any([name, phone, username]))
# Output: True
# Reason: phone is not empty, so at least one value is True


# all() → Returns True ONLY if ALL values are True / non-empty

name = "as"
phone = "312237"
username = "a"

print(all([name, phone, username]))
# Output: True
# Reason: all values are non-empty, so all are True


# ----------------------------------------
# COMPARISON OPERATORS
# These return True or False (boolean)
# ----------------------------------------

a = 10
b = 20

print(a == b)   # False → Equal to
print(a != b)   # True  → Not equal to
print(a > b)    # False → Greater than
print(a < b)    # True  → Less than
print(a >= b)   # False → Greater than or equal to
print(a <= b)   # True  → Less than or equal to


# ----------------------------------------
# LOGICAL OPERATORS
# ----------------------------------------

# AND operator → Both conditions must be True

print(3 < 5 and 5 == 5)   # True  → Both are True
print(3 > 5 and 5 == 5)   # False → One is False, so result is False


# OR operator → At least one condition must be True

print(3 < 5 or 5 == 5)    # True  → Both are True
print(3 > 5 or 5 == 5)    # True  → One is True
print(3 > 5 or 5 != 5)    # False → Both are False


# NOT operator → Reverses the result (True → False, False → True)

print(not True)   # False
print(not False)  # True
print(not not False)


# Allow access only if the user is logged in
# or they are a guest
# biut they must not be banned

is_logged_in = True
is_guest = False
is_banned = True

print(is_logged_in or is_guest and not is_banned)

print('a' in 'datata')
print('a' not in 'datata')

# security check : ensure the domain is not banned

domain = "gmail.com"
banned_domains = ["spam.com",  "fake.org", "bot.net"]
print(domain not in banned_domains)


# make sure the email exists , and its not empty

email = None
print(email != None and email != "")

# use is instead of == when checking for None
