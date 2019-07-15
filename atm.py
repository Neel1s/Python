class bank:
    customer_data = {1111:80520,1211:52000,1321:850000,5111:9000000}
    print("Welcome to XYZ banking services")
    pin=eval(input(print("Please enter your pin\n")))
    option=eval(input(print("Select a choice 1. Deposit\n 2. Withdraw\n  3. Check Balance")))
    def deposit(pin):
        print("Enter the amout")
        deposit_amount=eval(input())
        customer_data[pin]=customer_data[pin]+deposit_amount
    def withdraw(pin):
        withdraw_amount=eval(input(print("Enter the amout")))
        customer_data[pin]=customer_data[pin]-withdraw_amount

    def check_balance(pin):
        print("Your balance is: ")
        print(customer_data[pin])
    if option == 1:
        def deposit(pin)
    elif option ==2:
        def withdraw(pin)
    else:
        def check_balance(pin)


