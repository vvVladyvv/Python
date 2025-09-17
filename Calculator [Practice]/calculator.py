print("Welcome to the calculator\n-------------------------------\n")
on = True
while on:
    try:
        options = int(input("1. Sum\n2. Substract\n3. Multiplication\n4. Division\n5. Multiplication of exponents\n6. Exit\n\n@App developed by vvVladyvv\n\nWrite an option: "))
        if options not in [1, 2, 3, 4, 5, 6]:
            print("\n----------------------\nOption not found.\n----------------------\n")
        elif options == 1:
            print("Sum\n--------------------\nLet in blank for exit")
            while True:
                try:
                    first_value = float(input("Enter the first value: "))
                    second_value = float(input("Enter the second value: "))
                    Sum = first_value + second_value
                    print(f"\n--------------------------\nSum value is: {Sum}\n------------------------------\n")
                except ValueError:
                    print("Enter numbers value!")
                    break
        elif options == 2:
            print("Substract\n--------------------\nLet in blank for exit")
            while True:
                try:
                    first_value = float(input("Enter the first value: "))
                    second_value = float(input("Enter the second value: "))
                    Substract = first_value - second_value
                    print(f"\n--------------------------\nSubstract value is: {Substract}\n------------------------------\n")
                except ValueError:
                    print("Enter numbers value!")
                    break
        elif options == 3:
            print("Multiplication\n--------------------\nLet in blank for exit")
            while True:
                try:
                    first_value = float(input("Enter the first value: "))
                    second_value = float(input("Enter the second value: "))
                    Multiplicaction = first_value * second_value
                    print(f"\n--------------------------\nMultiplicaction value is: {Multiplicaction}\n------------------------------\n")
                except ValueError:
                    print("Enter numbers value!")
                    break
        elif options == 4:
            print("Division\n--------------------\nLet in blank for exit")
            while True:
                try:
                    first_value = float(input("Enter the first value: "))
                    second_value = float(input("Enter the second value: "))
                    Division = first_value / second_value
                    print(f"\n--------------------------\nDivision value is: {Division}\n------------------------------\n")
                except ValueError:
                    print("Enter numbers value!")
                    break
        elif options == 5:
            print("Exponents Multiplication\n--------------------\nLet in blank for exit")
            while True:
                try:
                    first_value = float(input("Enter the first value: "))
                    second_value = float(input("Enter the second value: "))
                    Multiplicaction = first_value ** second_value
                    print(f"\n--------------------------\nMultiplication value is: {Multiplicaction}\n------------------------------\n")
                except ValueError:
                    print("Enter numbers value!")
                    break
        elif options == 6:
            print("Exit the sistem.....")

            on = False
    except ValueError:
        print("\n-------------------\nPlease enter number values!\n----------------------\n")
