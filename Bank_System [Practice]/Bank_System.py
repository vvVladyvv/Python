print("***********Bank System************")
print()
Balance = 1000
Work = True
while Work:
    try:
        options = int(input("1. View account balance\n2. Deposit balance\n3. Withdraw balance\n4. Exit\n\nInto an option: "))
    except ValueError:
        print("Please into an numeric value!")
        continue
    if options not in [1, 2, 3, 4]:
        print("Please select an valid option!")
    elif options == 1:
            print(f"\nAccount balance: ${Balance:.2f}")
            print('\n------------------------------------------------\n')
    elif options == 2:
        print()
        deposit = int(input("How many cant you want deposit: "))
        if deposit > 0:
            Balance += deposit
            print("Deposit was realized succesfully.")
            print('\n------------------------------------------------\n')
        else:
            print("Declined")
            print('\n------------------------------------------------\n')
        
    elif options == 3:
        print()
        withdrawal = int(input("How many cant you want withdraw: "))
        if withdrawal <= Balance:
            Balance -= withdrawal
            print("Withdrawal was realized succesfully!")
            print('\n------------------------------------------------\n')
        else:
            print("Declined")
            print('\n------------------------------------------------\n')
    elif options == 4:
        print("Exit...")
        Work = False
