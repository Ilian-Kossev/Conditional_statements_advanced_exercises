number_of_junior_bikers = int(input())
number_of_senior_bikers = int(input())
race_trail = input()
total_number_of_bikers = number_of_senior_bikers + number_of_junior_bikers
tax_juniors = 0
tax_seniors = 0
if race_trail == "trail":
    tax_juniors = 5.50
    tax_seniors = 7
elif race_trail == "cross-country":
    tax_juniors = 8
    tax_seniors = 9.50
elif race_trail == "downhill":
    tax_juniors = 12.25
    tax_seniors = 13.75
elif race_trail == "road":
    tax_juniors = 20
    tax_seniors = 21.50
total_income = tax_juniors * number_of_junior_bikers + tax_seniors * number_of_senior_bikers
if total_number_of_bikers >= 50 and race_trail == "cross-country":
    total_income *= 0.75
final_income = total_income * 0.95
print(f"{final_income:.2f}")


