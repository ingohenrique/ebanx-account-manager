from models.account import Account
class AccountHandler:

    def __init__(self):
        self.accounts = {}
    
    def create_or_update_account(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].balance += amount
        else:
            self.accounts[account_id] = Account(account_id, amount)
        return self.accounts[account_id]
    
    def withdraw_from_account(self, account_id, amount):
        if account_id in self.accounts and self.accounts[account_id].balance >= amount:
            self.accounts[account_id].balance -= amount
            return self.accounts[account_id]
        return None