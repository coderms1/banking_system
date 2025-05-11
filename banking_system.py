# MINI BANKING SYSTEM ~ Capstone Project
# Coder: Sim

################################################################################
#  This program runs a simple little banking system with a menu that lets     ##
#    you do all the basics.  You can deposit, withdraw, check your balance,   ##
#     apply monthly interest, & even save your transaction history to a file. ##
#    Everything’s tracked in a list, fully validated, & printed out nice and  ##
#  clean. It keeps things simple, organized, & works almost like a real ATM!  ##
################################################################################

# FORMAT CURRENCY Function
def format_currency(amount):
    return f"{amount:>12,.2f}"

# PROMPT FOR INPUT Function
def prompt_for_num(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Enter a number that is > 0")
        except ValueError:
            print("Enter a valid number.")

# DEPOSIT Function
def deposit(balance, txn_list):
    value = prompt_for_num("Enter deposit amount: ")
    balance += value
    txn_list.append(("Deposited:", value))
    print(f"Deposit successful! New balance: ${format_currency(balance)}\n")
    return balance, txn_list

# WITHDRAW Function
def withdraw(balance, txn_list):
    value = prompt_for_num("Enter withdrawal amount: ")
    if value > balance:
        print("Insufficient Funds.\n")
    else:
        balance -= value
        txn_list.append(("Withdrew:", value))
        print(f"Withdrawal successful! New balance: ${format_currency(balance)}\n")
    return balance, txn_list

# CHECK BALANCE Function
def check_balance(balance):
    print(f"Your current balance is: ${format_currency(balance)}\n")

# VIEW TRANSACTION Function
def view_history(txn_list):
    print("\nTransaction History:")
    print("+----------------------+----------------+")
    if not txn_list:
        print(f"| No transactions yet. {' ':*15}|")
    else:
        for type, amt in txn_list:
            print(f"| {type:<20} ${format_currency(amt)} |")
    print("+----------------------+----------------+\n")

# APPLY INTEREST Function
def add_interest(balance, txn_list):
    if balance == 0:
        print("Balance is $0.00 — no interest will be applied.\n")
        return balance, txn_list
    rate = prompt_for_num("Enter interest rate: ")
    interest = balance * (rate / 100) / 12
    balance += interest
    txn_list.append(("Interest:", interest))
    print(f"Interest has been applied: ${format_currency(interest)} New balance: ${format_currency(balance)}\n")
    return balance, txn_list

# SAVE TO FILE Function
def save_to_file(balance, txn_list):
    file_name = "BankStatement.txt"
    _CONTENT_WIDTH_ = 30  # Smaller width for compact box

    # Calculate total deposited and withdrawn
    total_deposited = sum(amt for typ, amt in txn_list if typ == "Deposited:")  # Sum all deposit amounts
    total_withdrawn = sum(amt for typ, amt in txn_list if typ == "Withdrew:")  # Sum all withdrawal amounts

    with open(file_name, "w") as f:
        # Write header without box
        f.write(f"{'Zim`s Mini Bank':^30}\n")
        f.write(f"{'Transaction History':^30}\n")
        f.write("\n")

        # Write transaction history without box
        if not txn_list:
            f.write(f"{'No transactions yet.':^30}\n")
        else:
            for type, amt in txn_list:
                formatted_amt = format_currency(amt)
                f.write(f"{type:<12} ${formatted_amt.strip():>12}\n")
        f.write("\n")

        # Write boxed summary
        f.write(f"+{'-' * _CONTENT_WIDTH_}+\n")
        f.write(f"| {f'Total Deposited: ${format_currency(total_deposited).strip()}':<{_CONTENT_WIDTH_}} |\n")
        f.write(f"| {f'Total Withdrawn: ${format_currency(total_withdrawn).strip()}':<{_CONTENT_WIDTH_}} |\n")
        f.write(f"| {f'Balance: ${format_currency(balance).strip()}':<{_CONTENT_WIDTH_}} |\n")
        f.write(f"+{'-' * _CONTENT_WIDTH_}+\n")

    print(f"Transaction history saved to {file_name}\n")

# MAIN Function
def main():
    print("Welcome to Sim's Mini-Bank")
    # Begin
    balance = 0.0
    txn_list = []

    while True:
        print("""
1. Deposit Money
2. Withdraw Money
3. Check Balance
4. View Transaction History
5. Apply Interest Calculation
6. Save Transaction History and Exit
""")
        try:
            i_choice = int(input("Choose an option (1–6): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 6.\n")
            continue

        # ATM Choice menu
        match i_choice:
            case 1:
                balance, txn_list = deposit(balance, txn_list)
            case 2:
                balance, txn_list = withdraw(balance, txn_list)
            case 3:
                check_balance(balance)
            case 4:
                view_history(txn_list)
            case 5:
                balance, txn_list = add_interest(balance, txn_list)
            case 6:
                save_to_file(balance, txn_list)
                print("Thanks for using Zim's Mini Bank! Bank statement generated.\nGoodbye! Come back soon.")
                break
            case _:
                print("Invalid option. Please select from the menu.\n")

# Call main() funkytown
if __name__ == "__main__":
    main()
