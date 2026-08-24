from ledger import Ledger

MENU = """
========================================
  Personal Expense Tracker
========================================
1. Add new transaction
2. List all transactions
3. Filter by category
4. Filter by month
5. View balance
6. Most common category
7. Monthly breakdown
0. Exit
"""


def main():
    ledger = Ledger()
    try:
        ledger.read_from_json()
    except FileNotFoundError:
        pass
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        try:
            if choice == "1":
                date = input("Date (YYYY-MM-DD): ").strip()
                category = input("Category: ").strip()
                amount = float(input("Amount: ").strip())
                t_type = input("Type (income/expense): ").strip()
                ledger.add_transaction(date, category, amount, t_type)
                print("Transaction added.")
            elif choice == "2":
                txs = ledger.list_transactions
                if not txs:
                    print("No transactions recorded.")
                else:
                    for t in txs:
                        print(f"{t.date}  {t.category}  {t.amount} {t.type}")
            elif choice == "3":
                category = input("Category: ").strip()
                print(ledger.filter_by_category(category))
            elif choice == "4":
                month = input("Month (MM or YYYY-MM) ").strip()
                print(ledger.filter_by_month(month))
            elif choice == "5":
                print(ledger.get_balance())
            elif choice == "6":
                print(ledger.most_common_category())
            elif choice == "7":
                result = ledger.group_by_month()
                print(result if result else "No transactions recorded.")
        except ValueError as e:
            print(f"Error: {e}")
        except IndexError:
            print("Error: not enough data.")
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
