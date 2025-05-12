import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        disease TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

def add_patient():
    name = name_entry.get()
    disease = disease_entry.get()
    if name and disease:
        conn = sqlite3.connect('hospital.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patients (name, disease) VALUES (?, ?)", (name, disease))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Patient added successfully!")
        name_entry.delete(0, tk.END)
        disease_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both name and disease.")

def view_patients():
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, disease FROM patients")
    patients = cursor.fetchall()
    conn.close()
    patients_list.delete(0, tk.END)
    for patient in patients:
        patients_list.insert(tk.END, f"Name: {patient[0]}, Disease: {patient[1]}")

# Main window
root = tk.Tk()
root.title("Hospital Management System")

# Add patient frame
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

tk.Label(add_frame, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(add_frame)
name_entry.grid(row=0, column=1)

tk.Label(add_frame, text="Disease:").grid(row=1, column=0)
disease_entry = tk.Entry(add_frame)
disease_entry.grid(row=1, column=1)

add_button = tk.Button(add_frame, text="Add Patient", command=add_patient)
add_button.grid(row=2, columnspan=2, pady=5)

# View patients frame
view_frame = tk.Frame(root)
view_frame.pack(pady=10)

view_button = tk.Button(view_frame, text="View Patients", command=view_patients)
view_button.pack()

patients_list = tk.Listbox(view_frame, width=50)
patients_list.pack()

# Setup the database
setup_database()

# Start the GUI event loop
root.mainloop()
