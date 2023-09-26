from Validation import *
import sys
class BankAccount:
    customer_name={}
    def __init__(self, bank_name, ifsc_code, account_number, account_holder_name, age, gender, dob, address,
                 city, account_type, balance, pan_card_number, aadhar_number):
        self.bank_name = bank_name
        self.ifsc_code = ifsc_code
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.age = age
        self.gender = gender
        self.dob = dob
        self.address = address
        self.city = city
        self.account_type = account_type
        self.balance = balance
        self.pan_card_number = pan_card_number
        self.aadhar_number = aadhar_number

'''
        if(self.account_type in self.customer_name.keys()):
            self.customer_name[self.account_type]=[]
            self.customer_name[self.account_type].append(self.account_holder_name)
        else:
            self.customer_name[self.account_type]=self.account_holder_name
        
    def display(self):
        for k,v in self.customer_name.items():
            print(k,v)
'''
    def update_account_holder_name(self, new_name):
        self.account_holder_name = new_name

    def update_address(self, new_address):
        self.address = new_address

    def update_dob(self, new_dob):
        self.dob = new_dob

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def transfer_funds(self, receiver, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            receiver.deposit(amount)
            return True
        else:
            return False

    def balance_enquiry(self):
        return self.balance


    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder Name: {self.account_holder_name}\n" \
               f"Bank Name: {self.bank_name}\nBalance: {self.balance}\n"


# Create a dictionary to store bank accounts using account numbers as keys
bank_accounts = {}
    
def create_account():
    while True:
        print("Create a New Bank Account:")
        bank_name = input("Enter Bank Name: ")
        account_number = input("Enter Account Number: ")
        account_holder_name = input("Enter Account Holder Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        dob = input("Enter Date of Birth (DD-MM-YYYY): ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        account_type = input("Enter Type of Account: ")
        balance = input("Enter Initial Balance: ")
        pan_card_number = input("Enter PAN Card Number: ")
        aadhar_number = input("Enter Aadhar Number: ")
        ifsc_code = input("Enter IFSC code: ")
        

        if(isBankNameValid(bank_name)):
            pass
        else:
            print("Invalid Bank Name !! Please enter the correct Bank Name")

        
        if(isCityNameValid(city)):
            pass
        else:
            print("Invalid City Name !! Please enter the correct City Name")
        

        if(isIFSCValid(ifsc_code)):
            pass
        else:
            print("Invalid IFSC Code !! Please enter the correct IFSC Code")


        if(isAgeValid(age)):
            pass
        else:
            print("Invalid Age !! Please enter the correct Age")

        if(isAadharValid(aadhar_number)):
            pass
        else:
            print("Invalid Aadhar Number !! Please enter the correct Aadhar Number")

        if(isGenderValid(gender)):
            pass
        else:
            print("Invalid Gender!! Please enter the correct Gender")

        if(isAccountTypeValid(account_type)):
            pass
        else:
            print("Invalid Account Type!! Please enter the correct Account Type")

        if(isInitialBalanceValid(balance)):
            pass
        else:
            print("Invalid Amount!! Please enter the correct Amount")

        if(isAddressValid(address)):
            pass
        else:
            print("Invalid address!! Please enter the correct address")


        if(isDOBValid(dob)):
            pass
        else:
            print("Invalid Date!! Use proper date,month,year and hypen")

        if(isAccountHolderName(account_holder_name)):
            pass
        else:
            print("Invalid Name!! Please use alphabets and capitalize all the words..")

        if(isAccountNumberValid(account_number)):
            break
        else:
            print("Invalid account number!! Please enter the correct account number")


    new_account = BankAccount(bank_name, ifsc_code, account_number, account_holder_name, age, gender, dob, address,
                                  city, account_type, balance, pan_card_number, aadhar_number)   
    bank_accounts[account_number] = new_account
    print("Account created successfully!")
            
      
  

def delete_account():
    account_number = input("Enter Account Number to delete: ")
    if account_number in bank_accounts:
        del bank_accounts[account_number]
        print(f"Account {account_number} deleted successfully!")
    else:
        print("Account does not found.")

def update_account_details():
    account_number = input("Enter Account Number to update details: ")
    if account_number in bank_accounts:
        account = bank_accounts[account_number]
        print("\nSelect an option to update:")
        print("1. Update name of account holder")
        print("2. Update address of account holder")
        print("3. Update DOB of account holder")
        choice = input("Enter your choice: ")

        if choice == '1':
            new_name = input("Enter new name: ")
            account.update_account_holder_name(new_name)
            print("Account holder name updated successfully!")
        elif choice == '2':
            new_address = input("Enter new address: ")
            account.update_address(new_address)
            print("Address updated successfully!")
        elif choice == '3':
            new_dob = input("Enter new Date of Birth (DD-MM-YYYY): ")
            account.update_dob(new_dob)
            print("Date of Birth updated successfully!")
        else:
            print("Invalid choice.")
    else:
        print("Account not found.")

def deposit():
    account_number = input("Enter Account Number to deposit into: ")
    if account_number in bank_accounts:
        account = bank_accounts[account_number]
        amount = int(input("Enter the amount to deposit: "))
        if account.deposit(amount):
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")
    else:
        print("Account not found.")

def withdraw():
    account_number = input("Enter Account Number to withdraw from: ")
    if account_number in bank_accounts:
        account = bank_accounts[account_number]
        amount = float(input("Enter the amount to withdraw: "))
        if account.withdraw(amount):
            print("Withdrawal successful.")
        else:
            print("Invalid withdrawal amount.")
    else:
        print("Account not found.")

def funds_transfer():
    sender_account = input("Enter sender's Account Number: ")
    receiver_account = input("Enter receiver's Account Number: ")
    amount = float(input("Enter the amount to transfer: "))
        
    if sender_account in bank_accounts and receiver_account in bank_accounts:
        sender = bank_accounts[sender_account]
        receiver = bank_accounts[receiver_account]
        if sender.transfer_funds(receiver, amount):
            print("Funds transfer successful.")
        else:
            print("Invalid transfer amount.")
    else:
        print("Sender or receiver account not found.")

def search_account():
    print("\nSearch Account Details:")
    print("1. Search by Account Number")
    print("2. Search by Name")
    print("3. Search by Type of Account")
    choice = input("Enter your choice: ")

    if choice == '1':
        account_number = input("Enter Account Number to search: ")
        if account_number in bank_accounts:
            print(bank_accounts[account_number])
        else:
            print("Account not found.")
    elif choice == '2':
        name = input("Enter Account Holder Name to search: ")
        found = False
        for account in bank_accounts.values():
            if account.account_holder_name.lower() == name.lower():
                print(account)
                found = True
            if not found:
                print("No accounts found for the given name.")
    elif choice == '3':
        account_type = input("Enter Type of Account to search: ")
        found = False
        for account in bank_accounts.values():
            if account.account_type.lower() == account_type.lower():
                print(account)
                found = True
            if not found:
                print("No accounts found for the given account type.")
    else:
        print("Invalid choice.")

def balance_enquiry():
    account_number = input("Enter Account Number for balance enquiry: ")
    if account_number in bank_accounts:
        print(bank_accounts[account_number].balance_enquiry())
    else:
        print("Account not found.")


print("\n---------Bank Account Management System---------")

n=int(input("Enter how may records you want to insert: "))
while True:
    print("1. Create Account")
    print("2. Delete Account")
    print("3. Update Account Details")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Funds Transfer")
    print("7. Search Account Details")
    print("8. Balance Enquiry")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        for i in range(n):
            create_account()
    elif choice == '2':
        delete_account()
    elif choice == '3':
        update_account_details()
    elif choice == '4':
        deposit()
    elif choice == '5':
        withdraw()
    elif choice == '6':
        funds_transfer()
    elif choice == '7':
        search_account()
    elif choice == '8':
        balance_enquiry()
    elif choice == '9':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

   
        
       
    wish=input("Do you want to continue: Press Yes or No")
    if(wish.lower()=='no'):
        print("-----Thank You-----")
        print("-----Visit Again-----")
        sys.exit(0)
    
