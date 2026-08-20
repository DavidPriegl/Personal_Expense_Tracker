from transaction import Transaction
from collections import Counter, defaultdict

class Ledger:
    def __init__(self):
        self._transaction = []

    @property
    def list_transactions(self):
        return self._transaction

    def add_transaction(self, date, category, amount, t_type):
        if amount < 0:
            raise ValueError("Amount can't be negative.")
        
        if t_type not in ("income","expense"):
            raise ValueError("Type can only be income or expense.")

        self._transaction.append(Transaction(date, category, amount, t_type))

    def filter_by_category(self, category):
        if category not in (t.category for t in self._transaction):
            raise ValueError(f"{category} category not found.")
        category_transactions = [t for t in self._transaction if t.category == category]
        lines = [f"{t.date}  {t.category}  {t.amount} {t.type}" for t in category_transactions]
        return f"In the {category} category, these transactions are recorded:\n" + "\n".join(lines)

    def filter_by_month(self, month):
        month = f"{int(month):02d}"
        month_transactions = [t for t in self._transaction if t.date[5:7] == month]
        if not month_transactions:
            raise ValueError(f"{month}. month not found.")
        lines = [f"{t.date}  {t.category}  {t.amount} {t.type}" for t in month_transactions]
        return f"In the {month}. month, these transactions are recorded:\n" + "\n".join(lines)        





if __name__ == "__main__":
    ledger = Ledger()
    ledger.add_transaction("2026-08-20", "Food", 95.0, "expense")
    ledger.add_transaction("2026-08-19", "Salary", 3500.0, "income")
    ledger.add_transaction("2026-08-19", "Subscription", 10.0, "expense")
    ledger.add_transaction("2026-09-21", "Salary", 2500.0, "income")
    ledger.add_transaction("2026-09-08", "Subscription", 10.0, "expense")

    print(ledger.filter_by_category("Salary"))
    print('----------------------------------------')
    print(ledger.filter_by_month("08"))
    print('----------------------------------------')
    print(ledger.filter_by_month("9"))
    print('----------------------------------------')

    try:
        print(ledger.filter_by_category("Date"))
    except ValueError as e:
        print(e)
    print('----------------------------------------')

    try:
        print(ledger.filter_by_category("10"))
    except ValueError as e:
        print(e)
    print('----------------------------------------')

    try:
        ledger.add_transaction("2026-08-18", "Közlekedés", -500, "expense")
    except ValueError as e:
        print(e)
    print('----------------------------------------')

    try:
        ledger.add_transaction("2026-08-18", "Közlekedés", 500, "invoice")
    except ValueError as e:
        print(e)
    print('----------------------------------------')

