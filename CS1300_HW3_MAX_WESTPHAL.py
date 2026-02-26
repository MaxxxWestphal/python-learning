a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

print()

expr1 = a < b < c
expr2 = not (a > b or b > c)
expr3 = a <= b and b <= c

print("a < b < c                  :", expr1)
print("not (a > b or b > c)       :", expr2)
print("a <= b and b <= c          :", expr3)
print()






temp = int(input("Enter the current temperature (°F): "))
rain_input = input("Is it raining? (yes/no): ").strip().lower()

raining = (rain_input == "yes")

print()

if temp > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")
    
elif temp > 85:
    if raining:
        print("Warm rain — watch for flash floods.")
    else:
        print("Hot and dry — stay hydrated.")

elif temp >= 60:
    if raining:
        print("Grab an umbrella!")
    else:
        print("Nice weather — enjoy your day!")

elif temp >= 32:
    print("It's cold — bundle up!")

else:
    print("FREEZE WARNING: Roads may be icy!")







name = input("Enter student name: ")
exam1 = float(input("Enter Exam 1 score: "))
exam2 = float(input("Enter Exam 2 score: "))
exam3 = float(input("Enter Exam 3 score: "))

avg = (exam1 + exam2 + exam3) / 3

if avg >= 90:
    grade = "A"
elif avg >= 87:
    grade = "A-"
elif avg >= 83:
    grade = "B+"
elif avg >= 80:
    grade = "B"
elif avg >= 77:
    grade = "B-"
elif avg >= 73:
    grade = "C+"
elif avg >= 70:
    grade = "C"
elif avg >= 67:
    grade = "C-"
elif avg >= 63:
    grade = "D+"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

if avg >= 90:
    status = "Dean's List"
elif avg >= 70:
    status = "Good Standing"
elif avg >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

print("\n=============================")
print("STUDENT GRADE REPORT")
print("=============================")
print(f"Student: {name}")
print(f"Exam 1: {exam1}")
print(f"Exam 2: {exam2}")
print(f"Exam 3: {exam3}")
print("-----------------------------")
print(f"Average: {avg:.2f}")
print(f"Grade: {grade}")
print(f"Status: {status}")
print("=============================")

