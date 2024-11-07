import datetime

class ATM:

    # Define Users
    def __init__(self):
        self.users = {
            '1234': {'pin': '1111', 'balance': 1000, 'history': []},
            '5678': {'pin': '2222', 'balance': 5000, 'history': []},
        }
        self.current_user = None
    
    # Authentication Process
    def authenticate(self, card_number, pin):
        user = self.users.get(card_number)
        if user and user['pin'] == pin:
            self.current_user = card_number
            print ("Authentication successful!")
            return True
        else:
            print ("Authentication failed!")
            return False
        
    # Check Balance    
    def check_balance(self):
        balance = self.users[self.current_user]['balance']
        print(f"Your current balance is: ${balance}")
    
    # Deposit
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
            return
        self.users[self.current_user]['balance'] += amount
        self.add_transaction("Deposit", amount)
        print(f"${amount} deposited successfully!")

    # Withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
            return
        if amount > self.users[self.current_user]['balance']:
            print("Insufficient balance!")
            return
        self.users[self.current_user]['balance'] -= amount
        self.add_transaction("Withdrawal", amount)
        print(f"${amount} withdrawn successfully!")

    # Add a transaction
    def add_transaction(self, transaction_type, amount):
        timestamp = datetime.datetime.now().strftime ("%Y-%m-%d T%H:%M:)%S")
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'timestamp': timestamp
        }
        self.users[self.current_user]['history'].append(transaction)

    # View the transaction
    def view_transaction_history(self):
        print("Transaction history:")
        for transaction in self.users[self.current_user]['history']:
            print(f"{transaction['timestamp']} - {transaction['type']}: ${transaction['amount']}")
    
    # Logout
    def logout(self):
        print("Logging out...")
        self.current_user = None
    
    # Main Content
    def run(self):
        print("Welcome to the ATM!")
        card_number = input("Enter your card number: ")
        pin = input("Enter your PIN: ")

        # Main Menu
        if not self.authenticate(card_number, pin):
            return
        
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Transaction History")
            print("5. Logout")

            choice = input("Choose an option: ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif choice == "4":
                self.view_transaction_history()
            elif choice == "5":
                self.logout()
                break
            else:
                print("Invalid choice! Please try again!")

# Create an instance of the ATM class and run the main content
atm = ATM()
atm.run()