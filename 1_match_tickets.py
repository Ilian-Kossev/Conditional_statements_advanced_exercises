budget = float(input())
ticket_type = input()
number_of_people = int(input())
transport_cost = 0
needed_money = budget * transport_cost
if number_of_people <= 4:
    transport_cost = budget * 0.75
elif 4 < number_of_people <= 9:
    transport_cost = budget * 0.60
elif 9 < number_of_people <= 24:
    transport_cost = budget * 0.50
elif 24 < number_of_people <= 49:
    transport_cost = budget * 0.40
elif number_of_people > 50:
    transport_cost = budget * 0.25
if ticket_type == "VIP":
    needed_money = number_of_people * 499.99
elif ticket_type == "Normal":
    needed_money = number_of_people * 249.99
money = budget - transport_cost
left_money = money - needed_money
missing_money = needed_money - money
if left_money >= 0:
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {missing_money:.2f} leva.")


