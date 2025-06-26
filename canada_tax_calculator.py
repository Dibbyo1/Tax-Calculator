import tkinter as tk
from tkinter import messagebox

def calculate_federal_tax(income):
    # 2025 Federal tax brackets (Basic Personal Amount = $15,705)
    brackets = [
        (55767 - 15705, 0.15),
        (111733 - 55767, 0.205),
        (173205 - 111733, 0.26),
        (246752 - 173205, 0.29)
    ]
    remaining = income - 15705
    tax = 0
    if remaining <= 0:
        return 0
    for bracket, rate in brackets:
        if remaining <= 0:
            break
        taxed = min(remaining, bracket)
        tax += taxed * rate
        remaining -= taxed
    if remaining > 0:
        tax += remaining * 0.33
    return tax

def calculate_ontario_tax(income):
    # 2025 Ontario provincial tax brackets
    brackets = [
        (49231, 0.0505),
        (98232 - 49231, 0.0915),
        (150000 - 98232, 0.1116),
        (220000 - 150000, 0.1216)
    ]
    remaining = income
    tax = 0
    for bracket, rate in brackets:
        if remaining <= 0:
            break
        taxed = min(remaining, bracket)
        tax += taxed * rate
        remaining -= taxed
    if remaining > 0:
        tax += remaining * 0.1316
    return tax

def calculate_cpp(income):
    # 2025 CPP contribution
    return max(0, min(income, 68500) - 3500) * 0.0595

def calculate_ei(income):
    # 2025 EI contribution
    return min(income, 63200) * 0.0166

# --- GUI Logic ---
def calculate():
    try:
        age = int(age_entry.get())
        income = float(income_entry.get())

        if income < 0 or age < 0:
            raise ValueError

        fed = calculate_federal_tax(income)
        prov = calculate_ontario_tax(income)
        cpp = calculate_cpp(income)
        ei = calculate_ei(income)
        total = fed + prov + cpp + ei
        net = income - total

        tax_free = income <= 15705
        underage_note = "Note: You're under 18, but still required to file taxes if income exceeds BPA.\n" if age < 18 else ""

        result_label.config(text=(
            f"{underage_note}"
            f"Federal Tax        : ${fed:,.2f}\n"
            f"Ontario Tax        : ${prov:,.2f}\n"
            f"CPP Contribution   : ${cpp:,.2f}\n"
            f"EI Contribution    : ${ei:,.2f}\n"
            f"-------------------------------\n"
            f"Total Deductions   : ${total:,.2f}\n"
            f"Net Income (After Tax): ${net:,.2f}\n"
            f"{'No federal tax due to BPA' if tax_free else ''}"
        ))

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric inputs.")

root = tk.Tk()
root.title("Canada Tax Calculator 2025")

tk.Label(root, text="Enter Age:").grid(row=0, column=0, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1)

tk.Label(root, text="Annual Income (CAD):").grid(row=1, column=0, sticky="e")
income_entry = tk.Entry(root)
income_entry.grid(row=1, column=1)

tk.Button(root, text="Calculate Tax", command=calculate).grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify="left", font=("Courier", 10))
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
