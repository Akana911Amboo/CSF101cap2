################################
# TASHI TOBDEN
# 1 ELECTRICAL
# 02230083
################################
# REFERENCES
# https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/
# https://www.freecodecamp.org/news/how-to-build-an-online-banking-system-python-oop-tutorial/
# https://www.codewithc.com/building-a-bank-account-system-in-python/?amp=1
# https://www.tutorjoes.in/Python_example_programs/bank_management_system_in_python
################################################################################################################# 

import random  #This command is used to import the random module, which contains functions for generation of random numbers and choice of random items
import os  #This command is used to import the os module, and this module provides a way of using operating system-dependent functionality. The os module also includes functions for file system interaction, process management, reading or changing the environment variables.

class Account: #this functions uses the fundamental concept of OOP and creates an object with the attributes such as account number, password, etc
    def __init__(self, account_number, password, account_type, balance=0): # a function is created that is associated with the object
        self.account_number = account_number #This line is creating an instance attribute called account_number and assigning it the value passed to the constructor. The self variable points to the current class instance, and account_number is the variable passed to the __init__ method.
        self.password = password #This line instantiates an instance attribute called password and sets it to the value of the password parameter.
        self.account_type = account_type #This line creates an instance attribute by the name account_type and assigns to it the value of the account_type parameter.
        self.balance = balance #This line creates an instance variable named balance and assigns it the value of the balance parameter.

    def deposit(self, amount): #This line initiates the definition of a method named deposit. The parameter self refers to the instance of the class on which this method will be called. The amount parameter is the amount of money that will be deposited in the account.
        self.balance += amount #This line adds the value of amount to the balance attribute of the class instance. The += operator is short for self.balance = self.balance + amount, which means "add amount to the current balance."
        print(f"Deposited Nu {amount}. New balance is Nu {self.balance}.") #This line outputs a message to the console, stating how much was deposited and the new balance. An f before the string declares that it's an f-string; hence, it does support embedded expressions inside string literals. Probably, Nu is a notation of currency; {amount} and {self.balance} will be filled by the values of amount and self.balance correspondingly.

    def withdraw(self, amount): #It defines a method named withdraw, which takes two parameters: self—referencing the instance of the class—and amount, the money to be withdrawn.
        if self.balance >= amount: # checks if the account's balance covers the sum to be withdrawn.
            self.balance -= amount # Subtracts the amount from balance of account when there is sufficient funds.
            print(f"Withdrew Nu {amount}. New balance is Nu {self.balance}.") #Prints a message indicating that withdrawal is complete and displays a new balance.
        else:
            print("Insufficient funds.") #If insufficient balance, else: print(\"Insufficient funds.\") prints an error message.

    def display_balance(self): #The display_balance method is used to display the current balance of a bank account or, for that matter, any account, by printing it to the console. This will show the balance for the account when you call this method on an instance of the class.
        print(f"Current balance: Nu {self.balance}")

class PersonalAccount(Account): #This line defines a new class (child class from parent) named PersonalAccount. The class inherites from the parent class called Account.
    def __init__(self, account_number, password, balance=0): #Defined the constructor with the parameters account_number, password, and optional parameter balance set to a default of 0.
        super().__init__(account_number, password, "Personal", balance) #Calls the constructor of the superclass (parent) Account class, passing the account number, password, "Personal" as the account type, and balance.

class BusinessAccount(Account): #This line defines a new class, BusinessAccount, to be a subclass of the Account class.
    def __init__(self, account_number, password, balance=0): #This is the constructor method of the BusinessAccount class; it is called each time a new instance of the BusinessAccount class is being created.
        super().__init__(account_number, password, "Business", balance) #This line invokes the superclass's constructor (Account) and passes the account number, password, and the string "Business" to set the account type, plus an initial balance (defaulted to 0 if not supplied).

def generate_account_number(): #This line defines a function called generate_account_number.
    return str(random.randint(10000000, 99999999)) #The function will return a string representation of a random integer in the range 10,000,000 through 99,999,999. This random number will be an account number unique in nature.

def generate_password(): #This line defines a function called generate_password
    return str(random.randint(1000, 9999)) #This function will retun a string representation of a random integer in the range 1000 to 9999. This random number will be the password for the account created.

def save_account_to_file(account): #Defines a function for saving account details to a file.
    with open("accounts.txt", "a") as file: #Opens the file accounts.txt in append mode (\"a\"), which writes data to the end of the file without overwriting anything. The file variable is now referenced in the block.
        file.write(f"{account.account_number},{account.password},{account.account_type},{account.balance}\n") #Writes the account number, password, type, and balance to the file, separating each account by commas, and ends with a newline character (\\n) to make sure each account is on a newline.

def load_accounts_from_file(): #Defines a function load_account_details that takes a file name as input and returns a dictionary with account number as key and account object as value.
    accounts = {} #Initialize an empty dictionary to hold account objects.
    if os.path.exists("accounts.txt"): #Checks if the file accounts.txt exists in the directory.
        with open("accounts.txt", "r") as file: #Open the file accounts.txt in read mode.
            for line in file: #Iterate over each line in the file:
                account_number, password, account_type, balance = line.strip().split(',') # Parse the line by removing whitespaces and splitting by a comma to get variables.
                balance = float(balance) #Convert the balance string to a float.
                if account_type == "Personal": #Check the type of account: if it is personal:
                    account = PersonalAccount(account_number, password, balance) #Create a PersonalAccount object using the extracted details.
                elif account_type == "Business": #Check the type of account: if it is business:
                    account = BusinessAccount(account_number, password, balance) #Create a BusinessAccount object with the extracted details.
                accounts[account_number] = account #Set account object in the dictionary using the account number as key.
    return accounts #Return the dictionary with loaded accounts.

def main(): #It defines the main function, which is generally the entry point for a Python program.
    accounts = load_accounts_from_file() #Invokes the function load_accounts_from_file to load existing account details from a file and stores them in a variable named accounts.

    while True: #Starts an infinite loop, which will continue until it's explicitly broken out of.
        print("\nBanking Application") #Shows the title "Banking Application" on the screen.
        print("1. Open Account") #Displays the option to the user \"1. Open Account\".
        print("2. Login") #Show \"2. Login\" to the user.
        print("3. Exit") #Shows the "3. Exit" option to the user.
        choice = input("Enter choice: ") #Prompts the user for their choice and stores it in a variable named choice.

        if choice == '1': #Checks if the input from user (choice) is '1' (option to open new account).
            account_type = input("Enter account type (Personal/Business): ") #Prompts the user for the type of account they would like to open and stores it in a variable called account_type.
            account_number = generate_account_number() #Invokes the function generate_account_number to produce a new, unique account number, and this account number is held in a variable named account_number.
            password = generate_password() #Calls the generate_password function to generate a new password and stores it in a variable named password.

            if account_type.lower() == "personal": #It checks if the input of the user for account_type, after it is converted to lowercase, is equal to \"personal\".
                account = PersonalAccount(account_number, password) #If it is equal to \"personal\", then a new instance of the PersonalAccount class is created with the generated account number and password.
            elif account_type.lower() == "business": #It checks whether the input from the user for account_type, converted to lowercase, is equal to the string \"business\".
                account = BusinessAccount(account_number, password) #In the case where the user enters \"business\", this block creates a new instance of the BusinessAccount class with the generated account number and password.
            else: #If the input is neither \"personal\" nor \"business\", it enters this block.
                print("Invalid account type.") #It informs the user that they entered an invalid account type.
                continue #It jumps back to the start of the loop so that the rest of the code inside it doesn't run.

            accounts[account_number] = account #Adds the newly created object of account to the dictionary of accounts with key as the account_number.
            save_account_to_file(account) #Calls the save_account_to_file function to write the account details to "accounts.txt" file.
            print(f"Account created. Account Number: {account_number}, Password: {password}") #Prints a message to the user with the new account number and password, indicating that the account has been successfully created.

        elif choice == '2': #Checks if the input of the user (choice) is equal to 2, which corresponds to the option to log in to an account.
            account_number = input("Enter account number: ") #Prompts the user to enter their account number and stores it in a variable named account_number.
            password = input("Enter password: ") #Prompts the user for their password and stores it in a variable called password.
            account = accounts.get(account_number) #Fetches the account object from the accounts dictionary using the supplied account_number. Get will return None if account number does not exist.

            if account and account.password == password: #Checks for existence of account object, that is if account number entered was found, and the password related to that account matches password input by user.
                print(f"Logged in as {account.account_type} Account {account_number}") #If the entered credentials are valid, it prints a message that the user is signed in and specifies the account type and account number.

                while True: #Creates a infinite loop,  which will continue until it's explicitly broken out of.
                    print("\n1. Check Balance") #It presents to the user a \"1. Check Balance\" option.
                    print("2. Deposit") #Shows the user the option "2. Deposit".
                    print("3. Withdraw") #Presents to the user the option "3. Withdraw".
                    print("4. Transfer Money") #Shows the user the option \"4. Transfer Money\".
                    print("5. Delete Account") #Show the user the option \"5. Delete Account\".
                    print("6. Logout") #Displays to the user the option \"6. Logout\".
                    sub_choice = input("Enter choice: ") #Asks the user to enter their choice from the submenu and stores it in a variable named sub_choice.

                    if sub_choice == '1': #Checks if the user's input(sub_choice) is '1' which is the check account balance option.
                        account.display_balance() #Invokes the display_balance of the account object to display the current balance.

                    elif sub_choice == '2': #Checks if the user's input(sub_choice) is '2' which is the deposit money option.
                        amount = float(input("Enter amount to deposit: ")) #Prompts the user to input the amount they would like to deposit, and parse to float
                        account.deposit(amount) #Invokes the account object's deposit method with the entered amount

                    elif sub_choice == '3': #Checks if the user's input(sub_choice) is '3' which is the withdraw money option
                        amount = float(input("Enter amount to withdraw: ")) #Prompts the user to enter the amount they would like to withdraw, and parse to float
                        account.withdraw(amount) #Invokes the account object withdraw method with the entered amount

                    elif sub_choice == '4': #Checks if the user's input(sub_choice) is '4' which is the transfer money option
                        target_account_number = input("Enter target account number: ") #Prompts the user to enter the target account number they would like to transfer to
                        amount = float(input("Enter amount to transfer: ")) #Prompts the user to enter the amount they would like to transfer, and parse to float
                        target_account = accounts.get(target_account_number) #Extracts the target account object using the target account number from the accounts dictionary, if the account number doesn't exist the get will return None.

                        if target_account: #The first line checks if the target_account exists. If it does, it moves on to the next process. If not, it prints "Target account does not exist."
                            if account.balance >= amount: #The inside of the first if block ensures that the balance in the account, presumably the source account, can accommodate the amount specified.
                                account.withdraw(amount) #Withdraws the specified amount from the account
                                #If and only if both conditions are fulfilled: target account exists and balance in source account is sufficient, it does the following:
                                target_account.deposit(amount) #Deposits the same amount in the target_account.
                                print(f"Transferred Nu {amount} to {target_account_number}.") #Prints a message to the effect that transfer is successful, thus: "Transferred Nu {amount} to {target_account_number}."
                            else:
                                print("Insufficient funds.") ##If the balance is sufficient, it moves on to the next process. If not, it prints "Insufficient funds.
                        else:
                            print("Target account does not exist.") #prints target account doesnot exist if the reveivingaccount is not valid

                    elif sub_choice == '5': #checks if the user choose the option '5' to execute the below progran
                        confirm = input("Are you sure you want to delete this account? (yes/no): ") #The user is requested to confirm if they want to delete the account. The response to that question is stored in the variable confirm.
                        if confirm.lower() == 'yes': #The input is converted to lowercase so as to compare confirmation in a case-insensitive manner. If the user confirms by writing \"yes\", deletion proceeds.
                            del accounts[account_number]
                           # The specified account is removed from the dictionary of accounts. In this example, account_number is the key to the specified account in the dictionary.
                            with open("accounts.txt", "w") as file: #The program opens the file \"accounts.txt\" in write mode (\"w\"), meaning the file will be overwritten.
                                for acc in accounts.values(): #The program iterates over the remaining accounts from the dictionary of accounts.
                                    file.write(f"{acc.account_number},{acc.password},{acc.account_type},{acc.balance}\n") #For each account (acc), the details of the account - account number, password, account type, and balance - are written in the file in CSV format.
                            print("Account deleted.") #A message is printed to the user that the account has been deleted.
                            break #It breaks out of the loop. The break statement breaks out of the loop meaning the program will cease from any further operations of this account deletion.

                    elif sub_choice == '6': #If a user chooses option 6 from the submenu, the program will print \"Logged out.
                        print("Logged out.")
                        break #The break statement will terminate the current loop, and the user will be effectively logged out by terminating the submenu interaction.

                    else: #If the user selects a choice other than expected in the submenu (since 6 is not a valid choice), the program would display \"Invalid choice.\
                        print("Invalid choice.")
            else: #In the case when an account number or password entered is incorrect, the program will display \"Invalid account number or password.
                print("Invalid account number or password.") #

        elif choice == '3': #When a user chooses option 3 from the main menu, the program will print \"Exiting application.
            print("Exiting application.")
            break

        else: #If the user opts for a choice other than the expected ones in the main menu (since 3 is not a valid choice), the program will display \"Invalid choice.\"

            print("Invalid choice.")

main() 
#The main() function orchestrates user interactions in the program, facilitates the main menu and sub-menu options, user authentication,
# and account management such as view balance(s), deposit/withdraw, transfer funds, close account, log out, or exit the application.

