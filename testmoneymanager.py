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
        '''Tets that withdrawing an illegal amount raises an exception'''
        valid_input, valid_type, correct_amount = self.user.add_entry(
            'banana', item_types[1])
        self.assertEqual(
            (valid_input, valid_type, correct_amount), (False, True, True))

    def test_illegal_entry_type(self):
        '''Tests that adding illegal entry type raises an exception'''
        valid_input, valid_type, correct_amount = self.user.add_entry(
            90, 'banana')
        self.assertEqual(
            (valid_input, valid_type, correct_amount), (True, False, True))

    def test_insufficient_funds_entry(self):
        pass


unittest.main()
