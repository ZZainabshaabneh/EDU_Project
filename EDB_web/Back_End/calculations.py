def calculate():
    # Welcoming the user and asking for their name
    name = input("Welcome to Education without Borders! Please enter your name: ")
    print(f"\nWelcome, {name}!")

    # Asking the user if they want to perform calculations
    proceed = input(f"\nWould you like to perform calculations, {name}? (yes/no): ")


    # Prompting the user to select the operation
    print("\nSelect the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    operation_choice = int(input("Enter the number corresponding to the operation you want to perform: "))

    if operation_choice == 1:
        # Addition:
        print("\nExample:")
        print("1. Addition: If you have 3 apples and you buy 5 more, you have 3 + 5 = 8 apples.")
        Number_1 = int(input("\nEnter the first number: "))
        Number_2 = int(input("Enter the second number: "))
        print("\nAddition: We will add the first number to the second number.")
        addition_result = Number_1 + Number_2
        print(f"{Number_1} + {Number_2} = {addition_result}")
    elif operation_choice == 2:
        # Subtraction:
        print("\nExample:")
        print("2. Subtraction: If you have 8 apples and you eat 3, you have 8 - 3 = 5 apples left.")
        Number_1 = int(input("\nEnter the first number: "))
        Number_2 = int(input("Enter the second number: "))
        print("\nSubtraction: We will subtract the second number from the first number.")
        subtraction_result = Number_1 - Number_2
        print(f"{Number_1} - {Number_2} = {subtraction_result}")
    elif operation_choice == 3:
        # Multiplication:
        print("\nExample:")
        print("3. Multiplication: If you have 3 apples, and each apple costs $2, then the total cost is 3 * 2 = 6")
        Number_1 = int(input("\nEnter the first number: "))
        Number_2 = int(input("Enter the second number: "))
        print("\nMultiplication: We will multiply the first number by the second number.")
        multiplication_result = Number_1 * Number_2
        print(f"{Number_1} * {Number_2} = {multiplication_result}")
    elif operation_choice == 4:
        # Division :
        print("\nExample:")
        print(
            "4. Division: If you have 6 apples and you want to share them equally between 2 people, each person gets 6 / 2 = 3 apples")
        Number_1 = int(input("\nEnter the first number: "))
        Number_2 = int(input("Enter the second number: "))
        print("\nDivision: We will divide the first number by the second number.")
        if Number_2 != 0:
            division_result = Number_1 / Number_2
            print(f"{Number_1} / {Number_2} = {division_result:.2f}")
        else:
            print("Cannot divide by zero!")
    elif operation_choice == 5:
        # Remainder :
        print("\nExample:")
        print("5. Remainder: If you have 7 apples and you want to divide them into groups of 3, you will have 1 apple left over.")
        Number_1 = int(input("\nEnter the first number: "))
        Number_2 = int(input("Enter the second number: "))
        print("\nRemainder: We will find the remainder when dividing the first number by the second number.")
        remainder_result = Number_1 % Number_2
        print(f"{Number_1} % {Number_2} = {remainder_result}")
    else:
        print("Invalid operation choice.")


while True:
    repeat = input("\nWould you like to perform calculations again? (yes/no): ")
    if repeat.lower() == 'yes':
      try:
          calculate()
      except ValueError:
          print("Invalid input. Please Enter Integer")
    elif repeat.lower() == 'no':
        print("Goodbye")
    else:
        print("Invalid selction. Please Enter yes/no")

