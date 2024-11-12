class AccountRepository:
    account = []
    account_counter = 1000

    # Method to generate new account number
    # classmethod
    # Used to define a method which is limited to this class. self is not required. Calling a class without obj
    # 1. class-level access: classmethod can access and modify the class-level attributes
    # 2. Changes made in classmethod will reflect on all instance of class (shared across all instances of class)
    # 3. classmethod takes cls as first arg, normal method takes self as first arg, static take nothing as first arg
    @classmethod 
    def generate_account_number(cls):
        cls.account_counter += 1
        return cls.account_counter

    # Method to save account 
    @classmethod
    def save_account(cls, account):
        cls.account.append(account)

    # Method to get all account 
    def get_account(self):
        return self.account