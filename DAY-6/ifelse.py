#conditional statements
#executes or works based on condition

#if, elif, else 

#1.if statement

#if means execute the code only when conditions 


#online shopping
#is the product available 
#login with account
#is payment done? 

current_balance = 10000
pin = 1234
card_num = 123456789
cardnum=int(input("enter card number: "))
if cardnum == card_num:
    entered_pin = int(input("enter 4 digit pin: "))

    if entered_pin!=pin:
        print("invalid pin")
    else:
        print("1.check balance")
        print("2.withdraw")
else:
    print("invalid card number")
a=int(input("enter your choice:  "))
if a==1:
    print(current_balance)
elif a==2:
    amount=int(input("enter the amount: "))
    if amount <= 0:
        print("enter vaild amount")
    elif amount >= current_balance:
        print("insufficient balance")
    else:
        current_balance -= amount
        print("cash is withdrawed")
        print(f'your current balance : {current_balance}')

