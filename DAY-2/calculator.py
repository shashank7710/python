#simple calculator 
# which can perform basic operations like addition, subtraction, multiplication and division.


num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':   
    result = num1 - num2
elif operator == '*':   
    result = num1 * num2
elif operator == '/':  
    if num2 == 0:
            result = "Error: Division by zero is not allowed."
                      
    else:
        result = num1 / num2    
else:
    result = "Invalid operator. Please use +, -, *, or /."
    
print(f"Result: {result}")