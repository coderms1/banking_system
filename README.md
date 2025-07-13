# Sim's Mini-Bank 💵

A clean little command-line banking app built in Python. 
It’s simple, structured, and works like a tiny ATM — deposit money, 
make withdrawals, check your balance, calculate interest, 
and save your transaction history to a file.

You’ll get some smooth terminal output *and* a crispy `.txt` statement when you're done!

---

## 🚀 Features

- **Real-world flow**: deposit, withdraw, check balance, view history, apply interest, and save + exit
- **Data Structures**: Lists + tuples to track transactions
- **File Handling**: Generates a clean `BankStatement.txt` on exit
- **String Formatting**: f-strings + alignment to make things look tight
- **Control Flow**: while loops, match-case, if/else logic
- **Functions**: All modular, return-based and readable
- **Error Handling**: try/except guards for clean input
- **Output Formatting**: ASCII box, formatted transaction rows

---

## 🛠️ Installation

git clone https://github.com/coderms1/banking_system.git

Make sure you're running Python 3.6+:
No extra dependencies — runs with pure Python standard library.

```bash

🧑‍💻 Usage
Run the program:

python banking_system.py

Use the menu to:

- Deposit Money
- Withdraw Money
- Check Balance
- View Transaction History
- Apply Monthly Interest
- Save & Exit

Just follow the prompts and enter amounts/rates when asked.
The app handles all input/data validation.

📄 Output
Transaction history prints cleanly to the console, and when you choose option 6, a .txt file (BankStatement.txt) is created with a full summary.

Example output:

        Sim's Mini Bank        
     Transaction History       

Deposited:   $ 500.00
Withdrew:    $ 200.00
Interest:    $ 2.50

+------------------------------+
| Total Deposited: $ 500.00   |
| Total Withdrawn: $ 200.00   |
| Balance:        $ 302.50    |
+------------------------------+

📁 File Structure

Main-Directory/
├── banking_system.py       # Main script
├── BankStatement.txt     # Auto-generated on exit
└── README.md             # This file

🙌 Contributing
Support your local build0rs.

📬 Contact
@coderms1 on Github =]

---
