from models.account import Account
class AccountHandler:

    def __init__(self):
        self.accounts = {}
    
    def create_or_update_account(self, account_id, balance):
        if account_id in self.accounts:
            self.accounts[account_id].balance += balance
        else:
            self.accounts[account_id] = Account(account_id, balance)
        return self.accounts[account_id]