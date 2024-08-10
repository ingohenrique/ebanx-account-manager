class Account:
    """# Account object

    ## Parameters (required):
    - id [string]: users identification.
    ## Parameters (optional):
    - balance [integer]
    """

    def __init__(self, account_id, balance=0):
        self.balance = balance
        self.account_id = account_id

        
