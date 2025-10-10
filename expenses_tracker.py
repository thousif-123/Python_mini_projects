import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
from datetime import datetime, date
import csv

DB_FILE = "expenses.db"
DATE_FORMAT = "%Y-%m-%d"  

# ----------------- Database helpers -----------------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expense_date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_expense_db(expense_date, category, amount, description):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses (expense_date, category, amount, description) VALUES (?, ?, ?, ?)",
                (expense_date, category, amount, description))
    conn.commit()
    conn.close()

def delete_expense_db(expense_id):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def query_expenses(start_date=None, end_date=None):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    if start_date and end_date:
        cur.execute("SELECT id, expense_date, category, amount, description FROM expenses WHERE expense_date BETWEEN ? AND ? ORDER BY expense_date DESC",
                    (start_date, end_date))
    else:
        cur.execute("SELECT id, expense_date, category, amount, description FROM expenses ORDER BY expense_date DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

def sum_expenses(rows):
    return sum(r[3] for r in rows) 

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        root.title("Personal Expense Tracker")
        root.geometry("800x500")
        self.create_widgets()
        self.refresh_table()

    def create_widgets(self):
        frm_top = ttk.Frame(self.root, padding=10)
        frm_top.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(frm_top, text="Date (YYYY-MM-DD)").grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.date_var = tk.StringVar(value=date.today().strftime(DATE_FORMAT))
        self.date_entry = ttk.Entry(frm_top, textvariable=self.date_var, width=15)
        self.date_entry.grid(row=0, column=1, padx=5, pady=2)
        ttk.Label(frm_top, text="Category").grid(row=0, column=2, padx=5, pady=2, sticky=tk.W)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(frm_top, textvariable=self.category_var, values=[
            "Food", "Transport", "Utilities", "Shopping", "Health","Groceries","vegetables", "Other"
        ], width=18)
        self.category_combo.grid(row=0, column=3, padx=5, pady=2)
        self.category_combo.set("Other")

        ttk.Label(frm_top, text="Amount").grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        self.amount_var = tk.StringVar()
        self.amount_entry = ttk.Entry(frm_top, textvariable=self.amount_var, width=15)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(frm_top, text="Description").grid(row=1, column=2, padx=5, pady=2, sticky=tk.W)
        self.desc_var = tk.StringVar()
        self.desc_entry = ttk.Entry(frm_top, textvariable=self.desc_var, width=40)
        self.desc_entry.grid(row=1, column=3, padx=5, pady=2)

        self.add_btn = ttk.Button(frm_top, text="Add Expense", command=self.add_expense)
        self.add_btn.grid(row=0, column=4, rowspan=2, padx=10, pady=2, sticky=tk.N+tk.S)

        
        frm_mid = ttk.Frame(self.root, padding=(10, 0, 10, 0))
        frm_mid.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(frm_mid, text="From").grid(row=0, column=0, padx=5, pady=6, sticky=tk.W)
        self.from_var = tk.StringVar()
        self.from_entry = ttk.Entry(frm_mid, textvariable=self.from_var, width=12)
        self.from_entry.grid(row=0, column=1, padx=5, pady=6)

        ttk.Label(frm_mid, text="To").grid(row=0, column=2, padx=5, pady=6, sticky=tk.W)
        self.to_var = tk.StringVar()
        self.to_entry = ttk.Entry(frm_mid, textvariable=self.to_var, width=12)
        self.to_entry.grid(row=0, column=3, padx=5, pady=6)

        self.filter_btn = ttk.Button(frm_mid, text="Filter", command=self.filter_range)
        self.filter_btn.grid(row=0, column=4, padx=5, pady=6)

        self.show_all_btn = ttk.Button(frm_mid, text="Show All", command=self.refresh_table)
        self.show_all_btn.grid(row=0, column=5, padx=5, pady=6)

        self.export_btn = ttk.Button(frm_mid, text="Export CSV", command=self.export_csv)
        self.export_btn.grid(row=0, column=6, padx=5, pady=6)

        
        frm_table = ttk.Frame(self.root, padding=10)
        frm_table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        columns = ("id", "date", "category", "amount", "description")
        self.tree = ttk.Treeview(frm_table, columns=columns, show="headings", selectmode="extended")
        self.tree.heading("date", text="Date")
        self.tree.heading("category", text="Category")
        self.tree.heading("amount", text="Amount")
        self.tree.heading("description", text="Description")
        
        self.tree.column("id", width=0, stretch=False)
        self.tree.column("date", width=100, anchor=tk.CENTER)
        self.tree.column("category", width=120, anchor=tk.W)
        self.tree.column("amount", width=100, anchor=tk.E)
        self.tree.column("description", width=300, anchor=tk.W)

        vsb = ttk.Scrollbar(frm_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.LEFT, fill=tk.Y)

    
        frm_bottom = ttk.Frame(self.root, padding=10)
        frm_bottom.pack(side=tk.BOTTOM, fill=tk.X)

        self.delete_btn = ttk.Button(frm_bottom, text="Delete Selected", command=self.delete_selected)
        self.delete_btn.pack(side=tk.LEFT)

        self.total_label = ttk.Label(frm_bottom, text="Total: 0.00")
        self.total_label.pack(side=tk.RIGHT)

    def add_expense(self):
        d = self.date_var.get().strip()
        cat = self.category_var.get().strip()
        amt_text = self.amount_var.get().strip()
        desc = self.desc_var.get().strip()

        
        try:
            datetime.strptime(d, DATE_FORMAT)
        except Exception:
            messagebox.showwarning("Invalid date", f"Date must be YYYY-MM-DD (e.g. {date.today().strftime(DATE_FORMAT)})")
            return
        try:
            amt = float(amt_text)
        except Exception:
            messagebox.showwarning("Invalid amount", "Please enter a valid number for amount (e.g. 150.50)")
            return
        if not cat:
            messagebox.showwarning("Category", "Please select or type a category.")
            return

        add_expense_db(d, cat, amt, desc)
        self.amount_var.set("")
        self.desc_var.set("")
        self.refresh_table()

    def refresh_table(self):
       
        rows = query_expenses()
        self._populate_tree(rows)

    def _populate_tree(self, rows):
       
        for r in self.tree.get_children():
            self.tree.delete(r)
      
        for row in rows:
            _id, exp_date, cat, amt, desc = row
            self.tree.insert("", tk.END, values=(_id, exp_date, cat, f"{amt:.2f}", desc))
        total = sum_expenses(rows)
        self.total_label.config(text=f"Total: {total:.2f}")

    def delete_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Select", "Please select one or more entries to delete.")
            return
        if not messagebox.askyesno("Confirm", "Delete selected entries?"):
            return
        for item in sel:
            vals = self.tree.item(item, "values")
            expense_id = vals[0]
            delete_expense_db(expense_id)
        self.refresh_table()

    def filter_range(self):
        fr = self.from_var.get().strip()
        to = self.to_var.get().strip()
        if not fr or not to:
            messagebox.showwarning("Input", "Please enter both From and To dates in YYYY-MM-DD format.")
            return
        try:
            datetime.strptime(fr, DATE_FORMAT)
            datetime.strptime(to, DATE_FORMAT)
        except Exception:
            messagebox.showwarning("Invalid date", "Dates must be in YYYY-MM-DD format.")
            return
        rows = query_expenses(fr, to)
        self._populate_tree(rows)

    def export_csv(self):
        rows = []
        for item in self.tree.get_children():
            rows.append(self.tree.item(item, "values"))
        if not rows:
            messagebox.showinfo("No data", "No records to export.")
            return
      
        fpath = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files","*.csv")],
                                             initialfile=f"expenses_{date.today().strftime('%Y%m%d')}.csv")
        if not fpath:
            return
      
        try:
            with open(fpath, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id","date","category","amount","description"])
                for r in rows:
                    writer.writerow(r)
            messagebox.showinfo("Exported", f"Exported {len(rows)} rows to:\n{fpath}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not export CSV:\n{e}")


if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
