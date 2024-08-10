class AccountService:
    """
    This class interacts with the AccountHandler to perform tasks such as resetting accounts,
    get account information, and also make deposits, withdrawals, and transfers.
    """

    def __init__(self, account_handler):
        """
        Initializes the AccountService with an AccountHandler.

        ## Parameters:
        - account_handler [AccountHandler]: The handler that manage accounts.
        """
        self.account_handler = account_handler

    def reset(self):
        """
        Clear all store accounts.

        ## Returns:
        - None
        """
        self.account_handler.accounts = {}

    def get(self, account_id):
        """
        Retrieves the account by its ID.

        ## Parameters:
        - account_id [string]: The ID of the account to retrieve.

        ## Returns:
        - Account object if the account exists, otherwise None.
        """
        return self.account_handler.get_account(account_id)

    def deposit(self, destination, amount):
        """
        Deposits an amount into the destination account.
        Creates the account if it does not exist.

        ## Parameters:
        - destination [string]: The ID of the account.
        - amount [integer]: The amount to deposit.

        ## Returns:
        - Account object with the updated balance.
        """
        return self.account_handler.create_or_update_account(
            destination, amount
        )

    def withdraw(self, origin, amount):
        """
        Withdraws an amount from the account.

        ## Parameters:
        - origin [string]: The ID of the account.
        - amount [integer]: The amount to withdraw.

        ## Returns:
        - Account object with the updated balance if the withdrawal is ok, otherwise None.
        """
        return self.account_handler.withdraw_from_account(origin, amount)

    def transfer(self, origin, amount, destination):
        """
        Transfers an amount from the one account to another.

        ## Parameters:
        - origin [string]: The ID of the origin account.
        - amount [integer]: The amount to transfer.
        - destination [string]: The ID of the destination account.

        ## Returns:
        - A tuple containing two Account objects: the origin account and the destination account.
        - If the transfer fails, returns (None, None).
        """
        return self.account_handler.transfer_between_accounts(
            origin, amount, destination
        )
