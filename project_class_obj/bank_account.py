class BalanceException(Exception):
     pass

class BankAccount:
     def __init__(self,initialAmount,accName):
          self.balance = initialAmount
          self.name = accName
          print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

     def getBalances(self):
          print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

     def deposit(self,amount):
          self.balance = self.balance + amount
          print(f"\n Deposit Completed.")
          self.getBalances()

     def viableTransation(self,amount):
          if self.balance >= amount:
               return
          else:
               raise BalanceException(
                    f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
               )
     
     def withdraw(self,amount):
          try:
               self.viableTransation(amount)
               self.balance = self.balance - amount
               print("\nWithdraw complete.")
               self.getBalances()
          except BalanceException as error:
               print(f"\nWithdraw interrupted: {error}")

     def transfer(self,amount,account):
          try:
               print(f"******\n\nBegining Transfer..")
               self.viableTransation(amount)
               self.withdraw(amount)
               account.deposit(amount)
               print(f"\nTransfer complete!\n\n*********")
          except BalanceException as error:
               print(f"\nTransfer interupted. {error}" )

          
class InterestRewardAcct(BankAccount):
     def deposit(self, amount):
          self.balance = self.balance + (amount * 1.05)
          print("\nDeposit completed")
          self.getBalances()



class Savingcct(InterestRewardAcct):
    def __init__(self,initialAmount,accName):
         super().__init__(initialAmount,accName)
         self.fee = 5

    def withdraw(self, amount):
         try:
              self.viableTransation(amount + self.fee)
              self.balance = self.balance - (amount + self.fee)
              print("\nWithdraw completed.")
              self.getBalances()
         except BalanceException as error:
              print(f"\n Wothdraw interrupted: {error}")


