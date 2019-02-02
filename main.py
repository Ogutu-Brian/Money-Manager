import tkinter as tk
from tkinter import (messagebox, StringVar, Label, LEFT,
                     DISABLED, NORMAL, Button, OptionMenu, Scrollbar)
from pylab import plot, show, xlabel, ylabel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from collections import defaultdict
from pprint import pprint
import matplotlib.pyplot as plt
from moneymanager import MoneyManager, item_types

win = tk.Tk()
# The user number and associated variable
user_number_var = tk.StringVar()

# This is set as a default for ease of testing
user_number_var.set('123456')
user_number_entry = tk.Entry(win, textvariable=user_number_var)
user_number_entry.focus_set()

# The pin number entry and associated variables
pin_number_var = tk.StringVar()
# This is set as a default for ease of testing
pin_number_var.set('7890')
user_pin_entry = tk.Entry(win, text='PIN Number',
                          textvariable=pin_number_var, show="*")

# set the user file by default to an empty string
user_file = ''

# The balance label and associated variable
balance_var = tk.StringVar()
balance_var.set('Balance: $0.00')
balance_label = tk.Label(win, textvariable=balance_var)

# The Entry widget to accept a numerical value to deposit or withdraw
#amount_var = tk.StringVar()
tkVar = StringVar(win)
amount_entry = tk.Entry(win)
entry_type = tk.Entry(win)

# The transaction text widget holds text of the transactions
transaction_text_widget = tk.Text(win, height=10, width=48)

# The money manager object we will work with
user = MoneyManager()


def clear_pin_entry(event):
    '''Function to clear the PIN number entry when the Clear / Cancel button is clicked.'''
    pin_number_var.set('')


def handle_pin_button(event):
    '''Function to add the number of the button clicked to the PIN number entry.'''
    pin_string = pin_number_var.get()
    button_argument = event.widget['text']
    if(len(pin_string) < 4):
        user_pin_entry.insert(len(pin_string), button_argument)


def log_in(event):
    '''Function to log in to the banking system using a known user number and PIN.'''
    global user
    global pin_number_var
    global user_file
    global user_number_var
    filename = user_number_var.get()+".txt"
    file = None
    user_exists = True
    try:
        file = open(filename, "r")
    except:
        messagebox.showinfo("Error", "Invalid user number, please try again!")
        user = MoneyManager()
        user_pin_entry.focus_set()
        pin_number_var.set('')
        user_exists = False
    if user_exists:
        file_info_list = file.read().split('\n')
        file.close()
        user.user_number = file_info_list[0]
        user.pin_number = file_info_list[1]
        user.balance = file_info_list[2]
        if user.pin_number != pin_number_var.get():
            user = MoneyManager()
            raise Exception(
                messagebox.showinfo("Error", "Invalid pin number")
            )
        else:
            counter = 0
            item_list = []
            amount_list = []
            for item in file_info_list[3:]:
                if(counter % 2 == 0 and item.strip()):
                    item_list.append(item)
                elif(item.strip()):
                    amount_list.append(float(item))
                counter += 1
            counter = 0
            while counter < len(item_list):
                user.transaction_list.append((
                    item_list[counter],
                    amount_list[counter]
                ))
                counter += 1
            remove_all_widgets()
            create_user_screen()


def save_and_log_out():
    '''Function  to overwrite the user file with the current state of
       the user object (i.e. including any new transactions), remove
       all widgets and display the login screen.'''
    global user


def perform_deposit():
    '''Function to add a deposit for the amount in the amount entry to the
       user's transaction list.'''
    global user
    global amount_entry
    global balance_label
    global balance_var


def perform_transaction():
    '''Function to add the entry the amount in the amount entry from the user balance and add an entry to the transaction list.'''
    global user
    global amount_entry
    global balance_label
    global balance_var
    global entry_type


def remove_all_widgets():
    '''Function to remove all the widgets from the window.'''
    global win
    for widget in win.winfo_children():
        widget.grid_remove()


def read_line_from_user_file():
    '''Function to read a line from the users file but not the last newline character.
       Note: The user_file must be open to read from for this function to succeed.'''
    global user_file
    return user_file.readline()[0:-1]


def plot_spending_graph():
    '''Function to plot the user spending here.'''


def create_login_screen():
    '''Function to create the login screen.'''
    win.geometry('500x660')
    win.winfo_toplevel().title('FedUni Money Manager')
    Label(text="FedUni Money Manager", font=("Helvetica", 28)).grid(
        row=0, column=0, columnspan=3)
    Label(text="User Number/ PIN", font=("Helvetica", 15),
          justify=LEFT).grid(row=1, column=0)
    user_number_entry.grid(row=1, column=1)
    user_pin_entry.grid(row=1, column=2)
    button1 = Button(text="1", width=8, height=4)
    button1.grid(row=2, column=0)
    button1.bind('<Button-1>', handle_pin_button)
    button2 = Button(text="2", width=8, height=4)
    button2.grid(row=2, column=1)
    button2.bind('<Button-1>', handle_pin_button)
    button3 = Button(text="3", width=8, height=4)
    button3.grid(row=2, column=2)
    button3.bind('<Button-1>', handle_pin_button)
    button4 = Button(text="4", width=8, height=4)
    button4.grid(row=3, column=0)
    button4.bind('<Button-1>', handle_pin_button)
    button5 = Button(text="5", width=8, height=4)
    button5.grid(row=3, column=1)
    button5.bind('<Button-1>', handle_pin_button)
    button6 = Button(text="6", width=8, height=4)
    button6.grid(row=3, column=2)
    button6.bind('<Button-1>', handle_pin_button)
    button7 = Button(text="7", width=8, height=4)
    button7.grid(row=4, column=0)
    button7.bind('<Button-1>', handle_pin_button)
    button8 = Button(text="8", width=8, height=4)
    button8.grid(row=4, column=1)
    button8.bind('<Button-1>', handle_pin_button)
    button9 = Button(text="9", width=8, height=4)
    button9.grid(row=4, column=2)
    button9.bind('<Button-1>', handle_pin_button)
    cancel_button = Button(text="Cancel/Clear", width=8,
                           height=4, bg="red", activebackground="red")
    cancel_button.grid(row=5, column=0)
    cancel_button.bind('<Button-1>', clear_pin_entry)
    button0 = Button(text="0", width=8, height=4)
    button0.grid(row=5, column=1)
    button0.bind('<Button-1>', handle_pin_button)
    login_button = Button(text="Log In", width=8, height=4,
                          bg="green", activebackground="green")
    login_button.grid(row=5, column=2)
    login_button.bind('<Button-1>', log_in)


def create_user_screen():
    '''Function to create the user screen.'''
    global amount_text
    global amount_label
    global transaction_text_widget
    global balance_var
    win.geometry('500x660')
    Label(text="FedUni Money Manager", font=(
        "Helvetica", 22)).grid(row=0, columnspan=5)
    Label(text="User Number:"+" "+user.user_number,
          font=("Helvetica")).grid(row=1, column=0)
    balance_var.set("Balance: $"+user.balance)
    balance_label.grid(row=1, column=1)
    Label(text="AMount ($)", font=("Helvetica")).grid(row=2, column=0)
    Label(text="Entry Type", font=("Helvetica")).grid(row=3, column=0)
    logout_button = Button(text="Log Out", width=8, height=4)
    logout_button.grid(row=1, column=3)
    deposit_button = Button(text="Deposit", width=8, height=4)
    deposit_button.grid(row=2, column=3)
    entry_button = Button(text="Add Entry", width=8, height=4)
    entry_button.grid(row=3, column=3)
    amount_entry.grid(row=2, column=1)
    tkVar.set("Choose Entry")
    choices = set(item_types)
    item_menu = OptionMenu(win, tkVar, *choices)
    item_menu.grid(row=3, column=1)
    transaction_text_widget.grid(row=4, column=0, columnspan=5)
    scrollbar = Scrollbar(win, command=transaction_text_widget.yview)
    scrollbar.grid(row=4, column=4, sticky='nsew')
    transaction_text_widget['yscrollcommand'] = scrollbar.set
    transaction_text_widget.config(state=DISABLED)


create_login_screen()
win.mainloop()
