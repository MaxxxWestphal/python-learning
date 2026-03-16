age = int(input("Enter your age: "))
show = input("Is this a matinee showing? (yes/no): ")

is_matinee = True if show.lower() == "yes" else False

if age < 0:
    print("Error: Age cannot be negative.")
else:
    if age < 13:
        age_group = "Child"
        price = 6.00 if is_matinee else 8.00

    elif age <= 17:
        age_group = "Teen"
        price = 7.00 if is_matinee else 10.00

    elif age <= 64:
        age_group = "Adult"
        price = 8.00 if is_matinee else 13.00

    else:
        age_group = "Senior"
        price = 6.00 if is_matinee else 7.00

    print(f"\nAge group: {age_group}")
    print(f"Ticket price: ${price:.2f}")




student_id = input("Enter student ID: ")
name = input("Enter full name: ")
age_input = input("Enter age: ")
major = input("Enter major: ")

errors = []

if len(student_id) != 8:
    errors.append(f"Student ID must be exactly 8 characters (got {len(student_id)})")

if not student_id[:1].isalpha():
    errors.append("Student ID must start with a letter")

if len(student_id) == 8 and not student_id[1:].isdigit():
    errors.append("Student ID must have 7 digits after the first letter")

clean_name = name.strip()
if len(clean_name) < 2:
    errors.append("Name cannot be empty and must be at least 2 characters")

try:
    age = int(age_input)
    if age < 16 or age > 99:
        errors.append("Age must be between 16 and 99")
except:
    errors.append("Age must be a valid integer")

valid_majors = ["CS", "IT", "CE", "DS"]
if major.upper() not in valid_majors:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major})")

if errors:
    print("\n Profile has errors:")
    for e in errors:
        print("-", e)
else:
    print("\n Profile created successfully!")
    print(f"  Student ID: {student_id}")
    print(f"  Name: {clean_name}")
    print(f"  Age: {age}")
    print(f"  Major: {major.upper()}")








print("=" * 30)
print("CAMPUS CAFÉ ORDER SYSTEM")
print("=" * 30)
print("1. Coffee   - $3.50")
print("2. Sandwich - $6.00")
print("3. Salad    - $5.50")
print("4. Combo    - $8.00")
print("5. Exit")
print("=" * 30)

choice = input("Enter your choice (1-5): ")
item_name = ""
unit_price = 0.0

if choice == "1":  
    size = input("Choose size (Small/Medium/Large): ").lower()
    if size == "medium":
        unit_price = 4.50
        item_name = "Coffee (Medium)"
    elif size == "large":
        unit_price = 5.50
        item_name = "Coffee (Large)"
    elif size == "small":
        unit_price = 3.50
        item_name = "Coffee (Small)"
    else:
        unit_price = 3.50
        item_name = "Coffee (Small)"
        print("Invalid size. Defaulting to Small.")

elif choice == "2":  
    cheese = input("Add cheese? (yes/no): ").lower()
    unit_price = 6.00
    item_name = "Sandwich"
    if cheese == "yes":
        unit_price += 0.75
        item_name += " + Cheese"

elif choice == "3":  
    dressing = input("Choose dressing (ranch/italian/vinaigrette/none): ").lower()
    valid_dressings = ["ranch", "italian", "vinaigrette", "none"]
    if dressing in valid_dressings:
        item_name = f"Salad ({dressing.capitalize()})"
    else:
        item_name = "Salad (None)"
        print("Invalid dressing. Defaulting to none.")
    unit_price = 5.50

elif choice == "4":  
    size = input("Choose coffee size (Small/Medium/Large): ").lower()
    cheese = input("Add cheese to sandwich? (yes/no): ").lower()
    unit_price = 8.00
    item_name = "Combo"

    if size == "medium":
        unit_price += 1.00
        item_name += " + Medium Coffee"
    elif size == "large":
        unit_price += 2.00
        item_name += " + Large Coffee"
    elif size == "small":
        item_name += " + Small Coffee"
    else:
        item_name += " + Small Coffee"
        print("Invalid coffee size. Defaulting to Small.")

    if cheese == "yes":
        unit_price += 0.75
        item_name += " + Cheese"

elif choice == "5":
    print("Thank you! Goodbye.")
    exit()

else:
    print("Invalid choice. Exiting.")
    exit()

name = input("Enter your name: ").strip()
while not name:
    name = input("Name cannot be empty. Enter your name: ").strip()

try:
    quantity = int(input("How many? "))
    if quantity <= 0:
        raise ValueError
except:
    print("Invalid quantity. Must be a positive integer.")
    exit()

subtotal = unit_price * quantity
tax = round(subtotal * 0.07, 2)
total = round(subtotal + tax, 2)

print("\n" + "=" * 30)
print("ORDER RECEIPT")
print("=" * 30)
print(f"Customer: {name}")
print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("=" * 30)
print("Thank you for your order!")

