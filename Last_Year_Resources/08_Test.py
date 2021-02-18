# Text based calculator

def add(int_num1, int_num2, int_option, Operator):
    Number = Operator( int_num1, int_num2)
    print(Number)
    

def main():
    int_num1 = float(input('What is your first number, please? '))
    int_num2 = float(input('What is your second number, please?'))
    int_option = input("Do you want to Add, Subtract, Multiply or Divide, Enter the option you want.").title()
    if int_option == "Add":
            Operator = "+"
            print(Operator)
    
    add(int_num1, int_num2, int_option, Operator)


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

Number = (+( 2, 2))
print(Number)
main()
