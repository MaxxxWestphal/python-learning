principal = float(input("Principal: "))
rate = float(input("Rate (%): "))
years = int(input("Years: "))

balance = principal

for year in range(1, years + 1):
    balance = balance * (1 + rate / 100)
    print(f"Year {year}: ${balance:.2f}")

total_interest = balance - principal
print(f"Total interest earned: ${total_interest:.2f}")






def caesar_encode (text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                base = ord('A')
                new_char = chr((ord(ch) - base + shift) % 26 + base)
            else:
                base = ord('a')
                new_char = chr((ord(ch) - base + shift) % 26 + base)

            result += new_char
        else:
            result += ch

    return result
print(caesar_encode("Hello, World!", 3))   
print(caesar_encode("abc xyz", 2))          
print(caesar_encode("Python 3", 5))  







def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        result.append(new_row)

    return result
m1 = [[1, 2, 3],
      [4, 5, 6]]
print(transpose(m1))

m2 = [[1, 2],
      [3, 4],
      [5, 6]]
print(transpose(m2))








def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != " ":
            return board[0][c]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    for row in board:
        if " " in row:
            return "Ongoing"

    return "Draw"
board1 = [["X", "X", "X"],
["O", "O", " "],
[" ", " ", " "]]
print(check_winner(board1))   
board2 = [["X", "O", "X"],
["X", "O", " "],
[" ", "O", "X"]]
print(check_winner(board2))   
board3 = [["X", "O", "X"],
["X", "O", "O"],
["O", "X", "X"]]
print(check_winner(board3))   
board4 = [["X", "O", " "],
[" ", "X", " "],
[" ", " ", " "]]
print(check_winner(board4)) 







def expense_tracker():
    descriptions = []
    amounts = []

    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. Total spent")
        print("4. Largest expense")
        print("5. Remove expense (by number)")
        print("6. Quit")

        choice = input("Choice: ")

        if choice == "1":
            desc = input("Description: ")
            try:
                amt = float(input("Amount: "))
                if amt < 0:
                    print("Amount must be ≥ 0.")
                    continue
            except ValueError:
                print("Invalid amount.")
                continue

            descriptions.append(desc)
            amounts.append(amt)

        elif choice == "2":
            if not descriptions:
                print("No expenses recorded.")
            else:
                for i in range(len(descriptions)):
                    print(f"{i+1}. {descriptions[i]}: ${amounts[i]:.2f}")

        elif choice == "3":
            total = sum(amounts)
            print(f"Total: ${total:.2f}")

        elif choice == "4":
            if not descriptions:
                print("No expenses to compare.")
            else:
                max_index = amounts.index(max(amounts))
                print(f"Largest: {descriptions[max_index]} (${amounts[max_index]:.2f})")

        elif choice == "5":
            if not descriptions:
                print("No expenses recorded.")
                continue

            try:
                num = int(input("Expense number to remove: "))
            except ValueError:
                print("Invalid number.")
                continue

            if 1 <= num <= len(descriptions):
                descriptions.pop(num - 1)
                amounts.pop(num - 1)
            else:
                print("Invalid number.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
            expense_tracker() 
