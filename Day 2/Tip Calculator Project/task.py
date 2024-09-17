print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

#### My approach ####

# #1. To test, try to print the bill and tip together
# bill_tip_merged = (bill + (bill * tip) / 100)
# print(round(bill_tip_merged), 2)
# print("$",round(bill_tip_merged, 2))

#2. Include the calculation to pay each person
pay_per_person = round(((bill + (bill * tip) / 100) / people), 2)
print(f"Each person should pay: ${pay_per_person}")

# #### Angela's approach ####
# tip_as_percent = tip / 100  ## this will give result ex 0.2 etc
# total_tip_amount = bill * tip_as_percent  # bill * percent
# total_bill = bill + total_tip_amount  # the bill + tip
# bill_per_person = total_bill / people  # division per person
# final_bill = round(bill_per_person, 2)
#
# print(f"Each person should pay ${final_bill}")
