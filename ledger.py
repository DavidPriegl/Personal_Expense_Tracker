from transaction import Transaction
from collections import Counter, defaultdict
import json

class Ledger:
    def __init__(self):
        self._transaction = []

    @property
    def list_transactions(self):
        return list(self._transaction)

    def add_transaction(self, date, category, amount, t_type):
        if amount <= 0:
            raise ValueError("Amount can't be negative.")
        
        if t_type.lower() not in ("income","expense"):
            raise ValueError("Type can only be income or expense.")

        self._transaction.append(Transaction(date, category.lower(), amount, t_type.lower()))
        self.write_to_json()

    def filter_by_category(self, category):
        if category.lower() not in (t.category for t in self._transaction):
            raise ValueError(f"{category} category not found.")
        category_transactions = [t for t in self._transaction if t.category == category.lower()]
        lines = [f"{t.date}  {t.category}  {t.amount} {t.type}" for t in category_transactions]
        return f"In the {category} category, these transactions are recorded:\n" + "\n".join(lines)

    def filter_by_month(self, month):
        month = f"{int(month):02d}"
        month_transactions = [t for t in self._transaction if t.date[5:7] == month]
        if not month_transactions:
            raise ValueError(f"{month}. month not found.")
        lines = [f"{t.date}  {t.category}  {t.amount} {t.type}" for t in month_transactions]
        return f"In the {month}. month, these transactions are recorded:\n" + "\n".join(lines) 

    def get_balance(self):
        balance = 0
        for t in self._transaction:
            if t.type == 'expense':
                balance -= t.amount
            else:
                balance += t.amount
        return f"Wallet balance: {balance} $"

    def most_common_category(self):
        if len(self._transaction) == 0:
            return 'No transaction found.'
        categorys = [t.category for t in self._transaction]
        counter = Counter(categorys)
        return f"Your most common category is '{counter.most_common(1)[0][0]}'"

    def group_by_month(self):
        groups = defaultdict(list)
        for t in self._transaction:
            groups[t.date[:7]].append(t)
        parts = []
        for month in sorted(groups):
            lines = [f"{t.date}  {t.category}  {t.amount} {t.type}" for t in groups[month]]
            parts.append(f"{month}. month:\n" + "\n".join(lines))
        return "\n\n".join(parts)

    def write_to_json(self):
        data = [t._asdict() for t in self._transaction]
        with open('transaction.json', 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def read_from_json(self):
        with open('transaction.json', 'r') as file:
            data = json.load(file)
            self._transaction = [Transaction(**item) for item in data]

if __name__ == "__main__":
    ledger = Ledger()
    ledger.add_transaction("2026-08-20", "Food", 95.0, "expense")
    ledger.add_transaction("2026-08-19", "Salary", 3500.0, "income")
    ledger.add_transaction("2026-08-19", "Subscription", 10.0, "expense")
    ledger.add_transaction("2026-09-21", "Salary", 2500.0, "income")
    ledger.add_transaction("2026-09-08", "Subscription", 10.0, "expense")
    ledger.add_transaction("2026-10-06", "Entertainment", 15.0, "expense")

    print(ledger.filter_by_category("Salary"))
    print('----------------------------------------')
    print(ledger.filter_by_month("08"))
    print('----------------------------------------')
    print(ledger.filter_by_month("9"))
    print('----------------------------------------')
    print(ledger.get_balance())
    print('----------------------------------------')
    print(ledger.most_common_category())
    print('----------------------------------------')
    print(ledger.group_by_month())
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

