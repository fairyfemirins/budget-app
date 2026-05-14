# Budget App

A minimal, open-source budgeting tool for tracking monthly expenses and income. Built with Python and SQLite for simplicity and portability.

## Features (MVP)
- Add, edit, and delete transactions (expenses/income).
- Categorize transactions (e.g., Food, Rent, Entertainment).
- Set monthly budget limits per category.
- View monthly summaries and spending trends.
- Export data to CSV.

## Technical Architecture

### Database Schema
```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    type TEXT CHECK(type IN ('expense', 'income')) NOT NULL
);

CREATE TABLE budgets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT UNIQUE NOT NULL,
    budget_limit REAL NOT NULL
);
```

### Core Functions
| Function               | Description                                      |
|------------------------|--------------------------------------------------|
| `init_db()`            | Initialize the SQLite database.                  |
| `add_transaction()`    | Add a new transaction.                           |
| `get_transactions()`   | Retrieve transactions (filtered by month/year).  |
| `set_budget()`         | Set a budget limit for a category.               |
| `get_budget()`         | Retrieve the budget limit for a category.        |
| `export_to_csv()`      | Export transactions to a CSV file.               |

### CLI Usage
```bash
# Add a transaction
python3 cli.py add "2026-05-14" "Groceries" 50.0 "Food" "expense"

# List all transactions
python3 cli.py list

# Set a budget limit
python3 cli.py budget "Food" 500.0

# Export data to CSV
python3 cli.py export budget_data.csv
```

## Roadmap
- Web interface (Flask/Django).
- Bank API integrations (Plaid, Yodlee).
- Mobile app (React Native).
- Subscription-based cloud sync.

## License
MIT