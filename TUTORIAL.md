# Budget App: Reproducible Tutorial

## 1. Prerequisites
- Python 3.8+
- SQLite3 (included with Python)

---

## 2. Setup
```bash
# Clone the repository
git clone https://github.com/femirins/budget-app.git
cd budget-app
```

---

## 3. Initialize the Database
```bash
python3 budget.py
```

---

## 4. Add Transactions
```bash
# Add an expense
python3 cli.py add "2026-05-14" "Groceries" 50.0 "Food" "expense"

# Add income
python3 cli.py add "2026-05-14" "Salary" 3000.0 "Income" "income"
```

---

## 5. Set Budget Limits
```bash
python3 cli.py budget "Food" 500.0
```

---

## 6. List Transactions
```bash
# List all transactions
python3 cli.py list

# List transactions for a specific month/year
python3 cli.py list 5 2026
```

---

## 7. Export Data
```bash
python3 cli.py export budget_data.csv
```

---

## 8. Verify the Output
```bash
cat budget_data.csv
```

Expected output:
```csv
ID,Date,Description,Amount,Category,Type
1,2026-05-14,Groceries,50.0,Food,expense
2,2026-05-14,Salary,3000.0,Income,income
```

---

## 9. Extend the App
- Add a web interface using Flask/Django.
- Integrate with bank APIs (Plaid, Yodlee).
- Build a mobile app with React Native.

## License
MIT