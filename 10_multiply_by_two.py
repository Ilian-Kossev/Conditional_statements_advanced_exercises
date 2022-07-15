number = float(input())
while number:
    num = float(number)
    if num >= 0:
        result = num * 2
        print(f"Result: {result:.2f}")
    else:
        print("Negative number!")
        break
    number = input()
