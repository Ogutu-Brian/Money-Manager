import unittest
from tkinter import messagebox
from moneymanager import MoneyManager


class TestMoneyManager(unittest.TestCase):

    def setUp(self):
        self.user = MoneyManager()
        self.user.balance = 1000.0

    def test_legal_deposit_works(self):
    def test_illegal_deposit_raises_exception(self):
    def test_legal_entry(self):
    def test_illegal_entry_amount(self):
    def test_illegal_entry_type(self):
    def test_insufficient_funds_entry(self):


unittest.main()
