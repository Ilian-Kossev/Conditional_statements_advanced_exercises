number_chrysanthemum = int(input())
number_roses = int(input())
number_tulips = int(input())
season = input()
holiday = input()
total_flowers = number_roses + number_tulips + number_chrysanthemum
price_chrysanthemum = 0
price_roses = 0
price_tulips = 0
if season ==  "Spring" or season == "Summer":
    price_chrysanthemum = 2
    price_roses = 4.10
    price_tulips = 2.50
elif season == "Autumn" or season == "Winter":
    price_chrysanthemum = 3.75
    price_roses = 4.50
    price_tulips = 4.15
if holiday == "Y":
    price_chrysanthemum *= 1.15
    price_roses *= 1.15
    price_tulips *= 1.15
bouquet_price = number_chrysanthemum * price_chrysanthemum + number_roses * price_roses + number_tulips * price_tulips
if season == "Spring" and number_tulips > 7:
    bouquet_price *= 0.95
elif season == "Winter" and number_roses >= 10:
    bouquet_price *= 0.9
if total_flowers > 20:
    bouquet_price *= 0.8
final_bouquet_price = bouquet_price + 2
print(f"{final_bouquet_price:.2f}")







