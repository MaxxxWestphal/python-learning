months = [ 
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

for month in months:
    print(month)
    
    
    
    
    
import random
roll = 0
while roll != 6:
    roll = random.randint(1, 6)
    print("You rolled:", roll)
    
    
    
    
for n in range(1, 11):
    print(n * n)
    
    
    
    
user_input = ""
while user_input != "quit":
    user_input = input("Type something (or 'quit' to stop): ")
    
    
    
    
    
    num = 1
while num <= 5:      
    print(num)
    num += 1     
    
    
    
    
    
i = 0               
while i < 5:       
    print(i)
    i += 1         
    
    
    
    
    
    
    
#while score < 100
#while answer != "yes"
#while health > 0 and game_over == False
    
    


num = 2
while num < 10:
    print(num)
    num += 2
#prints 2,4,6,8

num = 2
while num <= 10:
    print(num)
    num += 2
#prints 2,4,6,8,10




value = 1
count = 0
while value <= 1000:
    print(value)
    value *= 2
    count += 1
print("It took", count, "doublings to exceed 1000.")





word = "education"
for char in word:
    if char in "aeiou":
        print(char)

num = None
while num != 0:
    num = int(input("Enter a number (0 to stop): "))
    
    

i = 10
while i > 0:
    print(i)
    i -= 1

#The while loop works, but the for loop is clearer because range(10, 0, -1)
#directly expresses the countdown. The for version is better for readability.

value = 1
while value < 1000:
    value *= 2
    print(value)
    
#It cannot be converted to a for loop in a meaningful way because the number
#of iterations is not known ahead of time. The loop depends on value doubling
#each time, so only a while loop makes sense here.




choice = 0
while choice != 3:
    print("Menu:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)
    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)
    elif choice == 3:
        print("Goodbye!")
    else:
        print("Invalid choice. Try again.")
