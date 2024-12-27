## Input we need from the user
    # Total rent 
    # Total food ordered for snacking 
    # Electricity Units Spend
    # Charge per Unit 
    # Persons living in room/flat

## Output
    # Total amount you've to pay 

rent = int(input("Enter the hostel/flat rent :₹ "))
food = int(input("Enter the amount of food ordered :₹ "))
electricity_spend = int(input("Enter the total of electricity spend :₹ "))
charge_per_unit = int(input("Enter the charge per units :₹ "))
persons = int(input("Enter the number of persons livining in room/flat :₹ "))

total_electricity = electricity_spend * charge_per_unit

output = (rent + food + total_electricity) // persons

print(f"Each person will pay : ₹{output}") 
