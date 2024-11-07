import datetime

class ATM:

    def __init__(self):
        self.users = {
            '1234': {'pin': '1111', 'balance': 1000, 'history': []},
            '5678': {'pin': '2222', 'balance': 5000, 'history': []},
        }
        self.current_user = None
    
    def authenticate(self, card_number, pin):
        user = self.users.get(card_number)
        if user and user['pin'] == pin:
            self.current_user = card_number
            print ("Authentication successful!")
            return True
        else:
            print ("Authentication failed!")
            return False
        
    def check_balance(self):
        balance = self.users[self.current_user]['balance']
        print(f"Your current balance is: ${balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
            return
        self.users[self.current_user]['balance'] += amount
        self.add_transaction("Deposit", amount)
        print(f"${amount} deposited successfully!")

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
    
    def add_transaction(self, transaction_type, amount):
        timestamp = datetime.datetime.now().strftime ("%Y-%m-%d T%H:%M:)%S")
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'timestamp': timestamp
        }
        self.users[self.current_user]['history'].append(transaction)

    