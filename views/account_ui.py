from services.account_manager import AccountManager
from services.transaction_manager import TransactionManager
from repositories.account_repository import AccountRepository


class AccountUI:
    def start(self):
        while True:
            print("\t\t\t\tWelcome to Global Digital Banking\n")
            print("\nSelect an option :")
            print("1. Open Account")
            print("2. Close Account")
            print("3. Withdraw Funds")
            print("4. Deposit Funds")
            print("5. Transfer Funds")
            print("9. Exit")

            choice = int(input("Enter your Choice : "))

            match choice:
                case 1:
                    self.open_account()
                case 2:
                    self.close_account()
                case 3:
                    self.withdraw_funds()
                case 4:
                    self.deposit_funds()
                case 5:
                    self.transfer_funds()
                case 9:
                    break
                case _:
                    print("Invalid Choice")

    def open_account(self):
        account_type = (
            input("Enter account type (savings / current) : ").strip().lower()
        )
        name = input("Enter your name : ")
        amount = float(input("Enter initial deposit amount : "))
        pin_number = input("Enter your pin :")
        privilege = (
            input("Enter account privilege (PREMIUM/GOLD/SILVER) : ").strip().upper()
        )

        if account_type == "savings":
            date_of_birth = input("Enter date of birth (YYYY-MM-DD) : ")
            gender = input("Enter gender (M/F) : ")
            account = AccountManager().open_account(
                account_type,
                name=name,
                balance=amount,
                date_of_birth=date_of_birth,
                gender=gender,
                pin_number=pin_number,
                privilege=privilege,
            )
        elif account_type == "current":
            registration_number = input("Enter registration number : ")
            website_url = input("Enter website URL : ")
            account = AccountManager().open_account(
                account_type,
                name=name,
                balance=amount,
                registration_number=registration_number,
                website_url=website_url,
                pin_number=pin_number,
                privilege=privilege
            )

        else:
            print("Invalid Account type. Please try again")
            return

        print(
            account_type.capitalize(),
            "Account opened successfully. Account Number :",
            account.account_number,
        )

    def close_account(self):
        account_number = int(input("Enter account number : "))
        account = next(
            (
                acc
                for acc in AccountRepository.account
                if acc.account_number == account_number
            ),
            None,
        )
        if account:
            try:
                AccountManager().close_account(account)
                print("Account closed successfully")
            except Exception as e:
                print("Error :", e)
        else:
            print("Account not found. Please try again")

    def withdraw_funds(self):
        account_number = int(input("Enter account number : "))
        amount = float(input("Enter amount to withdraw : "))
        pin_number = input("Enter your pin :")
        account = next(
            (
                acc
                for acc in AccountRepository.account
                if acc.account_number == account_number
            ),
            None,
        )

        if account:
            try:
                AccountManager().withdraw(account, amount, pin_number)
                print("Funds withdrawn successfully")
            except Exception as e:
                print("Error :", e)
        else:
            print("Account not found. Please try again")

    def deposit_funds(self):
        account_number = int(input("Enter account number : "))
        amount = float(input("Enter amount to deposit : "))
        account = next(
            (
                acc
                for acc in AccountRepository.account
                if acc.account_number == account_number
            ),
            None,
        )

        if account:
            try:
                AccountManager().deposit(account, amount)
                print("Funds deposited successfully")
            except Exception as e:
                print("Error :", e)
        else:
            print("Account not found. Please try again")

    def transfer_funds(self):
        from_account_number = int(input("Enter from account number : "))
        to_account_number = int(input("Enter to account number : "))
        amount = float(input("Enter amount to transfer : "))
        pin_number = int(input("Enter pin number : "))
        to_account = next(
            (
                acc
                for acc in AccountRepository.account
                if acc.account_number == to_account_number
            ),
            None,
        )
        from_account = next(
            (
                acc
                for acc in AccountRepository.account
                if acc.account_number == from_account_number
            ),
            None,
        )

        if from_account and to_account:
            try:
                AccountManager().transfer(from_account, to_account, amount, pin_number)
                print("Funds transferred successfully")
            except Exception as e:
                print("Error :", e)
        else:
            print("One or both Account(s) not found. Please try again")
