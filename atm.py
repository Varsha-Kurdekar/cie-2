import sys

if len(sys.argv) == 4:
    withdrawal = sys.argv[1]
    balance = sys.argv[2]
    pin = sys.argv[3]
    print("User provided inputs.")
    
else:
    withdrawal = 1000      
    balance = 500       
    pin = 12345 
    print("No inputs given - using default values.")  
    
    print("ATM details\n")  
    print("Withdrawal:",withdrawal) 
    print("Balance:",balance)   
    print("PIN:",pin)       

if pin == 12345:
    print("Approved:")
    else:
        print("Transaction Declined: Insufficient Balance")
else:
    print("Transaction Declined: Incorrect PIN")
