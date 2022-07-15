season = input()
group_type = input()
number_students = int(input())
number_nights = int(input())
price = 0
sport = " "
if season == "Winter":
    if group_type == "boys":
        sport = "Judo"
    elif group_type == "girls":
        sport = "Gymnastics"
    elif group_type == "mixed":
        sport = "Ski"
    if group_type == "boys" or group_type == "girls":
        price = 9.60
        if 10 <= number_students < 20:
            price *= 0.95
        elif 20 <= number_students < 50:
            price *= 0.85
        elif number_students >= 50:
            price *= 0.5
    elif group_type == "mixed":
        price = 10
        if 10 <= number_students < 20:
            price *= 0.95
        elif 20 <= number_students < 50:
            price *= 0.85
        elif number_students >= 50:
            price *= 0.5
elif season == "Spring":
    if group_type == "boys":
        sport = "Tennis"
    elif group_type == "girls":
        sport = "Athletics"
    elif group_type == "mixed":
        sport = "Cycling"
    if group_type == "boys" or group_type == "girls":
        price = 7.20
        if 10 <= number_students < 20:
            price *= 0.95
        elif 20 <= number_students < 50:
            price *= 0.85
        elif number_students >= 50:
            price *= 0.5
    elif group_type == "mixed":
        price = 9.50
        if 10 <= number_students < 20:
            price *= 0.95
        elif 20 <= number_students < 50:
            price *= 0.85
        elif number_students >= 50:
            price *= 0.5
elif season == "Summer":
    if group_type == "boys":
        sport = "Football"
    elif group_type == "girls":
        sport = "Volleyball"
    elif group_type == "mixed":
        sport = "Swimming"
    if group_type == "boys" or group_type == "girls":
        price = 15
        if 10 <= number_students < 20:
            price *= 0.95
        elif 20 <= number_students < 50:
            price *= 0.85
        elif number_students >= 50:
            price *= 0.5
    elif group_type == "mixed":
        price = 20
        if 10 <= number_students < 20:
            price *= 0.95
        elif 20 <= number_students < 50:
            price *= 0.85
        elif number_students >= 50:
            price *= 0.5
total_price = price * number_nights * number_students
print(f"{sport} {total_price:.2f} lv.")

