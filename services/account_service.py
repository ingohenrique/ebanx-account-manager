class AccountService:

    def __init__(self, account_handler):
        self.account_handler = account_handler

    def reset(self):
        self.account_handler.accounts = {}

    def get(self, account_id):
        return self.account_handler.get_account(account_id)

    def deposit(self, destination, amount):
        return self.account_handler.create_or_update_account(destination, amount)

    def withdraw(self, origin, amount):
        return self.account_handler.withdraw_from_account(origin, amount)
        
    def transfer(self, origin, amount, destination):
        return self.account_handler.transfer_between_accounts(origin, amount, destination)