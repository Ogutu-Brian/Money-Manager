import unittest
from tkinter import messagebox
from moneymanager import MoneyManager, item_types


class TestMoneyManager(unittest.TestCase):

    def setUp(self):
        self.user = MoneyManager()
        self.user.balance = 1000.0

    def test_legal_deposit_works(self):
        '''Tests that depositing money using the account's deposit funds function
        adds the amount to the balance'''
        self.user.deposit_funds(1000)
        self.assertEqual(2000, self.user.balance)

    def test_illegal_deposit_raises_exception(self):
        '''Tests that that depositing a value that is not a float results into 
        an exception being raised'''
        self.assertEqual(self.user.deposit_funds("4dssjd"), False)

    def test_legal_entry(self):
        '''Tests that adding a new entry with a legal amount subtracts the funds from 
        the balance'''
        self.user.add_entry(999, item_types[0])
        self.assertEqual(self.user.balance, 1)

    def test_illegal_entry_amount(self):
        pass

    def test_illegal_entry_type(self):
        pass

    def test_insufficient_funds_entry(self):
        pass


unittest.main()
