#shopping : if the total cost of items purchased is greater than or equal to 3000, apply a 10% discount and print the total cost after discount. Otherwise, print the total cost without any discount.


price = 1000
quantity = 3
total_cost = price * quantity
if total_cost >= 3000:
    discount = total_cost * 0.1  # 10% discount
    total_cost -= discount
    print(f"Total cost after discount: {total_cost}")
else:
    print(f"Total cost: {total_cost}")
