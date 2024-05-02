import math


# Start an infinite loop to keep the program running until the user decides to exit
while True:
    print("")
    # Ask the user for the type of mathematical operation they want to perform
    ask_1 = input("What mathematical operation would you like me to calculate \n(1.\
Cube root - 2.Power multipliers) 1 or 2: ")
    ask_2 = 0  # Initialize the variable to store the number for calculation

    # Check if the input is not valid (not 1 or 2)
    if ask_1 != "1" and ask_1 != "2":
        print("\n- Input type error. Enter a number 1 or 2!\n")
        continue  # Start the loop again to prompt the user for valid input

    else:
        # Convert the input to an integer if it's valid
        ask_1 = int(ask_1)
        # If the chosen operation is cube root or power multiplier, ask for the number
        if ask_1 == 1 or ask_1 == 2:
            ask_2 = float(input("\nEnter a number: "))

        # Perform the calculation based on the chosen operation
        if ask_1 == 1:
            # Calculate the cube root using the math.sqrt() function
            answer_1 = math.sqrt(ask_2)
            # Print the result with appropriate explanation
            print(f"The cube root of {ask_2} = {round(answer_1,2)}")
            print(f"Because {round(answer_1,2)} * {round(answer_1,2)} = {ask_2}")
        elif ask_1 == 2:
          while True:
            # If the operation is a power multiplier, ask for the power
            power_1 = int(input("Enter the power multiplier: "))
            # Calculate the result using the power operator **
            if power_1 >=1 and power_1 <=20:
              print("The power multiplier = " + str(ask_2) + (" * " + str(ask_2)) * (power_1-1) +
                    " = " + str(round(ask_2 ** power_1,2)))
              break
            elif power_1 == 0:
              print("The power multiplier = 1")
              break
            else:
              print("Error! Enter a power multiplier ander than 20.\n")
              continue  # Start the loop again to prompt the user for valid input

    # Ask the user if they want to perform another calculation
    another_calculation = input("\nDo you want to perform another calculation? (yes/no):")
    # If the user doesn't want to continue, break out of the loop and end the program
    if another_calculation.lower() != "yes":
        print("\nThank you for using the calculator! :)")
        break
    elif another_calculation.lower() == "yes":
        print("\n" + ("-"*65))
        continue  # Start the loop again to prompt the user for valid input
