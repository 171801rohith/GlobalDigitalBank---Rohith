from services.account_manager import AccountManager
from services.transaction_manager import TransactionManager
from repositories.account_repository import AccountRepository


class AccountUI:
    def start(self):
        while True:
            print('\nWelcome to Global Digital Bank')
            print('\nSelect an option')
            print('1.Open Account')
            print('2.Close Account')
            print('3.Withdraw Funds')
            print('4.Deposit Funds')
            print('5.Transfer Funds')
            print('9.Exit')
            choice=int(input("Enter your choice:"))
            if choice==1:
                self.open_account()
            elif choice==2:
                self.close_account()
            elif choice==3:
                self.withdraw_funds()
            elif choice==4:
                self.deposit_funds()
            elif choice==5:
                self.transfer_funds()
            elif choice==9:
                break
            else:
                print('Invalid Choice. Please try again')
            
    def open_account(self):
        account_type=input('Enter account type (savings/current):').strip().lower()
        name=input('Enter your name:')
        amount=float(input('Enter initial deposit amount:'))
        pin_number=int(input('Enter your pin number:'))
        privilege=input('Enter account privilege(PREMIUM/GOLD/SILVER):').strip().upper()
        
        if account_type=='savings':
               date_of_birth=input('Enter your date of birth (YYYY-MM-DD):')
               gender=input('Enter your gender (M/F):')
               account=AccountManager().open_account(account_type,name=name,balance=amount,date_of_birth=date_of_birth,gender=gender,pin_number=pin_number,privilege=privilege)
               
        elif account_type=='current':
            registration_number=input('Enter your registration number:')
            website_url=input('Enter your website URL:')
            account=AccountManager().open_account(account_type,name=name,balance=amount,registration_number=registration_number,website_url=website_url,pin_number=pin_number,privilege=privilege)
            
        else:
            print('Invalid account type. Please try again')
            return
        
        print(account_type.capitalize(),'Account opened successfully. Account Number :',account.account_number)
    def close_account(self):
        account_number=int(input('Enter your Account Number:'))
        account=next((acc for acc in AccountRepository.accounts if acc.account_number==account_number),None)
        
        if account:
            try:
                AccountManager().close_account(account)
                print('Account Closed Successfully')
            except Exception as e:
                print('Error:',e)
        else:
            print('Account Not Found.Please try again')
    
    
    def withdraw_funds(self):
        account_number=int(input('Enter your Account Number:'))
        amount=float(input('Enter amount to Withdraw:'))
        pin_number=int(input('Enter your pin number :')) 
        account =next((acc for acc in AccountRepository.accounts if acc.account_number==account_number),None)
        
        if account:
            try:
                AccountManager().withdraw(account,amount,pin_number)
                print('Amount Withdrawn Successfully') 
            except Exception as e:
                print('Error :',e)      
            else:
                print('Account not found.Please Try Again')

    def deposit_funds(self):
        account_number=int(input('Enter your Account Number:'))
        amount=float(input('Enter amount to Deposit:'))
        account =next((acc for acc in AccountRepository.accounts if acc.account_number==account_number),None)

        if account:
            try:
                AccountManager.deposit(account,amount)
                print('Amount deposited Successfully')
            except Exception as e:
                print('Error :',e)
            else:
                print('Account Not Found. Please try again')
    def transfer_funds(self):
        from_accountnumber=int(input('Enter your Account Number:'))
        to_accountnumber=int(input('Enter the Account Number to transfer to:'))
        amount=float(input("Enter the amount to transfer to:"))
        pin_number=int(input('Enter the pin number:'))
        from_account=next((acc for acc in AccountRepository.accounts if acc.account_number==from_accountnumber),None)
        to_account=next((acc for acc in AccountRepository.accounts if acc.account_number==to_accountnumber),None)
        if from_account and to_account:
            try:
                AccountManager().transfer(from_accountnumber,to_accountnumber,amount,pin_number)
                print('Amount Transferred Successfully')
            except Exception as e:
                print('Error:',e)
            else:
                print('Account Not Found.Please Try again')