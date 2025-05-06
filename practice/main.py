# ATM format 
print("==========Welcome=========")
pin = int(input("Enter your pin: "))

if pin==1234:
    amount= 10000
    print("1. Check balance")
    print("2. Withdraw cash")
    print("3. Exit")
    option = int(input("Select an option: "))
    if option==1:
        print("Your balance is: ", amount)
        print("Thank you for using the ATM!") 
    elif option==2:
        wamount= int(input("Enter amount to withdraw: "))
        if wamount<=amount:
            rem=amount-wamount
            print(f"Withdraw Amount: {wamount}! New balance: {rem}")
            print("Thank you for using the ATM!") 
        else:
            print("Insufficient funds")
    
              
else:
        print("Incorrect pin")
        exit()


# practice 2 present three products to the customer. The customer selects one product, and the program then shows the price details of the selected product:

# print("Welcome to the store! Please choose one of the following product: ")
# option = int(input("Choose device: "))
# if option==1:
#    print("Laptop")
#    print("price for this device is: ,amount")
