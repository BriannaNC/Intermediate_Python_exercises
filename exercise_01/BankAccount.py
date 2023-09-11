class BankAccount:
    #Bank account with a name and starting balance
    account_name: str
    account_balance: float
    def __init__( self,account_name: str, starting_balance: float ):
        self.account_name=account_name
        self.account_balance=starting_balance
    def Deposit(self,cash:float):
        self.account_balance=self.account_balance+cash
    def Withdrawl(self,cash:float):
        self.account_balance=self.account_balance-cash
    def GetBalance(self):
        balance_statement= print(self.account_name , "has a balance of $", self.account_balance)
        return balance_statement