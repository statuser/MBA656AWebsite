name = input("Hello, what is your name?")
print("Hi, " + name)

dog_age = int(input("What is your dog's age?"))
human_equiv_age = dog_age * 7
print("Your dog is", human_equiv_age, "in human equivalent years.")

length = float(input("What is the length of your rectangle?"))
width = float(input("What is the width of your rectangle?"))
print("The area of your rectable is " + str(length * width) + ".")

income = float(input("Please enter your yearly income (do not include commas or the dollar sign):"))
thirty_percent_rate_amount = max(0, income - 150000)
twentyfive_percent_rate_amount = max(0, income - thirty_percent_rate_amount - 100000)
twenty_percent_rate_amount = max(0, income - thirty_percent_rate_amount
                                 - twentyfive_percent_rate_amount - 75000)
fifteen_percent_rate_amount = max(0, income - thirty_percent_rate_amount
                                  - twentyfive_percent_rate_amount
                                  - twenty_percent_rate_amount - 50000)
ten_percent_rate_amount = max(0, income - thirty_percent_rate_amount
                              - twentyfive_percent_rate_amount
                              - twenty_percent_rate_amount
                              - fifteen_percent_rate_amount - 20000)
zero_percent_rate_amount = max(0, income - thirty_percent_rate_amount
                               - twentyfive_percent_rate_amount
                               - twenty_percent_rate_amount
                               - fifteen_percent_rate_amount
                               - ten_percent_rate_amount - 20000)
total_tax = (.3 * thirty_percent_rate_amount
             + .25 * twentyfive_percent_rate_amount
             + .2 * twenty_percent_rate_amount
             + .15 * fifteen_percent_rate_amount
             + .1 * ten_percent_rate_amount
             + 0 * zero_percent_rate_amount)
tax_rate = total_tax / income
print("Your overall tax amount is: $" + str(total_tax))
print("This represents a tax_rate of: " + str(round(tax_rate * 100, 2)) + "%")

# Answers will vary
