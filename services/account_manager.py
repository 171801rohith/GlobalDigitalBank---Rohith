# Open Account
# Close account
# Withdrawal
# Deposit
# Check is account is active
# transfer
# Validate pin number
# Close account

from models.savings import Savings
from models.current import Current
from repositories.account_repository import AccountRepository
from exceptions.exception import *
from services.transaction_manager import TransactionManager
from services.account_privileges_manager import AccountPrivilegesManager


class AccountManager:
    # kwargs = keyword arguements (U can pass more arguments than mentioned in declaration)
    def open_account(self, account_type, **kwargs):
        if account_type == "savings":
            new_account = Savings(**kwargs)

        elif account_type == "current":
            new_account = Current(**kwargs)
        else:
            raise ValueError("Invalid Account Type")

        AccountRepository.save_account(new_account)
        return new_account

    def check_account_active(self, account):
        if not account.is_active:
            raise AccountNotActiveException("Account is not  active")

    def validate_pin(self, account, pin_number):
        if account.pin_number != pin_number:
            raise InvalidPinException("invalid Pin Number")

    def withdraw(self, account, amount, pin_number):
        self.check_account_active(account)
        self.validate_pin(account, pin_number)

        if amount.balance < amount:
            raise InsufficientFundsException("insufficient funds")

        amount -= amount.balance
        TransactionManager.log_transaction(account.account_number, amount, "Withdraw")

    def deposit(self, account, amount):
        self.check_account_active(account)
        account.balance += amount.balance
        TransactionManager.log_transaction(account.account_number, amount, "Deposit")

    def transfer(self, from_account, to_account, amount, pin_number):
        self.check_account_active(from_account)
        self.check_account_active(to_account)
        self.validate_pin(from_account, pin_number)

        if from_account.balance < amount:
            raise InsufficientFundsException("insufficient funds")

        limit = AccountPrivilegesManager.get_limit(from_account.privilege)

        if amount > limit:
            raise TransferLimitExceededException("Transaction Limit Exceeded")

        from_account.balance -= amount
        to_account.balance += amount
        TransactionManager.log_transaction(
            from_account.account_number, amount, "Transfer", to_account.account_number
        )


    def close_account(self,account):
        if not account.is_active:
            raise AccountNotActiveException('Account is already Deactivated')