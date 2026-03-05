weight = float(input("Enter weight: "))

unit = input("Enter unit system (M/I): ").upper()

if unit == "M":
    height = float(input("Enter height (meters): "))
    bmi = weight / (height ** 2) 
    
elif unit == "I":
    height = float(input("Enter height (inches): "))
    bmi = (weight * 703) / (height ** 2)
    
else: 
    print("Invalid unit system.")
    exit()
    
print(f"BMI: {bmi:.1f}")
    
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category + "Overweight"
else:
    category = "Obese"
    
print("Category:", category)




password = input("Enter a password: ")

length_ok = len(password) >= 8
upper_ok = False
lower_ok = False
digit_ok = False
special_ok = False

for ch in password:
    if ch.isupper():
        upper_ok = True
    elif ch.islower():
        lower_ok = True
    elif ch.isdigit():
        digit_ok = True
    else:
        special_ok = True

criteria_met = 0
if length_ok:
    criteria_met += 1
if upper_ok:
    criteria_met += 1
if lower_ok:
    criteria_met += 1
if digit_ok:
    criteria_met += 1
if special_ok:
    criteria_met += 1

print("Length >= 8:", "PASS" if length_ok else "FAIL")
print("Uppercase:", "PASS" if upper_ok else "FAIL")
print("Lowercase:", "PASS" if lower_ok else "FAIL")
print("Digit:", "PASS" if digit_ok else "FAIL")
print("Special char:", "PASS" if special_ok else "FAIL")

print("Criteria met:", criteria_met, "/ 5")

if criteria_met == 5:
    rating = "Strong"
elif criteria_met >= 3:
    rating = "Moderate"
elif criteria_met >= 1:
    rating = "Weak"
else:
    rating = "No password entered"

print("Strength:", rating)



products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"]
quantities = [12, 45, 30, 8, 22]

print("=== INVENTORY ===")
for i in range(len(products)):
    print(f"{i+1}. {products[i]} - {quantities[i]}")
print("=================")

highest_index = 0
lowest_index = 0

for i in range(1, len(quantities)):
    if quantities[i] > quantities[highest_index]:
        highest_index = i
    if quantities[i] < quantities[lowest_index]:
        lowest_index = i

print(f"Highest: {products[highest_index]} ({quantities[highest_index]})")
print(f"Lowest: {products[lowest_index]} ({quantities[lowest_index]})")

total = 0
for q in quantities:
    total += q

average = total / len(quantities)

print(f"Total quantity: {total}")
print(f"Average quantity: {average:.2f}")

products.append("Webcam")
quantities.append(15)
print("\nAfter adding Webcam:")
for i in range(len(products)):
    print(products[i], "-", quantities[i])

products.insert(2, "USB Hub")
quantities.insert(2, 50)
print("\nAfter inserting USB Hub:")
for i in range(len(products)):
    print(products[i], "-", quantities[i])

index = products.index("Headset")
products.pop(index)
quantities.pop(index)

print("\nAfter removing Headset:")
for i in range(len(products)):
    print(products[i], "-", quantities[i])

removed_product = products.pop()
removed_quantity = quantities.pop()

print("\nRemoved last item:", removed_product, "-", removed_quantity)

print("\n=== FINAL INVENTORY ===")
for i in range(len(products)):
    print(f"{i+1}. {products[i]} - {quantities[i]}")

print("Inventory length:", len(products))




vehicle_type = input("Enter vehicle type (car/motorcycle/truck): ").strip().lower()
hours = float(input("Enter hours parked: "))
pass_holder = input("Monthly pass? (yes/no): ").strip().lower()

fee = 0.0

if pass_holder == "yes":
    fee = 0.0

elif vehicle_type == "motorcycle":
    if hours <= 2:
        fee = 1.0
    else:
        fee = 1.0 + 0.50 * (hours - 2)

elif vehicle_type == "car":
    if hours <= 2:
        fee = 3.0
    else:
        fee = 3.0 + 1.50 * (hours - 2)

elif vehicle_type == "truck":
    if hours <= 2:
        fee = 5.0
    else:
        fee = 5.0 + 2.50 * (hours - 2)

else:
    print("Invalid vehicle type.")
    quit()

print("\n--- Parking Receipt ---")
print("Vehicle:", vehicle_type.capitalize())
print(f"Duration: {hours:.2f} hours")
print("Pass holder:", "Yes" if pass_holder == "yes" else "No")
print(f"Fee: ${fee:.2f}")
print("-----------------------")
