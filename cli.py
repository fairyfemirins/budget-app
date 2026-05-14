#!/usr/bin/env python3

import sys
from budget import (
    add_transaction, get_transactions, set_budget, get_budget, export_to_csv
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 cli.py <command> [args]")
        print("Commands:")
        print("  add <date> <description> <amount> <category> <type> (type: expense/income)")
        print("  list [month] [year]")
        print("  budget <category> <limit>")
        print("  export <filename>")
        return

    command = sys.argv[1]

    if command == "add":
        date = sys.argv[2]
        description = sys.argv[3]
        amount = float(sys.argv[4])
        category = sys.argv[5]
        type_ = sys.argv[6]
        add_transaction(date, description, amount, category, type_)
        print("Transaction added.")

    elif command == "list":
        month = int(sys.argv[2]) if len(sys.argv) > 2 else None
        year = int(sys.argv[3]) if len(sys.argv) > 3 else None
        transactions = get_transactions(month, year)
        for t in transactions:
            print(f"{t[0]} | {t[1]} | {t[2]} | {t[3]:.2f} | {t[4]} | {t[5]}")

    elif command == "budget":
        category = sys.argv[2]
        limit = float(sys.argv[3])
        set_budget(category, limit)
        print(f"Budget set for {category}: {limit:.2f}")

    elif command == "export":
        filename = sys.argv[2]
        export_to_csv(filename)
        print(f"Data exported to {filename}.")


if __name__ == "__main__":
    main()