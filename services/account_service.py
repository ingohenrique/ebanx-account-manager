class AccountService:

    def __init__(self, account_handler):
        self.account_handler = account_handler

    def deposit(self, destination, amount):
        account = self.account_handler.create_or_update_account(destination, amount)
        return account
        