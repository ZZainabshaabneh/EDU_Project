# This python file will deal with teaching the operation, >, <, =, !=
import sys
import time
from colorama import init, Fore, Style

init()


def print_blinking_text(text, blink_duration=3):
    for _ in range(blink_duration * 2):  # Blink for the specified duration
        sys.stdout.write('\r' + text)
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r' + ' ' * len(text))
        sys.stdout.flush()
        time.sleep(0.5)

def kashkah():
    print("----------------------------------------------")


def select_an_operation():
    kashkah()
    print(Fore.BLUE)
    print("-  Choose an operator to study 🏫 about:")
    print("-  >, press 1  : ")
    print("-  <, press 2  : ")
    print("-  =, press 3  : ")
    print("-  !=,press 4  :")
    kashkah()
    operation_selected = int(input("Please choose am operation to learn about it : "))
    print(Fore.RESET)

    if operation_selected == 1:
        kashkah()
        print("You are about to learn the operator >")
        print("This operator teaches which number is greater than the other one")
        print("The answer could be either True or False for executing its next job")
        print("I will guide you to an example of usage")
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        if first_number > second_number:
            print(Fore.GREEN)
            print(Style.BRIGHT, f"Correct answer this number {first_number} > {second_number} 😀")
            print(Fore.RESET)
        else:
            print(Fore.RED)
            print(f"Incorrect number {first_number} is not bigger"
                  f" than the number {second_number} 😔")
            print(Fore.RESET)
    elif operation_selected == 2:
        kashkah()
        print("You are about to learn the operator <")
        print("This operator teaches which number is lesser than the other one")
        print("The answer could be either True or False for executing its next job")
        print("I will guide you to an example of usage")
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        if first_number < second_number:
            print(Fore.GREEN)
            print(Style.BRIGHT, f"Correct answer this number {first_number} < {second_number} 😀")
            print(Fore.RESET)
        else:
            print(Fore.RED)
            print(f"Incorrect the number {first_number} is not less"
                  f" than the number {second_number} 😔")
            print(Fore.RESET)
    elif operation_selected == 3:
        kashkah()
        print("You are about to learn the operator =")
        print("This operator teaches which number is equal to the other number")
        print("The answer could be either True or False for executing its next job")
        print("I will guide you to an example of usage")
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        if first_number == second_number:
            print(Fore.GREEN)
            print(Style.BRIGHT, f"Correct answer this number {first_number} = {second_number} 😀")
            print(Fore.RESET)
        else:
            print(Fore.RED)
            print(f"Incorrect answer the number {first_number} does not equal"
                  f" to the number {second_number} 😔")
            print(Fore.RESET)

    elif operation_selected == 4:
        kashkah()
        print("You are about to learn the operator !=, not equal")
        print("This operator teaches if the numbers are not equal to each other")
        print("The answer could be either True or False for executing its next task")
        print("I will guide you to an example of usage")
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        if first_number != second_number:
            print(Fore.GREEN)
            print(Style.BRIGHT, f"Correct answer this number {first_number} != {second_number} 😀")
            print(Fore.RESET)
        else:
            print(Fore.RED)
            print(f"Incorrect answer this number {first_number} is equal"
                  f" to this number {second_number}, as we learn about not equal 😔")
            print(Fore.RESET)
    else:
        print(Fore.YELLOW)
        print("Incorrect selection, only numbers from 1-4 are accepted")
        print(Fore.RESET)

def call_operations():
    while True:
        print(Fore.YELLOW)
        repeat = input("\nDo you want to learn operations ? (yes/no): ")
        print(Fore.RESET)
        if repeat.lower() == 'yes':
            try:
                select_an_operation()
            except ValueError:
                # Code to execute if a ValueError is raised
                #            print(Fore.RED + 'Invalid input. Please enter a valid integer!')
                print(Fore.RED)
                print_blinking_text('Invalid input. Please enter a valid integer value!')
                print(Fore.RESET)
        elif repeat.lower() == 'no':
            print(Fore.GREEN)
            print("Goodbye! ❤️")
            print(Fore.RESET)
            break
        else:
            print(Fore.RED)
            print("Only yes or no are accepted")
            print(Fore.RESET)
