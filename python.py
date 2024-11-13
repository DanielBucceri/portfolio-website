maxNum = int(input("Enter the total value: "))
counter = 0
base = 2000

# Perform an action until counter matches total
while counter < maxNum:
    leverage = 0
    gain = 0
    leverage = base * 5
    gain = leverage * 0.05
    base = base + gain

    counter += 1
    print(base)

print("The counter has reached the total.")
