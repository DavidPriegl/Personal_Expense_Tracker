# Personal Expense Tracker

A simple command-line Python application to track income and expenses, store transactions, and view basic financial summaries.

## Features

- Add transactions with:
  - date (`YYYY-MM-DD`)
  - category
  - amount
  - type (`income` or `expense`)
- List all recorded transactions
- Filter transactions by category
- Filter transactions by month
- Show current balance
- Show most common category
- Show grouped monthly breakdown
- Automatic JSON persistence

## Project Structure

- `main.py` – CLI menu and user interaction
- `ledger.py` – business logic and JSON read/write
- `transaction.py` – `Transaction` data structure

## Requirements

- Python 3.8+
- No external dependencies (standard library only)

## Getting Started

1. Clone the repository.
2. Open the project folder.
3. Run:

```bash
python main.py
```

## Menu Options

1. Add new transaction
2. List all transactions
3. Filter by category
4. Filter by month
5. View balance
6. Most common category
7. Monthly breakdown
0. Exit

## Data Storage

- Transactions are saved in `transaction.json` in the project root.
- Data is loaded automatically on startup (if the file exists).

## Input Rules

- Date must be in `YYYY-MM-DD` format.
- Amount must be greater than `0`.
- Type must be `income` or `expense`.

