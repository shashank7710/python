
# operator is a symbol or keyword that tells the compiler to perform specific mathematical or logical manipulations. Python divides the operators in the following groups:
# Arithmetic operators : +, -, *, /, %, **,//
# assignment operators : =, +=, -=, *=, /=, %=, **=
# Comparison operators : ==, !=, <, >, <=, >=
# Logical operators : and, or, not
# identity operators : is, is not
# membership operators : in, not in
# Bitwise operators : &(and), |(or), ^(xor), ~(not), <<(left shift), >>(right shift)

#arithmetic operators

a = 20
b = 10
print(a + b)  # Output: 30
print(a - b)  # Output: 10
print(a * b)  # Output: 200
print(a / b)  # Output: 2.0
print(a % b)  # Output: 0
print(a ** b)  # Output: 10240000000000
print(a // b)  # Output: 2

#assignment operators

x = 5
x += 3  # equivalent to x = x + 3   
print(x)  # Output: 8
x -= 2  # equivalent to x = x - 2
print(x)  # Output: 6
x *= 4  # equivalent to x = x * 4
print(x)  # Output: 24
x /= 3  # equivalent to x = x / 3
print(x)  # Output: 8.0
x %= 5  # equivalent to x = x % 5
print(x)  # Output: 3.0
x **= 2  # equivalent to x = x ** 2
print(x)  # Output: 9.0 


#comparison operators
x = 10
y = 20
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x < y)   # Output: True
print(x > y)   # Output: False
print(x <= y)  # Output: True
print(x >= y)  # Output: False

#logical operators

a = True
b = False
print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False
print(not b)    # Output: True
print(a and not b)  # Output: True
print(not a or b)   # Output: False
print((a and b) or (not a))  # Output: False
print((a or b) and (not b))  # Output: True
print((a and not b) or (not a and b))  # Output: True

age =  25
salary = 50000
print(age > 18 and salary > 30000)  # Output: True

#identity operators

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # Output: False
print(a is not b)  # Output: True

x = 7
y = 7
print(x is y)  # Output: True  reason: Python caches small integers, so x and y point to the same object in memory. 


#membership operators

list1 = [1, 2, 3, 4, 5]
print(3 in list1)  # Output: True
print(6 not in list1)  # Output: True 

#bitwise operators

x = 5  # Binary: 101
y = 3  # Binary: 011
print(x & y)  # Output: 1  (Binary: 001)
print(x | y)  # Output: 7  (Binary: 111)
print(x ^ y)  # Output: 6  (Binary: 110)
print(~x)     # Output: -6 (Binary: ...11010)
print(x << 1) # Output: 10 (Binary: 1010)
print(x >> 1) # Output: 2  (Binary: 010)