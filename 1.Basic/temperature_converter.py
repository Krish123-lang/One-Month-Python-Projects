def c_to_f(temp=0):
    return (temp * (9/5)+32)
    


def f_to_c(temp=0):
    return (temp - 32) * (5/9)



def k_to_c(temp=0):
    return (temp - 273.15)


while True:
    try:
        user_input = int(input('''
        1. Celsius to Fahrenheit
        2. Fahrenheit to Celsius
        3. Kelvin to Celsius
        4. Exit
        '''))
        if user_input == 1:
            temperature_to_convert = float(input("Enter the temperature to convert celsius to fahrenheit: "))
            print(f"The temperature in fahrenheit is: {c_to_f(temperature_to_convert):.2f}")
            
        elif user_input == 2:
            temperature_to_convert = float(input("Enter the temperature to convert fahrenheit to celsius: "))
            print(f"The temperature in celsius is: {f_to_c(temperature_to_convert):.2f}")
        
        elif user_input == 3:
            temperature_to_convert = float(input("Enter the temperature to convert kelvin to celsius: "))
            if temperature_to_convert < 0:
                print("Kelivn cannot be negative !")
                continue
            print(f"The temperature in celsius is: {k_to_c(temperature_to_convert):.2f}")
        
        elif user_input == 4:
            print("Good Bye !")
            break
        else:
            print("Invalid option !")
    except Exception as e:
        print(e)
