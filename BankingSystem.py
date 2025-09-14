# banking_system.py

import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# File to store account details
DATA_FILE = "accounts.txt"


# --- Helper Functions ---
def load_accounts():
    """Load accounts from file into a dictionary."""
    accounts = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                acc_no, name, balance = line.strip().split(",")
                accounts[acc_no] = {"name": name, "balance": float(balance)}
    return accounts


def save_accounts(accounts):
    """Save accounts dictionary back to file."""
    with open(DATA_FILE, "w") as f:
        for acc_no, details in accounts.items():
            f.write(f"{acc_no},{details['name']},{details['balance']}\n")


# --- Banking Operations ---
def create_account(accounts):
    acc_no = input(Fore.CYAN + "Enter Account Number: ")
    if acc_no in accounts:
        print(Fore.RED + "Account already exists!")
        return
    name = input(Fore.CYAN + "Enter Account Holder Name: ")
    balance = float(input(Fore.CYAN + "Enter Initial Deposit: "))
    accounts[acc_no] = {"name": name, "balance": balance}
    save_accounts(accounts)
    print(Fore.GREEN + " Account created successfully!")


def deposit(accounts):
    acc_no = input(Fore.CYAN + "Enter Account Number: ")
    if acc_no not in accounts:
        print(Fore.RED + "Account not found!")
        return
    amount = float(input(Fore.CYAN + "Enter Deposit Amount: "))
    accounts[acc_no]["balance"] += amount
    save_accounts(accounts)
    print(Fore.GREEN + f" Deposit successful! New Balance: {accounts[acc_no]['balance']}")


def withdraw(accounts):
    acc_no = input(Fore.CYAN + "Enter Account Number: ")
    if acc_no not in accounts:
        print(Fore.RED + "Account not found!")
        return
    amount = float(input(Fore.CYAN + "Enter Withdrawal Amount: "))
    if accounts[acc_no]["balance"] < amount:
        print(Fore.RED + " Insufficient balance!")
    else:
        accounts[acc_no]["balance"] -= amount
        save_accounts(accounts)
        print(Fore.GREEN + f" Withdrawal successful! New Balance: {accounts[acc_no]['balance']}")


def check_balance(accounts):
    acc_no = input(Fore.CYAN + "Enter Account Number: ")
    if acc_no not in accounts:
        print(Fore.RED + "Account not found!")
        return
    print(Fore.YELLOW + f" Account Holder: {accounts[acc_no]['name']}")
    print(Fore.YELLOW + f" Balance: {accounts[acc_no]['balance']}")


# --- Main Menu ---
def main():
    accounts = load_accounts()

    while True:
        print(Style.BRIGHT + Fore.MAGENTA + "\n===== Banking System Menu =====")
        print(Fore.BLUE + "1. Create Account")
        print(Fore.BLUE + "2. Deposit Money")
        print(Fore.BLUE + "3. Withdraw Money")
        print(Fore.BLUE + "4. Check Balance")
        print(Fore.BLUE + "5. Exit")

        choice = input(Fore.CYAN + "Enter your choice: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            print(Fore.GREEN + "👋 Thank you for using the Banking System!")
            break
        else:
            print(Fore.RED + " Invalid choice! Try again.")


if __name__ == "__main__":
    main()
