def main_menu():
    while True:
        print("-------------------------------------------------------")
        print("\nSimple Menu System")
        print("1.Add two numbers.")
        print("2.Substract two numbers.")
        print("3.Multiply two numbers.")
        print("4.divide two numbers.")
        print("5.Exit.\n")

        choice = int(input("choose an option from 1 to 5: "))

        if choice == 1:
            add_numbers()
        elif choice == 2:
            substract_numbers()
        elif choice == 3:
            multiply_numbers()
        elif choice == 4:
            divide_numbers()
        elif choice == 5:
            print("Exit\nGoodbye :) ")
            break
        else:
            print("invalid choice. you just allow to enter a number in range of 1 t0 5.")


def add_numbers():
    num1 = int(input("Enter number one: "))
    num2 = int(input("Enter number two: "))
    print(num1 + num2)


def substract_numbers():
    num1 = int(input("Enter number one: "))
    num2 = int(input("Enter number two: "))
    print(num1 - num2)


def multiply_numbers():
    num1 = int(input("Enter number one: "))
    num2 = int(input("Enter number two: "))
    print(num1 * num2)


def divide_numbers():
    num1 = int(input("Enter number one: "))
    num2 = int(input("Enter number two: "))
    if num2 != 0:
        print(num1 // num2)
    else:
        print("can not divide by zero.")


# for starting the menu system, call the main function. type this: main_menu()
main_menu()
