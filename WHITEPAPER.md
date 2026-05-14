# Budget App: Design and Rationale

## 1. Introduction
Budgeting tools are essential for personal finance management, yet existing solutions often suffer from:
- Overly complex interfaces.
- Lack of transparency (closed-source).
- High subscription costs.

This project addresses these gaps by providing a **minimal, open-source, and extensible** budgeting tool.

---

## 2. Design Decisions

### 2.1 Technology Stack
- **Language:** Python (widely accessible, easy to extend).
- **Database:** SQLite (zero-configuration, portable, file-based).
- **Interface:** CLI (low overhead, scriptable, easy to test).

### 2.2 Database Schema
- **Transactions Table:** Stores date, description, amount, category, and type (expense/income).
- **Budgets Table:** Stores category-specific budget limits.

**Rationale:**
- SQLite is ideal for single-user applications.
- The schema is normalized to avoid redundancy.

### 2.3 Core Features
1. **Transaction Management:** Add, list, and export transactions.
2. **Budget Limits:** Set and enforce monthly limits per category.
3. **Data Export:** CSV export for analysis in spreadsheets.

**Rationale:**
- Focus on **core functionality** first (MVP).
- Extensibility for future features (e.g., web interface, bank APIs).

### 2.4 Error Handling
- SQLite errors (e.g., duplicate categories) are propagated to the user.
- Input validation is minimal in the CLI but can be extended.

---

## 3. Future Work
- **Web Interface:** Flask/Django for a user-friendly dashboard.
- **Bank Integrations:** Plaid/Yodlee for automatic transaction imports.
- **Mobile App:** React Native for cross-platform support.
- **Cloud Sync:** Subscription-based sync across devices.

---

## 4. Conclusion
This project demonstrates how a **minimal, open-source** budgeting tool can address gaps in the current market. By focusing on **simplicity, portability, and extensibility**, it provides a foundation for future enhancements.

## License
MIT