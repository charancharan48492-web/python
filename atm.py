account={
    "name":"charan",
    "balance":"100000000",
    "pin":"9944",
    "type":"businessaccount"

}
print("===MINI ATM===")
pin=input("enter your pin: ")
if pin == account["pin"]:
    while True:
        print("***MINI ATM===")
        print("1. check balance:")
        print("2. withdraw money:")
        print("3. deposit money:")
        print("4 . account details:")
        print("5. exit")
        choice=input("enter your choice: ")
        if choice=="1":
            print("your balance is:",account["balance"])
        elif choice=="2":
            amount=input("enter your amount:")
            if amount>0:
                account["balance"]=account["balance"]+amount
                print("money deposited successfully.")
                print ("collect your cash")
                print("New balance",account["balance"])
        elif choice=="4":
            print("\nAccount Name",account["name"])
            print("Account Balance",account["balance"])
            print("\nAccount Type",account["type"])
        elif choice=="5":
           print("thank you for using mini atm.")
           break
        else:
            print("invalid pin")
            print("access denied")