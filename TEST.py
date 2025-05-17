import tkinter as tk
from tkinter import messagebox, font
import pandas as pd

def calculate_tax(income, employment_type, residency_status):
    tax = 0
    if residency_status == "indian":
        if income <= 250000:
            tax = 0
        elif income <= 500000:
            tax = (income - 250000) * 0.05
        elif income <= 750000:
            tax = (income - 500000) * 0.1 + 12500
        elif income <= 1000000:
            tax = (income - 750000) * 0.15 + 37500
        elif income <= 1250000:
            tax = (income - 1000000) * 0.2 + 75000
        elif income <= 1500000:
            tax = (income - 1250000) * 0.25 + 125000
        else:
            tax = (income - 1500000) * 0.3 + 187500
        if employment_type == "government":
            tax *= 0.9  # 10% discount for government employees
    elif residency_status == "nri":
        if income > 250000:
            tax = (income - 250000) * 0.4
    return tax

def submit():
    name = name_entry.get().strip()
    gender = gender_var.get()
    employment_type = employment_var.get()
    residency_status = residency_var.get()

    if name == "":
        messagebox.showerror("Input Error", "Name cannot be empty.")
        return

    try:
        income = float(income_entry.get())
        if income < 0:
            raise ValueError("Income cannot be negative.")
        tax = calculate_tax(income, employment_type, residency_status)

        messagebox.showinfo("Tax Calculation", f"Total tax for {name} is: ₹{tax:.2f}")

        data = {
            "Name": name,
            "Gender": gender,
            "Employment Type": employment_type,
            "Residency Status": residency_status,
            "Annual Income": income,
            "Tax": tax
        }

        df = pd.DataFrame([data])
        df.to_csv("income_tax_data.csv", mode='a', header=not pd.io.common.file_exists("income_tax_data.csv"),
                  index=False)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid positive number for income.")

root = tk.Tk()
root.title("Income Tax Calculator")
root.geometry("400x320")
root.resizable(False, False)
bg_color = "#1a237e"  # dark navy blue
root.configure(bg=bg_color)

# Define fonts
heading_font = font.Font(family="Segoe UI", size=16, weight="bold")
label_font = font.Font(family="Segoe UI", size=11)
entry_font = font.Font(family="Segoe UI", size=11)
watermark_font = font.Font(family="Segoe UI", size=40, weight="bold")

# Watermark Canvas
canvas = tk.Canvas(root, width=400, height=320, bg=bg_color, highlightthickness=0)
canvas.place(x=0, y=0)

# Faint watermark text - slightly lighter blueish gray
canvas.create_text(200, 160, text="INDIAN GOVERNMENT",
                   font=watermark_font, fill="#9fa8da", angle=45, anchor="center")

# Frame for form inputs
form_frame = tk.Frame(root, bg=bg_color)
form_frame.place(relx=0.5, rely=0.5, anchor="center")

# Heading Label - bright gold/yellow
heading_label = tk.Label(form_frame, text="Income Tax Calculator", bg=bg_color, fg="#ffd700", font=heading_font)
heading_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

# Name Label and Entry
tk.Label(form_frame, text="Name:", bg=bg_color, fg="#e0f7fa", font=label_font).grid(row=1, column=0, sticky="e", padx=(0,12), pady=6)
name_entry = tk.Entry(form_frame, font=entry_font, relief="groove", bd=2, width=25)
name_entry.grid(row=1, column=1, sticky="w", pady=6)

# Gender Label and Radio Buttons
tk.Label(form_frame, text="Gender:", bg=bg_color, fg="#e0f7fa", font=label_font).grid(row=2, column=0, sticky="e", padx=(0,12), pady=6)
gender_var = tk.StringVar(value="male")
gender_frame = tk.Frame(form_frame, bg=bg_color)
gender_frame.grid(row=2, column=1, sticky="w", pady=6)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="male", bg=bg_color, fg="#81d4fa", font=label_font, selectcolor=bg_color).pack(side="left", padx=(0,10))
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="female", bg=bg_color, fg="#f48fb1", font=label_font, selectcolor=bg_color).pack(side="left")

# Employment Type Label and Radio Buttons
tk.Label(form_frame, text="Type of Employment:", bg=bg_color, fg="#e0f7fa", font=label_font).grid(row=3, column=0, sticky="e", padx=(0,12), pady=6)
employment_var = tk.StringVar(value="private")
employment_frame = tk.Frame(form_frame, bg=bg_color)
employment_frame.grid(row=3, column=1, sticky="w", pady=6)
tk.Radiobutton(employment_frame, text="Private", variable=employment_var, value="private", bg=bg_color, fg="#aed581", font=label_font, selectcolor=bg_color).pack(side="left", padx=(0,10))
tk.Radiobutton(employment_frame, text="Government", variable=employment_var, value="government", bg=bg_color, fg="#ffb74d", font=label_font, selectcolor=bg_color).pack(side="left")

# Residency Status Label and Radio Buttons
tk.Label(form_frame, text="Residency Status:", bg=bg_color, fg="#e0f7fa", font=label_font).grid(row=4, column=0, sticky="e", padx=(0,12), pady=6)
residency_var = tk.StringVar(value="indian")
residency_frame = tk.Frame(form_frame, bg=bg_color)
residency_frame.grid(row=4, column=1, sticky="w", pady=6)
tk.Radiobutton(residency_frame, text="Indian Resident", variable=residency_var, value="indian", bg=bg_color, fg="#4db6ac", font=label_font, selectcolor=bg_color).pack(side="left", padx=(0,10))
tk.Radiobutton(residency_frame, text="NRI", variable=residency_var, value="nri", bg=bg_color, fg="#9575cd", font=label_font, selectcolor=bg_color).pack(side="left")

# Income Label and Entry
tk.Label(form_frame, text="Annual Income (₹):", bg=bg_color, fg="#e0f7fa", font=label_font).grid(row=5, column=0, sticky="e", padx=(0,12), pady=6)
income_entry = tk.Entry(form_frame, font=entry_font, relief="groove", bd=2, width=25)
income_entry.grid(row=5, column=1, sticky="w", pady=6)

# Submit Button
submit_button = tk.Button(form_frame, text="Calculate Tax", bg="#357ABD", fg="white", font=label_font,
                          relief="flat", command=submit, padx=10, pady=6, cursor="hand2", width=20)
submit_button.grid(row=6, column=0, columnspan=2, pady=(15, 10))

submit_button.bind("<Enter>", lambda e: submit_button.config(bg="#4a90e2"))
submit_button.bind("<Leave>", lambda e: submit_button.config(bg="#357ABD"))

root.mainloop()