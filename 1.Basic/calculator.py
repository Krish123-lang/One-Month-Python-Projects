def calculator(first_num, second_num):

    while True:
        operation_user = input(""" 
        1. Add
        2. Subtract
        3. Multiplication
        4. Divison
        5. Exit\n""")

        if operation_user == "1":
            print(f"{first_num} + {second_num} = {first_num+second_num}")
        elif operation_user == "2":
            print(f"{first_num} - {second_num} =  {first_num-second_num}")
        elif operation_user == "3":
            print(f"{first_num} x {second_num} =  {first_num*second_num}")
        elif operation_user == "4":
            if second_num == 0:
                print("Cannot divide by zero !")
            else:
                print(f"{first_num} / {second_num} =  {first_num/second_num}")
        elif operation_user == "5":
            print("Goodbye !")
            break
        else:
            print("Invalid operator !!!")


try:
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    calculator(first_num, second_num)
except ValueError:
    print("Please enter a valid number !")
