**Sim's Mini-Bank**

# Description
A simple command-line banking system implemented in Python, allowing users to manage deposits, 
withdrawals, balance checks, transaction history, interest calculations, and save transaction summaries to a file.

# Features

     Data Structures: Lists (txn_list), tuples (transaction records).
     String Methods: f-strings, strip(), alignment specifiers (:<n, :>n, :^n).
     File Handling: open(), write() with context manager.
     Control Flow: while, for, if/else, match.
     Functions: Modular functions with return values, built-in functions (sum, len, etc.).
     Exception Handling: try/except for input validation.
     Formatting: ASCII box drawing, table formatting.


# **Installation**

Clone the Repository:
git clone https://github.com/your-username/zims-mini-bank.git
cd zims-mini-bank

Ensure Python 3 is Installed:

The program requires Python 3.6 or higher.
Check your Python version:python3 --version

If not installed, download from python.org.

No External Dependencies:

The program uses only Python's standard library.


# **Usage**

Run the Program:python3 bank_program.py

# Interact with the Menu:
     1-Deposit Money: Add funds to your account
     2-Withdraw Money: Remove funds if sufficient balance exists
     3-Check Balance: View the current account balance
     4-View Transaction History: Display all transactions (deposits, withdrawals, interest)
     5-Apply Interest: Calculate and add monthly interest based on a user-provided rate
     6-Save and Exit: Save transaction summary to BankStatement.txt and exit the program

     [Enter numerical inputs as prompted (e.g., amounts, interest rates)]


# **Output:**
Transactions are displayed on the console.
On exit (option 6), a BankStatement.txt file is generated with a summary, including total deposited, total withdrawn, and balance in a boxed format.


      **Example BankStatement.txt:
            Zim`s Mini Bank      
         Transaction History     
      
      Deposited:   $      500.00
      Withdrew:    $      200.00
      Interest:    $        2.50
      
      +------------------------------+
      | Total Deposited: $500.00     |
      | Total Withdrawn: $200.00     |
      | Balance: $302.50             |
      +------------------------------+
      **

# **File Structure**
      zims-mini-bank/
      ├── bank_program.py       # Main Python script for the banking system
      ├── BankStatement.txt     # Generated file with transaction summary (created on exit)
      └── README.md             # This file
      

# **Contributing**
Support your local build0rs.


# **Fork the repository.**
Create a new branch (git checkout -b feature/your-feature).
Make changes and commit (git commit -m "Add your feature").
Push to your branch (git push origin feature/your-feature).
Open a pull request.


# **Contact**
For questions or feedback, open an issue on the GitHub repository or contact coder-zim on GitHub.
