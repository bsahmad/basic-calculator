def show_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def calculator():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Cannot divide by zero.")

calculator()
