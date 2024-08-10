from models.account import Account


class AccountHandler:
    """
    Handles operations related to accounts, such as creating, updating, withdrawing, and transferring between accounts.
    """

    def __init__(self):
        """
        Initializes the AccountHandler with an empty dict to store accounts.

        Attributes:
        - accounts [dict]: A dict to store accounts.
        """
        self.accounts = {}

    def get_account(self, account_id):
        """
        Retrieves an account by ID.

        ## Parameters:
        - account_id [string]: The ID of the account.

        ## Returns:
        - Account object if the account exists, otherwise None.
        """
        if account_id in self.accounts:
            return self.accounts[account_id]
        return None

    def create_or_update_account(self, account_id, amount):
        """
        Creates a new account or updates an existing account.

        ## Parameters:
        - account_id [string]: The ID of the account.
        - amount [integer]: The amount to set or add to the account balance.

        ## Returns:
        - Account object with the updated balance.
        """
        if account_id in self.accounts:
            self.accounts[account_id].balance += amount
        else:
            self.accounts[account_id] = Account(account_id, amount)
        return self.accounts[account_id]

    def withdraw_from_account(self, account_id, amount):
        """
        Withdraws an amount from an account if it has balance.

        ## Parameters:
        - account_id [string]: The ID of the account.
        - amount [integer]: The amount to withdraw.

        ## Returns:
        - Account object with the updated balance if the withdrawal is ok, otherwise None.
        """
        if account_id in self.accounts and self.accounts[account_id].balance >= amount:
            self.accounts[account_id].balance -= amount
            return self.accounts[account_id]
        return None

    def transfer_between_accounts(self, origin_id, amount, destination_id):
        """
        Transfers an amount from one account to another one.

        ## Parameters:
        - origin_id [string]: The ID of the origin account.
        - amount [integer]: The amount to transfer.
        - destination_id [string]: The ID of the destination account.

        ## Returns:
        - A tuple of two Account objects: the origin account and the destination account.
        - If the transfer fails, returns (None, None).
        """
        origin = self.withdraw_from_account(origin_id, amount)
        if origin:
            destination = self.create_or_update_account(destination_id, amount)
            return origin, destination
        return None, None
