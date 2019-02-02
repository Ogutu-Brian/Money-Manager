import unittest
from tkinter import messagebox
from moneymanager import MoneyManager, item_types


class TestMoneyManager(unittest.TestCase):

    def setUp(self):
        self.user = MoneyManager()
        self.user.balance = 1000.0

    def test_legal_deposit_works(self):
        '''Tests if correct procedure for depositing funds works'''
        self.user.deposit_funds(1000)
        self.assertEqual(2000, self.user.balance)

    def test_illegal_deposit_raises_exception(self):
        pass

    def test_legal_entry(self):
        pass

    def test_illegal_entry_amount(self):
        pass

    def test_illegal_entry_type(self):
        pass

    def test_insufficient_funds_entry(self):
        pass


unittest.main()
