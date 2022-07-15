season = input()
km = float(input())
price_per_km = 0
if km <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.9
    elif season == "Winter":
        price_per_km = 1.05
elif 5000 < km <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.1
    elif season == "Winter":
        price_per_km = 1.25
else:
    price_per_km = 1.45
salary_before_taxes = km * price_per_km * 4
salary_after_taxes = salary_before_taxes * 0.9
print(f"{salary_after_taxes:.2f}")