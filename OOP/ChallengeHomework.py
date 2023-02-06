
'''For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.'''
class Account():

    def __init__(self,owner, balance=0):
        #the below two line code make those two argument as string
        # self.owner = f'Account owner:{owner}'# the space between words in single quote matters
        # self.balance = f'Account balance: ${balance}'
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print( f'Added {deposit_amount} to the balance')

    def withdraw(self,withdrawal_amount):

        if self.balance >= withdrawal_amount:
            self.balance = self.balance - withdrawal_amount
            print( 'Withdrawal accepted')
        else:
            print( 'Funds Unavailable')

    def __str__(self):#this is to print object of the class
        return f'Owner: {self.owner} \nBalance: {self.balance}'



accn1 = Account('jose', 200)
print(accn1.owner)#Account owner: jose
#print(accn1.owner, accn1.balance)#jose 200
print(accn1.balance)#Account balance: $200
# print(accn1.deposit(50))
# print(accn1.withdraw(75))
print(accn1.withdraw(500))

a =Account('Samm', 500)
print(a.owner)#sam
print(a.balance)#500
print(a.deposit(100))#Deposit accepted
print(a.balance)#600
print(a.withdraw(1))#Withdrawal accepted