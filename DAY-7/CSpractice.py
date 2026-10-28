# #identify number is positive or negative

# num = int(input("Enter a number: "))
# if num > 0:
#     print("number is positive")
# elif num == 0:
#     print("zero")
# else:
#     print("number is negative")
    
# #identify number is odd or even

# num1 = int(input("Enter a number: "))
# if num1 % 2 == 0:
#     print("number is even")
# elif num1 % 2 !=0:
#     print("number is odd")
# else:
#     print("invalid number or zero")

# #largest of two numbers

# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# if num2 > num3:
#     print(f'{num2} is greater')
# else:
#     print(f'{num3} is greater')


# #largest of three numbers
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# c = int(input("Enter a number: "))
# if a > b and a > c:
#     print("a is greater")
# elif b > a and b > c:
#     print("b is greater")
# elif c > a and c > b:
#     print("c is greater")
# elif a==b and a>c:
#     print("a and b are greater")
# elif b==c and b>a:
#     print("b and c are greater")
# elif a==c and a>b:
#     print("number3 and c are greater")
# else:
#     print("all are equal")


#college admission

# marks = int(input("Enter your marks: "))
# entrance = input("did you pass your entrance exam? (yes/no): ")

# if marks >= 60 and entrance == "yes":
#     print("----Eligible for admission----")
# else:
#     print(f'not eligilbe')

#driving eligibility
# age = int(input("enter your age: "))
# if age >=18:
#     d_license = input("uh have driving license? (yes/no): ")
#     if d_license == "yes":
#         print("you can drive")
#     else:
#         print("driving license is required")
# else:
#     print("you are not eligible to drive")

#movie pricising
age = int(input("enter your age: "))
if age <= 5:
    print("free")
elif age >= 60 :
    print("amount: 120")
else:
    print("amount: 200")

#leap year
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
    
num = int()