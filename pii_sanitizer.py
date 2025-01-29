import re
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF

# Regular expressions for detecting PII
PII_PATTERNS = {
    "Emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "Phone Numbers": r"\b\d{10}\b|\+\d{1,3}[-.\s]?\d{10}\b",
    "Credit Cards": r"\b\d{4}[-.\s]?\d{4}[-.\s]?\d{4}[-.\s]?\d{4}\b",
    "Addresses": r"\b\d{1,5}\s\w+\s\w+\b"
}

def sanitize_text(text):
    """Redact PII from text based on patterns"""
    for label, pattern in PII_PATTERNS.items():
        text = re.sub(pattern, "[REDACTED]", text)
    return text

def process_file(file_path):
    """Sanitize text or CSV files"""
    try:
        if file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                data = f.read()
            cleaned_data = sanitize_text(data)
            save_file(cleaned_data, file_path, "txt")
        
        elif file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
            for col in df.select_dtypes(include=[object]).columns:
                df[col] = df[col].astype(str).apply(sanitize_text)
            save_file(df, file_path, "csv")
        
        messagebox.showinfo("Success", "File sanitized and saved successfully!")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process file: {e}")

def save_file(data, original_path, file_type):
    """Save sanitized data as a new file"""
    sanitized_path = original_path.replace(".", "_sanitized.")
    if file_type == "txt":
        with open(sanitized_path, "w", encoding="utf-8") as f:
            f.write(data)
    elif file_type == "csv":
        data.to_csv(sanitized_path, index=False)

def generate_report(text):
    """Generate a PDF report summarizing redacted PII"""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output("pii_report.pdf")
    messagebox.showinfo("Success", "Report generated: pii_report.pdf")

def open_file():
    """Open a file dialog and process the selected file"""
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv")])
    if file_path:
        process_file(file_path)

# GUI
root = tk.Tk()
root.title("Data Privacy - PII Sanitizer")
root.geometry("400x200")

label = tk.Label(root, text="Select a file to sanitize:")
label.pack(pady=10)
button = tk.Button(root, text="Open File", command=open_file)
button.pack(pady=10)
root.mainloop()
