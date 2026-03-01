# data types

# int -5 , 12 , 10000
# float 3.15 , 0.5 ,100.2
# complex 2+3i


# Types type() , int() , float(), complex()

from math import ceil, floor, trunc


x = "10"
y = 5.7
z = 2 + 3j
xint = 10
xfloat = 10.221
print(type(x))
print(type(y))
print(type(z))


print(x*3)
x = int(x)
print(x)


float(xfloat)


print("-----------------------------")

print(2+3)
print(5-3)
print(4*3)
print(7/2)
print(7//2)
print(9 % 2)
print(2 ** 3)


# Rounding
print("-----------------------------")

print(abs(2-20))
print(floor(1.9))
print(ceil(1.1))
print(round(1.232))
print(trunc(292.3))