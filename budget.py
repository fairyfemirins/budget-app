#!/usr/bin/env python3

import sqlite3
from datetime import datetime
import csv
import os

# Initialize database
DB_PATH = os.path.expanduser("~/projects/budget-app/budget.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            type TEXT CHECK(type IN ('expense', 'income')) NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT UNIQUE NOT NULL,
            budget_limit REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_transaction(date, description, amount, category, type_):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (date, description, amount, category, type)
        VALUES (?, ?, ?, ?, ?)
    """, (date, description, amount, category, type_))
    conn.commit()
    conn.close()


def get_transactions(month=None, year=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if month and year:
        cursor.execute("""
            SELECT * FROM transactions
            WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?
            ORDER BY date
        """, (f"{month:02d}", str(year)))
    else:
        cursor.execute("SELECT * FROM transactions ORDER BY date")
    transactions = cursor.fetchall()
    conn.close()
    return transactions


def set_budget(category, limit):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO budgets (category, budget_limit)
        VALUES (?, ?)
    """, (category, limit))
    conn.commit()
    conn.close()


def get_budget(category):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT budget_limit FROM budgets WHERE category = ?", (category,))
    budget = cursor.fetchone()
    conn.close()
    return budget[0] if budget else None


def export_to_csv(filename):
    transactions = get_transactions()
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Date', 'Description', 'Amount', 'Category', 'Type'])
        writer.writerows(transactions)


if __name__ == "__main__":
    init_db()