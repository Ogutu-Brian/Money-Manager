from tkinter import messagebox
#item types that will be used for trsnsactions
item_types = ["food", "rent", "bills", "entertainment", "other"]


class MoneyManager(object):
    def __init__(self):
        '''Constructor to set username to '', pin_number to an empty string,
           balance to 0.0, and transaction_list to an empty list.'''
        self.user_number = -1
        self.pin_number = ''
        self.balance = 0.0
        self.transaction_list = []

    def add_entry(self, amount, entry_type):
        '''Function to add and entry an amount to the tool. Raises an
           exception if it receives a value for amount that cannot be cast to float. Raises an exception
           if the entry_type is not valid - i.e. not food, rent, bills, entertainment or other'''
        valid = True
        try:
            amount = float(amount)
        except:
            valid = False
            messagebox.showerror(
                "Transaction Error",
                "The amont cannot be cast to float"
            )
        if valid:
            if(entry_type.lower() not in item_types):
                raise Exception(
                    messagebox.showerror(
                        "Transaction Error",
                        "The item type is invalid"
                    )
                )
            else:
                if((self.balance - amount) < 0.0):
                    raise Exception(
                        messagebox.showerror(
                            "Transaction Error",
                            "You do not have sufficient funds to do the transaction"
                        )
                    )
                else:
                    self.balance -= amount
                    self.transaction_list.append(
                        (entry_type, amount)
                    )

    def deposit_funds(self, amount):
        '''Function to deposit an amount to the user balance. Raises an
           exception if it receives a value that cannot be cast to float. '''
        try:
            amount = float(amount)
            self.balance += amount
            self.transaction_list.append(("Deposit", amount))
            return True
        except:
            return False
    def get_transaction_string(self):
        '''Function to create and return a string of the transaction list. Each transaction
           consists of two lines - either the word "Deposit" or the entry type - food etc - on
           the first line, and then the amount deposited or entry amount on the next line.'''
        transaction_string = ""
        for item in self.transaction_list:
            transaction_string += item[0] + "\n"+str(item[1])+"\n"
        return transaction_string

    def save_to_file(self):
        '''Function to overwrite the user text file with the current user
           details. user number, pin number, and balance (in that
           precise order) are the first four lines - there are then two lines
           per transaction as outlined in the above 'get_transaction_string'
           function.'''
        file_name = str(self.user_number)+".txt"
        user_number = str(self.user_number)+"\n"
        pin_number = str(self.pin_number)+"\n"
        balance = str(self.balance)+"\n"
        file = open(file_name, "w")
        file.write(user_number)
        file.write(pin_number)
        file.write(balance)
        file.write(self.get_transaction_string())
        file.close()
