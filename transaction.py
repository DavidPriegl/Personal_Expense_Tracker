from collections import namedtuple

Transaction = namedtuple("Transaction", ["date", "category", 
                                         "amount", "type"])


if __name__ == "__main__":
    t = Transaction("2026-08-20", "Élelmiszer", 12500.0, "expense")
    print(t)
    print(t.category)
    print(t.amount)
    print(t[0])