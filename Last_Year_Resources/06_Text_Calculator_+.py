# Text based calculator

def add(int_num1, int_num2, int_option):
    if int_option == "Add":
        print("{:.2f} plus {:.2f} is {:.2f}".format(int_num1, int_num2, int_num1+int_num2))
        again()
    elif int_option == "Subtract":
        print("{:.2f} Subtract {:.2f} is {:.2f}".format(int_num1, int_num2, int_num1-int_num2))
        again()
    elif int_option == "Multiply":
        print("{:.2f} Multiply {:.2f} is {:.2f}".format(int_num1, int_num2, int_num1*int_num2))
        again()
    elif int_option == "Divide":
        print("{:.2f} Divide {:.2f} is {:.2f}".format(int_num1, int_num2, int_num1/int_num2))
        again()
    else:
        print("Error")
        main()


def main():
    int_num1 = float(input('What is your first number, please? '))
    int_num2 = float(input('What is your second number, please?'))
    int_option = input("Do you want to Add, Subtract, Multiply or Divide, Enter the option you want.").title()
    
    add(int_num1, int_num2, int_option)


def again():
    int_yes = input("Do you want to play again Y/N")
    if int_yes == "Y":
        main()
    if int_yes == "N":
        print("Goodbye")
        exit()
    else:
        print("Please enter Y or N")
        again()


main()
